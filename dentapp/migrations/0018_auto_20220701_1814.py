# Generated by Django 3.2.12 on 2022-07-01 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dentapp', '0017_auto_20220701_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membershipcustomer',
            name='customer_email',
            field=models.EmailField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='membershipcustomer',
            name='customer_id',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='membershipcustomer',
            name='customer_number',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.CharField(max_length=150)),
                ('service_name', models.CharField(max_length=150)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]