from re import template
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from reports.forms import ReportForm
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import FormMixin

from books.models import Book
from .models import Report
from comments.models import Comment
from comments.forms import CommentForm

# Create your views here.
class ReportListView(ListView):
    model = Report
    context_object_name = "reports"

    def get_queryset(self):
        reports = Report.objects.all().order_by("-created_at") # Order Reports by newest
        return reports

class ReportDetailView(FormMixin, DetailView):
    model = Report
    context_object_name = "report"
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("users:login")
        
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.report = self.object
            comment.user = request.user
            comment.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        return context
    
    def get_success_url(self):
        return reverse("reports:report-detail", kwargs={"pk": self.object.pk})

class ReportCreateView(LoginRequiredMixin ,CreateView):
    model = Report
    template_name = "reports/report_form.html"
    form_class = ReportForm
    login_url = reverse_lazy("users:login")
    success_url = reverse_lazy("reports:report-list")

    def form_valid(self, form):
        book_title = form.cleaned_data.get("book_title")
        book_author = form.cleaned_data.get("book_author")

        book, created = Book.objects.get_or_create(title=book_title, author=book_author)

        report = form.save(commit=False)
        report.user = self.request.user
        report.book = book
        report.save()
        return redirect("reports:report-detail", pk=report.pk)

    def handle_no_permission(self):
        # Add a message to inform the user why they are being redirected
        messages.warning(self.request, "Please log in to create a report.")
        return super().handle_no_permission()

class ReportUpdateView(LoginRequiredMixin, UpdateView):
    model = Report
    template_name = "reports/report_form.html"
    # fields = ["book_title", "book_author", "title", "content"]
    form_class = ReportForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Edit Report"
        return context
    
    def get_success_url(self):
        return reverse_lazy("reports:report-detail", kwargs={"pk": self.object.pk})
    
    def get_object(self, queryset=None):
        report = super().get_object(queryset)
        if not (self.request.user.is_superuser) and (report.user != self.request.user):
            raise PermissionDenied("You do not have permission to edit this report.")
        return report

class ReportLikeView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        report = get_object_or_404(Report, pk=kwargs["pk"])
        if request.user in report.user_likes.all():
            report.user_likes.remove(request.user)
        else:
            report.user_likes.add(request.user)
        return HttpResponseRedirect(reverse("reports:report-detail", kwargs={"pk": report.pk}))

class ReportDeleteView(LoginRequiredMixin, DeleteView):
    model = Report
    success_url = reverse_lazy("reports:report-list")

    def get_object(self, queryset=None):
        report = super().get_object(queryset)
        if not (self.request.user.is_superuser) and (report.user != self.request.user):
            raise PermissionDenied("You do not have permission to delete this report.")
        return report