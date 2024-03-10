from django import forms
from .models import CertificateHolder
from .models import CertificateInfo


class CertificateHolderForm(forms.ModelForm):
    class Meta:
        model = CertificateHolder
        fields = '__all__'
