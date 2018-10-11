from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import *
from ifit.core.models import *

class AvaliacaoList(generics.ListCreateAPIView):
    serializer_class = SerializerAvaliacao
    queryset = Avaliacao.objects.all()
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        contexto = ('request',request)
        queryset = Avaliacao.objects.filter(professor=request.user.id)
        serializer = SerializerAvaliacao(queryset,context=contexto,many=True)
        return Response(serializer.data)



class AvaliacaoDetalhe(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SerializerAvaliacao
    queryset = Avaliacao.objects.all()
    permission_classes = (IsAuthenticated,)


class ClienteList(generics.ListCreateAPIView):
    serializer_class = SerializerCliente
    queryset = Cliente.objects.all()
    permission_classes = (IsAuthenticated,)


class ClienteDetalhe(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SerializerCliente
    queryset = Cliente.objects.all()
    permission_classes = (IsAuthenticated,)




class TreinoList(generics.ListCreateAPIView):
    serializer_class = SerializerTreino
    queryset = Treino.objects.all()
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        user_loged = request.user.id
        contexto = ('request',request)
        queryset = Treino.objects.filter(professor_id=user_loged)
        serializer = SerializerTreino(queryset,context=contexto,many=True)
        return Response(serializer.data)




class TreinoDetalhe(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SerializerTreino
    queryset = Treino.objects.all()
    permission_classes = (IsAuthenticated,)


class ExercicioTreinoList(generics.ListCreateAPIView):
    serializer_class = SerializerExercicioTreino
    queryset = ExercicioTreino.objects.all()
    permission_classes = (IsAuthenticated,)


class ExercicioTreinoDetalhe(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SerializerExercicioTreino
    queryset = ExercicioTreino.objects.all()
    permission_classes = (IsAuthenticated,)


class ExercicioList(generics.ListCreateAPIView):
    serializer_class = SerializerExercicio
    queryset = Exercicio.objects.all()
    permission_classes = (IsAuthenticated,)



class ExercicioDetalhe(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SerializerExercicio
    queryset = Exercicio.objects.all()
    permission_classes = (IsAuthenticated,)


class ExerciciosTreinoList(APIView):
    permission_classes = (IsAuthenticated,)

    #deleta exercicio do treino pegando id do exercicio do treino
    def delete(self,request,pk):
        contexto = {'request', request}
        queryset = ExercicioTreino.objects.filter(id=pk)
        queryset.delete()
        return Response(queryset)

    #lista todos os exercicios do treino equivalente
    def get(self,request,pk):
        contexto = {'request',request}
        queryset = ExercicioTreino.objects.filter(treino=pk)
        serializer = SerializerExercicioTreino(queryset,context = contexto,many=True)
        return Response(serializer.data)

class RegisterList(generics.CreateAPIView):
    serializer_class = SerialiserUserCreate
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)


class PerfilUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = SerialiserUserUpdate
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)



class UserList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        contexto = ('request',request)
        queryset = CustomUser.objects.all().exclude(id=request.user.id)
        serializer = SerialiserUser(queryset,context=contexto,many=True)
        return Response(serializer.data)

class UpdateFoto(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SerialiserUpdateFoto
    queryset = CustomUser.objects.all()



class UserSearch(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,username):
        contexto = ('request',request)
        queryset = CustomUser.objects.filter(username=username).exclude(id=request.user.id)
        serializer = SerialiserUser(queryset,context=contexto,many=True)
        return Response(serializer.data)



class Convidar(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request,id):
        user_loged = CustomUser.objects.get(id=request.user.id)
        convidado = CustomUser.objects.get(id=id)
        if not convidado in user_loged.friends.all():
            user_loged.convite(convidado)
        return Response ('Usuario Convidado')


class ConvitesRecebidos(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        user_loged = request.user.id
        contexto = ('request',request)
        queryset = Convite.objects.filter(convidado=user_loged)
        serializer = SerializerConvite(queryset,context=contexto,many=True)
        return Response(serializer.data)

    #Atualiza a solicitação para aceita
    permission_classes = (IsAuthenticated,)
    def put(self,request,id):
        contexto = ('request',request)
        queryset = Convite.objects.filter(id=id).update(status="ACE")
        return Response('Aceito')

    def delete(self,request,id):
        contexto = ('request',request)
        queryset = Convite.objects.filter(id=id).update(status="REG")
        return Response('Regeitada')


class ConvitesEnviados(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        user_loged = request.user.id
        contexto = ('request',request)
        queryset = Convite.objects.filter(convidante=user_loged)
        serializer = SerializerConvite(queryset,context=contexto,many=True)
        return Response(serializer.data)

class AceitarConvite(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request,id):
        convite = Convite.objects.get(id=id)
        convite.aceitar()
        return Response('Aceito')

class RemoverAmigo(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request,id):
        user_loged = CustomUser.objects.get(id=request.user.id)
        user_loged.remove_friend(id)

        return Response('Amigo Removido')

class ListarAmigos(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        user_loged = request.user.id
        contexto = ('request',request)
        user = CustomUser.objects.get(id=user_loged)
        serialize = user.friends.all()
        serializer = SerialiserUser(serialize,context=contexto,many=True)
        return Response(serializer.data)


class PesquisaAvaliacao(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request,id,data_ini,data_fim):
        contexto = ('request',request)

        avaliacoes = Avaliacao.objects.filter(professor=request.user.id,data_create__range=(data_ini,data_fim),aluno=id)
        serializer = SerializerAvaliacao(avaliacoes,context=contexto,many=True)
        return Response(serializer.data)

class PesquisaTreino(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,id,data_ini,data_fim):
        contexto = ('request',request)
        treinos = Treino.objects.filter(professor=request.user.id,data_inicio__range=(data_ini,data_fim),aluno=id)
        serializer = SerializerTreino(treinos,context=contexto,many=True)
        return Response(serializer.data)

