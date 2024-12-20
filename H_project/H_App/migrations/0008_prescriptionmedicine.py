# Generated by Django 5.1.2 on 2024-11-18 09:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('H_App', '0007_alter_prescription_appointment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrescriptionMedicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('morning', models.BooleanField(default=False)),
                ('afternoon', models.BooleanField(default=False)),
                ('evening', models.BooleanField(default=False)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='H_App.medicine')),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicine_details', to='H_App.prescription')),
            ],
        ),
    ]
