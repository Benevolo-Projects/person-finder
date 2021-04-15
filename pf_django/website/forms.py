from django import forms
from .models import Uploader, Find


class UploadForm(forms.ModelForm):
    class Meta:
        model = Uploader
        fields = ['fname_u', 'lname_u', 'email_u', 'mobile_u', 'image_l']


class FindForm(forms.ModelForm):
    class Meta:
        model = Find
        fields = ['image']