from rest_framework import serializers
from ifit.core.models import *


class SerializerTreino(serializers.ModelSerializer):

    class Meta:
        model = Treino
        fields = '__all__'

class SerializerExercicio(serializers.ModelSerializer):

    class Meta:
        model = Exercicio
        fields = '__all__'

class SerializerExercicioTreino(serializers.ModelSerializer):

    class Meta:
        model = ExercicioTreino
        fields = '__all__'



class SerializerAvaliacao(serializers.ModelSerializer):

    class Meta:
        model = Avaliacao
        fields = '__all__'

class SerializerCliente(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'

class SerialiserUserCreate(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only = True
    )
    class Meta:
        model = CustomUser
        fields = ['username','email','password']

    def create(self,validated_data):
        user = super(SerialiserUserCreate,self).create(validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
            user.save()
        return user

class SerialiserUser(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id','username','first_name','last_name','frase','email','cidade','uf']

    def to_representation(self, instance):
        representation = super(SerialiserUser,self).to_representation(instance)
        representation['foto'] = instance.foto.url or None
        return representation

class SerialiserUserUpdate(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id','username','first_name','last_name','frase','email','cidade','uf']
class SerialiserUpdateFoto(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id','foto']

class SerializerConvite(serializers.ModelSerializer):

    class Meta:
        model = Convite
        fields = '__all__'

