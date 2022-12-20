from django.db import models

# Create your models here.

class Article(models.Model):
    
    Article_Status = (
        ("DRAFT", "Draft"),
        ("PUBLISHED", "Published"),
    )
    author = models.CharField(max_length=100,null=True)
    title = models.CharField(max_length=128,unique=True)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True,null=True)
    status = models.CharField(
        max_length=16,
        choices=Article_Status,
        default=Article_Status[0],
    )

    def __str__(self):
        return self.title