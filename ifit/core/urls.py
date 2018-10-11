from django.urls import path
from . import views


app_name='core'

urlpatterns=[
    #TODO Api's
    path('',views.Index.as_view(),name='index'),
    path('cliente',views.ClienteList.as_view(),name='cliente-list'),
    path('cliente-create',views.ClienteCreate.as_view(),name='cliente-create'),
    path('cliente-update/<int:pk>',views.ClienteUpdate.as_view(),name='cliente-update'),

    path('treino-list/',views.TreinoList.as_view(),name='treino-list'),
    path('treino-create/', views.TreinoCreate.as_view(), name='treino-create'),
    path('treino-update/<int:pk>', views.TreinoUpdate.as_view(), name='treino-update'),
    path('exercicio-create/',views.ExercicioCreate.as_view(),name='exercicio-create'),

    path('avaliacao-list',views.AvaliacaoList.as_view(),name='avaliacao-list'),
    path('avaliacao-create', views.AvaliacaoCreate.as_view(), name='avaliacao-create'),
    path('avaliacao-update/<int:pk>', views.AvaliacaoUpdate.as_view(), name='avaliacao-update')
]
