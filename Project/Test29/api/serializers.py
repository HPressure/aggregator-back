from rest_framework import serializers
from Test29.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('newsId', 'newsTitle', 'newsImg', 'newsURL')
