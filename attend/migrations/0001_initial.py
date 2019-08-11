# Generated by Django 3.0 on 2019-08-11 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='attendinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffnum', models.PositiveIntegerField()),
                ('attdate', models.DateField()),
                ('weekday', models.CharField(max_length=20)),
                ('starttime', models.CharField(max_length=10)),
                ('stoptime', models.CharField(max_length=10)),
                ('starttime5', models.CharField(max_length=10)),
                ('stoptime5', models.CharField(max_length=10)),
                ('starttime4', models.CharField(max_length=10)),
                ('stoptime4', models.CharField(max_length=10)),
                ('starttime3', models.CharField(max_length=10)),
                ('stoptime3', models.CharField(max_length=10)),
                ('hours', models.PositiveSmallIntegerField()),
                ('machine', models.CharField(max_length=10)),
                ('verify', models.CharField(max_length=30)),
            ],
        ),
    ]
