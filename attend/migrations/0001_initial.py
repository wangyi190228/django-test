# Generated by Django 3.0 on 2019-08-11 12:45

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
                ('verifyS', models.CharField(max_length=30)),
                ('stoptime', models.CharField(max_length=10)),
                ('verifyT', models.CharField(max_length=30)),
                ('machine', models.CharField(max_length=10)),
                ('hours', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
