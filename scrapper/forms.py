from django import forms

from .models import SAPUser


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class SAPUserForm(forms.ModelForm):
    class Meta:
        model = SAPUser
        fields = ("login", "password", "ip", "instance_number")
