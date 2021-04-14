from django import forms
from .models import Uploader


class UploadForm(forms.ModelForm):
    class Meta:
        model = Uploader
        fields = ['fname_u', 'lname_u', 'email_u', 'mobile_u']