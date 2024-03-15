from django.shortcuts import render, redirect
from .models import CertificateHolder
from .models import CertificateInfo
from .forms import CertificateHolderForm, CertificateInfoForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Succesfully logged in')
            return redirect('index')
        else:
            messages.success(request, 'There was an error loggin in, please try again')
            return redirect('index')
    else:
        return render(request, 'index.html', {})


def certificateholders(request):
    if request.user.is_authenticated:
        all_certificate_holders = CertificateHolder.objects.all()
        return render(request, 'certificate-holders.html', {'cert_holders': all_certificate_holders})
    else:
        messages.success(request, 'Please log in to view this page')
        return redirect('index')


def certificates(request):
    if request.user.is_authenticated:
        all_certificates = CertificateInfo.objects.all()
        return render(request, 'certificates.html', {'certs': all_certificates})
    else:
        messages.success(request, 'Please log in to view this page')
        return redirect('index')


def addholder(request):
    form = CertificateHolderForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Certificate Holder added successfully")
                return redirect('certificate-holders')
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
    else:
        messages.success(request, "You Must Be Logged In")
        return redirect('index')


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('index')


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'User has been successfully registered')
            return redirect('index')
    else:
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def holder_info(request, pk):
    if request.user.is_authenticated:
        holder_record = CertificateHolder.objects.get(id=pk)
        return render(request, 'holder-info.html', {'holder_record': holder_record})
    else:
        messages.success(request, 'Please log in to view this page')
        return redirect('index')


def delete_cert_holder(request, pk):
    if request.user.is_authenticated:
        delete_info = CertificateHolder.objects.get(id=pk)
        delete_info.delete()
        messages.success(request, 'Certificate holder deleted successfully')
        return redirect('certificate-holders')
    else:
        messages.success(request, "Please login to delete")
        return redirect('certificate-holders')


def update_cert_holder(request, pk):
    if request.user.is_authenticated:
        current_record = CertificateHolder.objects.get(id=pk)
        form = CertificateHolderForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Certificate Holder updated successfully')
            return redirect('certificate-holders')
        return render(request, 'update-certificate-holder.html', {'form': form})
    else:
        messages.success(request, "Please login to delete")
        return redirect('certificate-holders')


def certificate_info(request, pk):
    if request.user.is_authenticated:
        certificate_record = CertificateInfo.objects.get(certificate_number=pk)
        return render(request, 'certificate-info.html', {'certificate_record': certificate_record})
    else:
        messages.success(request, 'Please log in to view this page')
        return redirect('index')


def addcertificate(request):
    form = CertificateInfoForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Certificate added successfully")
                return redirect('certificates')
            else:
                certificate_holder = request.POST['certificate_holder']
                certificate_start_date = request.POST['certificate_start_date']
                certificate_duration = request.POST['certificate_duration']
                certificate_expiration_date = request.POST['certificate_expiration_date']
                certificate_active = request.POST['certificate_active']
                messages.success(request, 'Error, please check all the fields have been correctly submitted')
                return render(request, 'add-certificate.html', {
                    'certificate_holder': certificate_holder,
                    'certificate_start_date': certificate_start_date,
                    'certificate_duration': certificate_duration,
                    'certificate_expiration_date': certificate_expiration_date,
                    'certificate_active': certificate_active})
            messages.success(request, 'Certificate Details Successfully Added')
            return redirect('certificates')
        else:
            return render(request, 'add-certificate.html', {})
    else:
        messages.success(request, "You Must Be Logged In")
        return redirect('index')
