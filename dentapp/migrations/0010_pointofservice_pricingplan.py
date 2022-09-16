# Generated by Django 3.2.12 on 2022-06-30 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dentapp', '0009_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pointofservice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_of_service', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Pricingplan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pricingplan')),
                ('name', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('point_of_services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dentapp.pointofservice')),
            ],
            options={
                'verbose_name': 'Pricing Plan',
                'verbose_name_plural': 'Pricing Plan',
            },
        ),
    ]
