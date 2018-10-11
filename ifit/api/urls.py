from django.urls import path
from . import views


app_name = 'api'

urlpatterns = [

    path('clientes/', views.ClienteList.as_view(), name='api-cliente'),
    path('cliente/<int:pk>', views.ClienteDetalhe.as_view(), name='api-cliente-detalhe'),
    path('treinos/', views.TreinoList.as_view(), name='api-treino'),
    path('treino/<int:pk>', views.TreinoDetalhe.as_view(), name='api-treino-detalhe'),
    path('treinos-exercicio/', views.ExercicioTreinoList.as_view(), name='api-exercicio-treino'),
    path('treino-exercicio/<int:pk>', views.ExercicioTreinoDetalhe.as_view(), name='api-exercicio-treino-detalhe'),
    path('pesquisa-treino/<int:id>/<str:data_ini>/<str:data_fim>', views.PesquisaTreino.as_view(),
         name="api=pesquisa-treino"),

    path('exercicios',views.ExercicioList.as_view(),name="api=exercicio"),
    path('exercicio/<int:pk>',views.ExercicioDetalhe.as_view(),name="api-exercicio"),

    path('avaliacoes/',views.AvaliacaoList.as_view(),name='api-avaliacao'),
    path('avaliacao/<int:pk>', views.AvaliacaoDetalhe.as_view(), name='api-avaliacao-detalhe'),
    path('pesquisa-avaliacao/<int:id>/<str:data_ini>/<str:data_fim>',views.PesquisaAvaliacao.as_view(),name="api=pesquisa-avaliacao"),

    path('exercicios-treino/<int:pk>',views.ExerciciosTreinoList.as_view(),name="exercicios-treino"),
    #User
    path('registro/',views.RegisterList.as_view(),name='register'),
    path('update-user/<int:pk>',views.PerfilUpdate.as_view(),name="update-user"),
    path('list-users/',views.UserList.as_view(),name='list-users'),
    path('pesquisa-usuario/<str:username>', views.UserSearch.as_view(), name='pesquisa-usuario'),
    path('change-foto/<int:pk>',views.UpdateFoto.as_view(),name='change-foto'),

    #convites
    path('convidar/<int:id>',views.Convidar.as_view(),name='convidar'),
    path('convites-recebidos/', views.ConvitesRecebidos.as_view(), name="convites-recebidos"),
    path('convites-enviados/', views.ConvitesEnviados.as_view(), name="convites-enviados"),
    path('listar-amigos/', views.ListarAmigos.as_view(), name="listar-amigos"),
    path('aceitar-convite/<int:id>', views.AceitarConvite.as_view(), name="aceitar-convite"),
    path('remover-amigo/<int:id>', views.RemoverAmigo.as_view(), name="remover-amigo"),


]