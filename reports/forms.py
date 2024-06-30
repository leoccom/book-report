from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["book_title", "book_author", "title", "content"]
    
    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        self.fields["book_title"].widget.attrs.update({"placeholder": "책 제목"})
        self.fields["book_author"].widget.attrs.update({"placeholder": "저자 이름"})
        self.fields["title"].widget.attrs.update({"placeholder": "독후감 제목"})
        self.fields["content"].widget.attrs.update({"placeholder": "독후감 내용을 작성해주세요."})