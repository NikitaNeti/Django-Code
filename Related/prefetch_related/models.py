from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    name= models.CharField(max_length=50)
    author = models.ForeignKey(Person,on_delete=models.CASCADE)
    publishers = models.ManyToManyField(Person,related_name='publishers')

    def __str__(self):
        return self.name