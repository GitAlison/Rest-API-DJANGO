from django import forms
from .models import Treino, ExercicioTreino,Avaliacao
from django.forms import inlineformset_factory


class TreinoForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = ['professor','aluno','data_inicio','data_fim']
        widgets = {
            'profesor': forms.Select(attrs={'class':'form-control'}),
            'aluno': forms.Select(attrs={'class':'form-control'}),
            'data': forms.TextInput(attrs={'class': 'form-control','type':'date'})
        }


class ExercicioTreinoForm(forms.ModelForm):
    class Meta:
        model = ExercicioTreino
        fields = ['dia','treino','exercicio','repeticoes','sequencias','carga',
                  'duracao','descanso']
        widgets = {
            'dia':forms.Select(attrs={'class':'form-control'}),
            'exercicio': forms.Select(attrs={'class': 'form-control select2'}),
            'repeticoes': forms.TextInput(attrs={'class': 'form-control'}),
            'sequencias': forms.TextInput(attrs={'class': 'form-control'}),
            'carga': forms.TextInput(attrs={'class': 'form-control','type':'decimal'}),
            'duracao': forms.TextInput(attrs={'class': 'form-control','type':'time'}),
            'descanso': forms.TextInput(attrs={'class': 'form-control','type':'time'}),
        }
class FormAvaliacao(forms.ModelForm):

    class Meta:
        model = Avaliacao
        fields = '__all__'
        widgets = {
            'professor': forms.Select(attrs={'class':'form-control'}),
            'aluno': forms.Select(attrs={'class':'form-control'}),
            'data': forms.TextInput(attrs={'class': 'form-control','type':'date'}),
            'altura': forms.TextInput(attrs={'class': 'form-control'}),
            'peso': forms.TextInput(attrs={'class': 'form-control'}),
            'ombro': forms.TextInput(attrs={'class': 'form-control'}),
            'torax': forms.TextInput(attrs={'class': 'form-control'}),
            'cintura': forms.TextInput(attrs={'class': 'form-control'}),
            'quadril': forms.TextInput(attrs={'class': 'form-control'}),
            'biseps_esq': forms.TextInput(attrs={'class': 'form-control'}),
            'biseps_dir': forms.TextInput(attrs={'class': 'form-control'}),
            'antebraco_esq': forms.TextInput(attrs={'class': 'form-control'}),
            'antebraco_dir': forms.TextInput(attrs={'class': 'form-control'}),
            'coxa_esq': forms.TextInput(attrs={'class': 'form-control'}),
            'coxa_dir': forms.TextInput(attrs={'class': 'form-control'}),
            'panturrilha_esq': forms.TextInput(attrs={'class': 'form-control'}),
            'panturrilha_dir': forms.TextInput(attrs={'class': 'form-control'}),
        }

ExercicioFormset = inlineformset_factory(Treino, ExercicioTreino,
                                         form=ExercicioTreinoForm, can_delete=True,
                                         extra=2, )
