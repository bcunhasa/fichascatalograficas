from django import forms

from .models import Ficha

class FichaForm(forms.ModelForm):
    class Meta:
        model = Ficha

        fields = ['nome',
            'sobrenome',
            'cutter',
            'titulo',
            'sub_titulo',
            'curso',
            'ano',
            'orientador',
            'coorientador',
            'tipo_trabalho',
            'fonte',
            'tamanho_fonte']

        labels = {'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'cutter': 'Cutter',
            'titulo': 'Título',
            'sub_titulo': 'Sub-título',
            'curso': 'Curso',
            'ano': 'Ano',
            'orientador': 'Orientador',
            'coorientador': 'Coorientador',
            'tipo_trabalho': 'Tipo do trabalho',
            'fonte': 'Fonte',
            'tamanho_fonte': 'Tamanho da fonte'}
