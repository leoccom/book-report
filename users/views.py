from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class UserRegisterView(CreateView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

class UserLoginView(LoginView):
    template_name = "users/login.html"

    def get_success_url(self):
        next_url = self.request.GET.get("next")
        if next_url:
            return next_url
        return reverse_lazy("home")
    
class UserLogoutView(LogoutView):
    template_name = "users/logout.html"
    # next_page = reverse_lazy("home")

    def get_success_url(self):
        return reverse_lazy("home")

class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "users/profile_detail.html"
    context_object_name = "user"

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs["username"])
    
    # def get_object(self, queryset=None):
    #     user_profile = super().get_object(queryset=queryset)
    #     if self.request.user == user_profile:
    #         return user_profile
    #     else:
    #         raise Http404("You are not authorized to view this page.")

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "users/profile_update.html"
    form_class = UserUpdateForm

    def get_object(self):
        return self.request.user
    
    def get_success_url(self):
        return reverse_lazy("users:profile-detail", kwargs={"username": self.request.user.username})