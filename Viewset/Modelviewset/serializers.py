from rest_framework import serializers
from .models import Article

Article_Status = (
        ('0', "Draft"),
        ("1", "Published"),
    )

class ArticleSerializer(serializers.ModelSerializer):
   class Meta:
       model = Article
       fields = ['id','author','title','created_at','status']



