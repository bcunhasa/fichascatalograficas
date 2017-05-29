from django import forms

from .models import Ficha

class FichaForm(forms.ModelForm):
    class Meta:
        model = Ficha

        fields = ['nome',
            'sobrenome',
            #'cutter',
            'titulo',
            'sub_titulo',
            'curso',
            'instituicao',
            'cidade',
            'ano',
            'orientador',
            'folhas',
            'referencias',
            'anexos',
            'encardenacao',
            #'coorientador',
            #'figuras',
            'assunto1',
            'assunto2',
            'assunto3',
            'assunto4',
            'assunto5',
            'tipo_trabalho',
            'titulo_obtido',
            'fonte',
            #'tamanho_fonte',
            ]

        labels = {'nome': 'Nome*:',
            'sobrenome': 'Último nome:',
            'cutter': 'Cutter*:',
            'titulo': 'Título*:',
            'sub_titulo': 'Sub-título:',
            'curso': 'Curso*:',
            'instituicao': 'Instituição de ensino*:',
            'cidade': 'Cidade*:',
            'ano': 'Ano*:',
            'orientador': 'Orientador*:',
            'folhas': 'Número de folhas*:',
            'referencias': 'Nº da folha em que começam as referências bibliográficas*:',
            'anexos': 'Nº da folha em que começam as referências bibliográficas*:',
            'encardenacao': 'Tipo de encardenação*:',
            'coorientador': 'Coorientador:',
            'figuras': 'O trabalho possui figuras?',
            'assunto1': 'Assunto 1*:',
            'assunto2': 'Assunto 2:',
            'assunto3': 'Assunto 3:',
            'assunto4': 'Assunto 4:',
            'assunto5': 'Assunto 5:',
            'tipo_trabalho': 'Tipo do trabalho:',
            'titulo_obtido': 'Título obtido:',
            'fonte': 'Fonte:',
            'tamanho_fonte': 'Tamanho da fonte:'
            }
            