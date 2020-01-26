# Generated by Django 3.0.2 on 2020-01-15 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=100)),
                ('trip_link', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aspect', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=600)),
                ('sentiment', models.CharField(max_length=25)),
                ('user', models.CharField(max_length=200)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abcr_home.Hotel')),
            ],
        ),
    ]