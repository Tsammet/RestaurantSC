from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import authenticate



class RegisterSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=Profile.USER_ROLE_CHOICES, default = 'user')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']

    def create(self, validated_data): # validated_data contiene los datos que han sido validados y procesados por el Serializer (datos JSON que pasaron las validaciones definidas).
        role = validated_data.pop('role', 'user') #se remueve el campo role del diccionario validated_data y si no está tomará 'user' como predeterminado
        user = User(**validated_data) #Crea una instancia de User con los datos restantes en validated_data (que deberían ser username, email, y password).
        user.set_password(validated_data['password'])
        user.save()
        Profile.objects.create(user=user, role=role) 
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username = username, password = password)
        if user is None:
            raise serializers.ValidationError("Credenciales incorrectas")
        
        data['user'] = user

        return data