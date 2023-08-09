from django import forms

from .models import Reports

class ReportsForm(forms.ModelForm):
    """
    Form related to a Report.
    """
    class Meta:
        model = Reports
        fields = ("title", "body", "report_img", "img_caption")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control my-3"}),
            "body": forms.Textarea(attrs={"class": "form-control my-3"}),
            "img_caption": forms.TextInput(attrs={"class": "form-control my-3"}),
        }