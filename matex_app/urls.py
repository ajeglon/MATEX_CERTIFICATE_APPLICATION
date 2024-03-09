from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('certificate-holders', views.certificateholders, name='certificate-holders'),
    path('certificates', views.certificates, name='certificates'),
]