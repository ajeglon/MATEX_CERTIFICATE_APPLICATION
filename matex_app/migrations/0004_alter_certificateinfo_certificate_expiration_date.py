# Generated by Django 4.2.11 on 2024-03-15 18:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matex_app', '0003_alter_certificateinfo_certificate_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificateinfo',
            name='certificate_expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 16, 18, 28, 52, 102264)),
        ),
    ]