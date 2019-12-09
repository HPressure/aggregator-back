from django.db import models

# Create your models here.


class Article(models.Model):
    newsId = models.AutoField(primary_key=True)
    newsTitle = models.CharField(max_length=300)
    newsImg = models.URLField(max_length=200, null='True')
    newsURL = models.URLField(max_length=300, null='True')

    class Meta:
        db_table = 'Test29'
