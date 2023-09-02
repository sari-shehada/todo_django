from rest_framework import serializers
from .models import TODO, AppUser


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ('id', 'name')


class TODOSerializer(serializers.ModelSerializer):
    class Meta:
        model = TODO
        fields = ('id', 'title', 'details', 'isFinished', 'postedBy')
