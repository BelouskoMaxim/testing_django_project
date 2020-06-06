from django.db import models

# Create your models here.
class Specialization(models.Model):
    Name = models.CharField(max_length=30)

    def __str__(self):
        return self.Name

class City(models.Model):
    Name = models.CharField(max_length=30)

    def __str__(self):
        return self.Name


class Manufacture(models.Model):
    Name = models.CharField(max_length=256)
    City = models.ManyToManyField('City')
    Specialization = models.ManyToManyField('Specialization')
    ReadyToOrders = models.BooleanField()
    AnswerMean = models.IntegerField()
    def __str__(self):
        return self.Name

