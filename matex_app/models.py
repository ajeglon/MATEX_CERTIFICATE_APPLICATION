from django.db import models


# Create your models here.
class CertificateHolder(models.Model):
    nhs_number = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    date_of_birth = models.DateField()

    def __str__(self):
        return str(self.nhs_number) + " - " + f'{self.first_name} {self.last_name}'


class CertificateInfo(models.Model):
    certificate_holder = models.ForeignKey(CertificateHolder,on_delete=models.CASCADE)
    certificate_number = models.AutoField(primary_key=True)
    certificate_start_date = models.DateField()
    certificate_duration = models.DurationField()
    certificate_expiration_date = models.DateField()
    certificate_active = models.BooleanField()

    def __str__(self):
        return str(self.certificate_number) + " - " + f'{self.certificate_holder}'


