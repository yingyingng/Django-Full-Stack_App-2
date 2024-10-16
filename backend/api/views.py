

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
#from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
#from .models import Note
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import GuestList
import pandas as pd
from django.http import JsonResponse
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import make_password
from .serializers import GuestLoginSerializer


#class NoteListCreate(generics.ListCreateAPIView):
    #serializer_class = NoteSerializer
    #permission_classes = [IsAuthenticated]

    #def get_queryset(self):
        #user = self.request.user
        #return Note.objects.filter(author=user)

    #def perform_create(self, serializer):
        #if serializer.is_valid():
            #serializer.save(author=self.request.user)
        #else:
            #print(serializer.errors)


#class NoteDelete(generics.DestroyAPIView):
    #serializer_class = NoteSerializer
    #permission_classes = [IsAuthenticated]

    #def get_queryset(self):
        #user = self.request.user
        #return Note.objects.filter(author=user)

#for creating new users in registration - not needed

#class CreateUserView(generics.CreateAPIView):
    #queryset = User.objects.all()
    #serializer_class = UserSerializer
    #permission_classes = [AllowAny]

class GuestLoginView(APIView):
    #permission_classes = [IsAuthenticated]
    
    def post(self, request):
        print("Request data:", request.data)  # This will print in the terminal
        serializer = GuestLoginSerializer(data=request.data)
        if serializer.is_valid():
            guest = serializer.validated_data
            print("Validated data:", guest)  # This will also print in the terminal
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            print("Serializer errors:", serializer.errors)  # This will print errors in the terminal
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#class LoginView(APIView):
    #permission_classes = [AllowAny]

    #def post(self, request):
        #username = request.data.get('username')
        #password = request.data.get('password')

        #try:
           # with open('/tmp/out.txt', 'w') as f:
                #print ("abcdef", file=f)
            #user = GuestList.objects.get(last_name=username, hp_num=password)

            #return JsonResponse(status=200)
        #except GuestList.DoesNotExist:
            #return JsonResponse({'error': 'Invalid username or password'}, status=200)
        
        #user = authenticate(requ
        # 
        # 
        # est, username=username, password=password)
        
        #if user is not None:
            #login(request, user)  # Log the user in (optional, if session management is needed)
            #return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        #else:
            #return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)

#def index(response, last_name):
    #ls = GuestList.objects.get(last_name=last_name)
    #item = ls.item_set.get(id = 1)
    #return HttpResponse("<h1>%s</h1>" % (ls.last_name, str(item.text)))