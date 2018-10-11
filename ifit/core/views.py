from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from django.contrib import messages
from .models import *
from .forms import TreinoForm, ExercicioTreinoForm, FormAvaliacao



class Index(TemplateView):
    template_name = 'index.html'


class ClienteList(ListView):
    model = Cliente


class ClienteCreate(CreateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('core:cliente-list')


class ClienteUpdate(UpdateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('core:cliente-list')


class TreinoList(ListView):
    model = Treino
    fields = '__all__'


class TreinoCreate(CreateView):
    model = Treino
    form_class = TreinoForm

    def get_success_url(self):
        return reverse_lazy('core:treino-update', kwargs={'pk': self.object.pk})


class TreinoUpdate(UpdateView):
    model = Treino
    form_class = TreinoForm

    def get_context_data(self, **kwargs):
        context = super(TreinoUpdate, self).get_context_data(**kwargs)
        context['treino_id'] = self.object.pk
        context['exercicio'] = ExercicioTreinoForm(self.request.POST or None)
        context['exercicios'] = ExercicioTreino.objects.filter(treino_id=self.object.pk).order_by('dia')

        return context

    def get_success_url(self):
        return reverse_lazy('core:treino-update', kwargs={'pk': self.object.pk})


class ExercicioCreate(CreateView):
    model = ExercicioTreino
    form_class = ExercicioTreinoForm
    template_name = 'core/treino_form.html'

    def get_success_url(self):
        return reverse_lazy('core:treino-update', kwargs={'pk': self.object.treino.pk})


class AvaliacaoList(ListView):
    model = Avaliacao


class AvaliacaoCreate(CreateView):
    model = Avaliacao
    form_class = FormAvaliacao
    template_name = 'core/avaliacao_form.html'

    def get_success_url(self):
        messages.success(self.request, 'Ficha Criada com sucesso')
        return reverse_lazy('core:ficha-list')


class AvaliacaoUpdate(UpdateView):
    model = Avaliacao
    form_class = FormAvaliacao
    template_name = 'core/avaliacao_form.html'

    def get_success_url(self):
        messages.success(self.request, 'Ficha Atualizada')
        return reverse_lazy('core:ficha-list')

    template_name = 'core/avaliacao_form.html'
    success_url = reverse_lazy('core:ficha-list')


