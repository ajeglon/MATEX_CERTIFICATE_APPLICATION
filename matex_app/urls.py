from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('certificate-holders', views.certificateholders, name='certificate-holders'),
    path('certificates', views.certificates, name='certificates'),
    path('add-holder', views.addholder, name='add-holder'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register')
]
