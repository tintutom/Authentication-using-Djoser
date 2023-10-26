# from djoser.serializers import UserCreateSerializer
# from django.contrib.auth import get_user_model
# from rest_framework import serializers

# User = get_user_model()

# class UserCreateSerializer(UserCreateSerializer):
#     is_doctor = serializers.BooleanField(required=False)
#     is_staff = serializers.BooleanField(required=False)

#     class Meta(UserCreateSerializer.Meta):
#         model = User
#         fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password', 'is_doctor', 'is_staff')

#     def create(self, validated_data):
#         is_doctor = validated_data.pop('is_doctor')
#         is_staff = validated_data.pop('is_staff')
#         user = super().create(validated_data)

#         user.is_doctor = is_doctor
#         user.is_staff = is_staff
#         user.save()

#         return user


from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreateSerializer(serializers.ModelSerializer):
    is_doctor = serializers.BooleanField()
    is_staff = serializers.BooleanField()

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'is_doctor', 'is_staff')

    def create(self, validated_data):
        is_doctor = validated_data.pop('is_doctor', False)
        is_staff = validated_data.pop('is_staff', False)
        user = User.objects.create_user(**validated_data)
        user.is_doctor = is_doctor
        user.is_staff = is_staff
        user.save()
        return user

# from djoser.serializers import UserCreateSerializer
# from django.contrib.auth import get_user_model
# from rest_framework import serializers

# User = get_user_model()

# class CustomUserCreateSerializer(UserCreateSerializer):
#     is_doctor = serializers.BooleanField()
#     is_staff = serializers.BooleanField()

#     class Meta(UserCreateSerializer.Meta):
#         model = User
#         fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password', 'is_doctor', 'is_staff')

#     def create(self, validated_data):
#         print("create method is called")
#         is_doctor = validated_data.pop('is_doctor', False)
#         is_staff = validated_data.pop('is_staff', False)
#         print(f'is_doctor before: {is_doctor}')
#         print(f'is_staff before: {is_staff}')

#         user = super().create(validated_data)

#         user.is_doctor = is_doctor
#         user.is_staff = is_staff
#         print(f'is_doctor after: {user.is_doctor}')
#         print(f'is_staff after: {user.is_staff}')

#         user.save()

#         return user

        
