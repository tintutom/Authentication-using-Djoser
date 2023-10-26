
from rest_framework import serializers
from django.contrib.auth.models import User

class UserCreateSerializer(serializers.ModelSerializer):
    is_staff = serializers.BooleanField(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff')