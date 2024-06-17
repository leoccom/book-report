from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["book_title", "book_author", "title", "content"]
        # widgets = {
        #     "book_title": forms.TextInput(attrs={"placeholder": "책 제목"}),
        #     "book_author": forms.TextInput(attrs={"placeholder": "책 저자"}),
        #     "title": forms.TextInput(attrs={"placeholder": "글 제목"}),
        #     "content": forms.Textarea(attrs={"placeholder": ""})
        # }
    
    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        self.fields["book_title"].widget.attrs.update({"placeholder": "책 제목"})
        self.fields["book_author"].widget.attrs.update({"placeholder": "책 저자"})
        self.fields["title"].widget.attrs.update({"placeholder": "글 제목"})
        self.fields["content"].widget.attrs.update({"placeholder": ""})