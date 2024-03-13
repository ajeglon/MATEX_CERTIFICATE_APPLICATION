from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('certificate-holders', views.certificateholders, name='certificate-holders'),
    path('certificates', views.certificates, name='certificates'),
    path('add-holder', views.addholder, name='add-holder'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('holder-info/<int:pk>/', views.holder_info, name='holder-info'),
    path('delete_cert_holder/<int:pk>/', views.delete_cert_holder, name='delete-holder-info'),
    path('update_cert_holder/<int:pk>/', views.update_cert_holder, name='update-holder-info')
]
