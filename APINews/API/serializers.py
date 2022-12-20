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


# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField(max_length=100)
#     title = serializers.CharField(max_length=128,allow_blank=True)    
#     content = serializers.CharField(max_length=200)
#     created_at = serializers.DateField()
#     status = serializers.MultipleChoiceField(choices=Article_Status,default=Article_Status[0])
    
#     def create(self, validated_data):
#         return Article.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.author = validated_data.get('author',instance.author)
#         instance.title = validated_data.get('title',instance.title)
#         instance.content = validated_data.get('content',instance.content)
#         instance.created_at = validated_data.get('created_at',instance.created_at)
#         instance.status = validated_data.get('status',instance.status)
#         instance.save()
#         return instance 
