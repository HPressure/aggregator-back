from django.db import models

# Create your models here.


class Show(models.Model):
    Id = models.AutoField(primary_key=True, max_length=11)
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=500, null='True')
    Img = models.URLField(max_length=200, null='True')
    BuyUrl = models.URLField(max_length=200, null='True')
    Date = models.CharField(max_length=50)
    Hour = models.CharField(max_length=10)

    class Meta:
        db_table = 'ArhDrama'
