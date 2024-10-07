from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate

#from .models import Note

# for creating new users in registration - not needed

#class UserSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = User
        #fields = ["id", "username", "password"]
        #extra_kwargs = {"password": {"write_only": True}}

    #def create(self, validated_data):
        #print(validated_data)
        #user = User.objects.create_user(**validated_data)
        #return user


#class NoteSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = Note
        #fields = ["id", "title", "content", "created_at", "author"]
        #extra_kwargs = {"author": {"read_only": True}}

class GuestLoginSerializer(serializers.Serializer):
    username = serializers.CharField()  # This maps to the last_name field
    password = serializers.CharField(write_only=True)  # This maps to the hp_num field

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        # Use Django's authenticate method (which will call your custom backend)
        guest = authenticate(username=username, password=password)

        if guest is None:
            raise serializers.ValidationError("Invalid credentials")

        return guest  # Return the authenticated guest object