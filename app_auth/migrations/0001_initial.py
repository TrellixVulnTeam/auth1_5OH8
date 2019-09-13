# Generated by Django 2.0.6 on 2019-08-26 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Driver_Name', models.CharField(max_length=10)),
                ('Vehicle_Number', models.CharField(max_length=10)),
                ('Sim_Number', models.CharField(max_length=10)),
                ('IMEI_Number', models.CharField(max_length=10)),
                ('Device_Model', models.CharField(choices=[('P', 'Prime 07'), ('B', 'Benley 140'), ('O', 'OBDII'), ('R', 'Optimus 2.0')], max_length=20)),
                ('Vehicle_Licence_No', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_name', models.CharField(max_length=10)),
                ('Company_address', models.TextField(max_length=50)),
                ('Phone_number', models.CharField(max_length=10)),
            ],
        ),
    ]
