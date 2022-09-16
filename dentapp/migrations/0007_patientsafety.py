# Generated by Django 3.2.12 on 2022-05-10 05:39

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentapp', '0006_membershipbannerimage_membershipdescription_membershipplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientSafety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='PatientSafety')),
                ('short_description', models.TextField()),
                ('long_description', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'verbose_name': 'PatientSafety',
                'verbose_name_plural': 'PatientSafeties',
            },
        ),
    ]