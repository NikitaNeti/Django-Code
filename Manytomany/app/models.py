from django.db import models

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)


    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline

# Create a few Publicatins

# p1 = Publication(title='The Python Journal')
# p1.save()

# Create an Artice:

# a1 = Article(headline='Django lets you build web apps easily')
# a1.save()

# Associate the Article with a Publication 
# arc = a1.publications.add(p1)


# p2 = Publication(title='Science News')
# p2.save()





