from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True, validators = [
                                    UniqueValidator(queryset=User.object.all())])
    
    password = serializers.CharField(write_only =True,required = True,validators=[
                                validate_password],style = {'input_type':'password'})
    
    password2 = serializers.CharField(write_only =True,required = True,style = {'input_type':'password'})
    
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'password2'
        )