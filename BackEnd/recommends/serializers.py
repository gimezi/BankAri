from rest_framework import serializers
from .models import Recommend
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','username')


class RecommendSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Recommend
        fields = '__all__'
        # read_only_fields = ('username',)
