from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import UserAccount,UserProfile


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'first_name', 'last_name', 'email', 'user_type']
        read_only_fields = ['id']

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email address is required.")
        if not '@' in value:
            raise serializers.ValidationError("Please enter a valid email address.")
        return value

    def validate_first_name(self, value):
        if not value:
            raise serializers.ValidationError("First name is required.")
        return value

    def validate_last_name(self, value):
        if not value:
            raise serializers.ValidationError("Last name is required.")
        return value

    def validate_user_type(self, value):
        user_types = [choice[0] for choice in UserAccount.USER_TYPE_CHOICES]
        if value not in user_types:
            raise serializers.ValidationError("Invalid user type.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        # Create UserProfile instance
        UserProfile.objects.create(user=instance,name=f'{instance.first_name}')
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields =['name']
        read_only_fields = ['id']