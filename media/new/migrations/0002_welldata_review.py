# Generated by Django 5.1.1 on 2024-09-26 07:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WellData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=255)),
                ('block', models.CharField(max_length=255)),
                ('grampanchayat', models.CharField(max_length=255)),
                ('site_name', models.CharField(max_length=255)),
                ('location_details', models.TextField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('ownership_type', models.CharField(max_length=50)),
                ('government_source', models.CharField(max_length=255)),
                ('diameter_of_well', models.FloatField()),
                ('height_of_measuring_point', models.FloatField()),
                ('image_upload', models.ImageField(blank=True, null=True, upload_to='well_images/')),
                ('status', models.CharField(max_length=50)),
                ('month_year', models.DateField()),
                ('ground_water_level_updated_2024', models.FloatField()),
                ('ground_water_level_updated_2023', models.FloatField()),
                ('ground_water_level_updated_2022', models.FloatField()),
                ('depth_of_well', models.FloatField()),
                ('type_of_well', models.CharField(max_length=255)),
                ('well_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_name', models.CharField(max_length=100)),
                ('review_title', models.CharField(max_length=85)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new.task')),
            ],
        ),
    ]
