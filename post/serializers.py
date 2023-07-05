from rest_framework import serializers
from .models import Category        # точка чтобы указать на том же уровне


class PostSerializers(serializers.Serializer):
    category = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all())
    title = serializers.CharField(max_length = 100)
    body = serializers.CharField(allow_blank = True, allow_null = True)
    created_at = serializers.DateTimeField(read_only = True)

