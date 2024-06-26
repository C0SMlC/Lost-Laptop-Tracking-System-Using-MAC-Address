# Generated by Django 5.0.3 on 2024-04-07 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_remove_user_date_joined_remove_user_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StolenLaptopDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('aadhaar_no', models.CharField(max_length=12)),
                ('approximate_time', models.TimeField()),
                ('date', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('contact_no', models.CharField(max_length=15)),
                ('brand', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('model_no', models.CharField(max_length=100)),
                ('mac_address', models.CharField(max_length=17)),
            ],
        ),
    ]
