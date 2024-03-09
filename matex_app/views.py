from django.shortcuts import render
from .models import CertificateHolder
from .models import CertificateInfo


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def certificateholders(request):
    all_certificate_holders = CertificateHolder.objects.all()
    return render(request, 'certificate-holders.html', {'cert_holders': all_certificate_holders})


def certificates(request):
    all_certificates = CertificateInfo.objects.all()
    return render(request, 'certificates.html', {'certs': all_certificates})
