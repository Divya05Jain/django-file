from django.db import models

# Create your models here.

class Task(models.Model):

    tile = models.CharField(max_length=85)

    content = models.CharField(max_length=300)

    date_posted = models.DateTimeField(auto_now_add=True)

class Review(models.Model):

    reviewer_name = models.CharField(max_length=100)

    review_title = models.CharField(max_length=85)

    task = models.ForeignKey(Task, on_delete=models.CASCADE)


class WellData(models.Model):
    district = models.CharField(max_length=255)
    block = models.CharField(max_length=255)
    grampanchayat = models.CharField(max_length=255)
    site_name = models.CharField(max_length=255)
    location_details = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    ownership_type = models.CharField(max_length=50)
    government_source = models.CharField(max_length=255)
    diameter_of_well = models.FloatField()
    height_of_measuring_point = models.FloatField()
    image_upload = models.ImageField(upload_to='well_images/', blank=True, null=True)  # Make sure to handle media files
    status = models.CharField(max_length=50)
    month_year = models.DateField()  # Adjust format if needed
    ground_water_level_updated_2024 = models.FloatField()
    ground_water_level_updated_2023 = models.FloatField()
    ground_water_level_updated_2022 = models.FloatField()
    depth_of_well = models.FloatField()
    type_of_well = models.CharField(max_length=255)
    well_id = models.CharField(max_length=255)

    def __str__(self):
        return self.site_name
