# Generated by Django 3.2.7 on 2022-11-06 09:12

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=django_countries.fields.CountryField(default='CA', max_length=2, verbose_name='Country'),
        ),
    ]
