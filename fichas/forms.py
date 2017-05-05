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
            'folhas',
            'orientador',
            'coorientador',
            'figuras',
            'assunto1',
            'assunto2',
            'assunto3',
            'assunto4',
            'assunto5',
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
            'folhas': 'Número de folhas',
            'orientador': 'Orientador',
            'coorientador': 'Coorientador',
            'figuras': 'O trabalho possui figuras?',
            'assunto1': 'Assunto 1',
            'assunto2': 'Assunto 2',
            'assunto3': 'Assunto 3',
            'assunto4': 'Assunto 4',
            'assunto5': 'Assunto 5',
            'tipo_trabalho': 'Tipo do trabalho',
            'fonte': 'Fonte',
            'tamanho_fonte': 'Tamanho da fonte'}
