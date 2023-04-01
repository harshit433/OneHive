from django.db import models
from home.models import contact
from django_resized import ResizedImageField
# Create your models here.

class allevents(models.Model):

    event_type   = models.CharField(max_length=50,null=True)
    event_name   = models.CharField(max_length=50,null=True)
    event_venue  = models.CharField(max_length=50,null=True)
    event_info   = models.TextField(null=True)
    banner_image = ResizedImageField(upload_to='images/',size = [800,600],null = True)
    team_size    = models.IntegerField(null=True)
    deadline     = models.DateField(auto_now_add=False)
    eligibility  = models.CharField(null=True, max_length=50)
    category     = models.CharField(null=True, max_length=50)
    event_date   = models.DateField(auto_now_add=False)
    info         = models.TextField(null=True)
    guidlines    = models.TextField()
    rules        = models.TextField()
    event_image  = models.ImageField(upload_to='images/', max_length=None)
    ist_prize    = models.IntegerField(null=True)
    second_prize = models.IntegerField( null=True)
    third_prize  = models.IntegerField(null=True)
    participation = models.CharField(max_length=50,null = True)
    contact_name = models.CharField(max_length=50,null = True)
    contact_no   = models.IntegerField(null=True)
    reference_url= models.URLField(max_length=200,null=True)



