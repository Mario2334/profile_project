from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(max_length=100,
    #     style={ 'placeholder': 'Username' ,'base_template':'input.html'})
    # password = serializers.CharField(
    #     max_length=100,
    #     style={'input_type': 'password', 'placeholder': 'Password'}
    # )
    #
    # email = serializers.EmailField(
    #     max_length=100,
    #     style={'placeholder': 'Email', 'autofocus': True}
    # )
    # first_name = serializers.CharField(
    #     max_length=100,
    #     style={'placeholder': 'Email', 'autofocus': True}
    # )
    # last_name = serializers.CharField(max_length=100,
    #     style={'placeholder': 'Email', 'autofocus': True})
    #
    # profile_pic = serializers.ImageField()
    #
    # bio = serializers.CharField(max_length=400 ,
    #                             style={'placeholder': 'Bio' })

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.is_active = True
        user.set_password(raw_password=password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ['username' , 'password' , 'email' , 'first_name' , 'last_name' ,'profile_pic' , 'bio']
