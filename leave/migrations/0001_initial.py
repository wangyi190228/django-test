# Generated by Django 3.0 on 2019-08-29 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alapply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffnum', models.PositiveIntegerField()),
                ('alstartdate', models.DateField()),
                ('starttime', models.CharField(max_length=10)),
                ('alstopdate', models.DateField()),
                ('stoptime', models.CharField(max_length=10)),
                ('aldays', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Alinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffnum', models.PositiveIntegerField()),
                ('applicant', models.CharField(max_length=32)),
                ('aplitime', models.DateTimeField()),
                ('reason', models.TextField()),
                ('leader', models.CharField(max_length=32)),
                ('fapltime', models.DateTimeField()),
                ('fapl', models.BooleanField()),
                ('freason', models.TextField()),
                ('hr', models.CharField(max_length=32)),
                ('sapl', models.BooleanField()),
                ('sreason', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='staffAl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffnum', models.PositiveIntegerField()),
                ('startdate', models.DateField()),
                ('stopdate', models.DateField()),
                ('expirydate', models.DateField()),
                ('Alsum', models.PositiveSmallIntegerField()),
                ('remain', models.PositiveSmallIntegerField()),
                ('used', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
