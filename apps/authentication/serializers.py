from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User
class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""
    password = serializers.CharField(
        max_length=255,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)
    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response
        fields = ('email', 'first_name', 'last_name', 'password', 'token')
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    """Serializer login requests and signin user"""
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'token')
    def validate(self, data):
        first_name = data.get('first_name', None)
        last_name = data.get('last_name', None)
        email = data.get('email', None)
        password = data.get('password', None)
        # Raise an exception if a
        # username is not provided.
        if email is None:
            raise serializers.ValidationError(
                'An email is required to login'
            )
        # Raise an exception if a
        # password is not provided.
        if password is None:
            raise serializers.ValidationError(
                'A password is required to login'
            )
        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with that email or password was not found'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated'
            )
        return {
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "token": user.token
        }