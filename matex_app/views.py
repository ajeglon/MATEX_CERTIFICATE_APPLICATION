from django.shortcuts import render, redirect
from .models import CertificateHolder
from .models import CertificateInfo
from . forms import CertificateHolderForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def certificateholders(request):
    all_certificate_holders = CertificateHolder.objects.all()
    return render(request, 'certificate-holders.html', {'cert_holders': all_certificate_holders})


def certificates(request):
    all_certificates = CertificateInfo.objects.all()
    return render(request, 'certificates.html', {'certs': all_certificates})


def addholder(request):
    if request.method == 'POST':
        form = CertificateHolderForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            nhs_number = request.POST['nhs_number']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            date_of_birth = request.POST['date_of_birth']
            messages.success(request, 'Error, please check all the fields have been correctly submitted')
            return render(request, 'add-holder.html', {'nhs_number': nhs_number,
                                                       'first_name': first_name,
                                                       'last_name': last_name,
                                                       'email': email,
                                                       'date_of_birth': date_of_birth})
        messages.success(request, 'Certificate Holder Details Successfully Added')
        return redirect('certificate-holders')
    else:
        return render(request, 'add-holder.html', {})
