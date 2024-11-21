from django.db import models

# Create your models here.
class OtherModel(models.Model):
    name = models.CharField(max_length=100)


class Article(models.Model):
    auto_field = models.AutoField(primary_key=True) 
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    