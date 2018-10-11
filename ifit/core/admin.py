from django.contrib import admin
from .models import Cliente,Avaliacao,Musculo,Exercicio,Treino,ExercicioTreino,Convite,CustomUser


class ItemExercicioTreino(admin.TabularInline):
    model = ExercicioTreino

class TreinoAdmin(admin.ModelAdmin):
    inlines = [ItemExercicioTreino]


class AdminAvaliacao(admin.ModelAdmin):
    fieldsets = [
        ('Cabeçalho',{'fields':['professor','aluno','data','altura','peso','ombro','peitoral','costas','cintura','quadril']}),
        ('Esquerdo',{'fields':['biseps_esq',
                               'antebraco_esq',
                               'coxa_esq',
                               'pantirrilha_esq']}),
        ('Direito',{'fields':['biseps_dir',
                           'antebraco_dir',
                           'coxa_dir',
                           'pantirrilha_dir']}),

    ]
admin.site.register(Convite)
admin.site.register(CustomUser)
admin.site.register(Treino,TreinoAdmin)
admin.site.register(Avaliacao,AdminAvaliacao)
admin.site.register([Cliente,Musculo,Exercicio])
