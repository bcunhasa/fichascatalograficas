from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

from unicodedata import normalize
import csv

from django.db import models

class Ficha(models.Model):
    """A ficha catalográfica padrão que será usada na aplicação"""

    # Opções para os campos de mútipla escolha
    CDU = ()
    with open('fichas/static/csv/cdu.csv', 'r') as arquivo:
        leitor = csv.DictReader(arquivo)
        dicionario = {}
        for linha in leitor:
            dicionario[linha['assunto']] = linha['assunto']
        CDU = sorted(list(dicionario.items()))
    
    FONTE = (
        ('Arial', 'Arial'),
        ('Times', 'Times New Roman'),
    )

    TIPO_TRABALHO = (
        ('Monografia', 'Monografia'),
        ('Dissertação', 'Dissertação'),
        ('Tese', 'Tese'),
    )
    
    TEM_FIGURAS = (
   	    ('Sim', 'Sim'),
   	    ('Nao', 'Não'),
    )
    
    TITULO_OBTIDO = (
        ('Especialista', 'Especialista'),
        ('Bacharel', 'Bacharel'),
        ('Mestre', 'Mestre'),
        ('Doutor', 'Doutor'),
    )
    
    GENERO = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
    )
    
    TITULO_ORIENTADOR = (
        ('Especialista', 'Especialista'),
        ('Mestre', 'Mestre'),
        ('Doutor', 'Doutor'),
    )
    
    ENCARDENACAO = (
        ('Brochura', 'Brochura'),
        ('Espiral', 'Espiral'),
    )
    
    """
    CDD = (
        ('Direito', 'Direito'),
        ('Direito Público', 'Direito Público'),
        ('Direito Internacional Público', 'Direito Internacional Público'),
        ('Direito Penal Internacional', 'Direito Penal Internacional'),
        ('Direito Constitucional', 'Direito Constitucional'),
        ('Direitos Fundamentais', 'Direitos Fundamentais'),
        ('Direito Eleitoral', 'Direito Eleitoral'),
        ('Direito Administrativo', 'Direito Administrativo'),
        ('Direito Ambiental', 'Direito Ambiental'),
        ('Direito Econômico', 'Direito Econômico'),
        ('Direito Financeiro', 'Direito Financeiro'),
        ('Direito Tributário', 'Direito Tributário'),
        ('Direito Processual', 'Direito Processual'),
        ('Direito Processual Penal', 'Direito Processual Penal'),
        ('Direito Processual Civil', 'Direito Processual Civil'),
        ('Direito Penal', 'Direito Penal'),
        ('Direito Penitenciário', 'Direito Penitenciário'),
        ('Direito Previdenciário', 'Direito Previdenciário'),
        ('Direito Militar', 'Direito Militar'),
        ('Direito Penal Militar', 'Direito Penal Militar'),
        ('Direito Aéreo', 'Direito Aéreo'),
        ('Direito Aéreo Militar', 'Direito Aéreo Militar'),
        ('Direito aplicado à Telecomunicação', 'Direito aplicado à Telecomunicação'),
        ('Direito Espacial', 'Direito Espacial'),
        ('Direito Privado', 'Direito Privado'),
        ('Direito Civil', 'Direito Civil'),
        ('Direitos Reais, Coisas e Bens', 'Direitos Reais, Coisas e Bens'),
        ('Direito de Família', 'Direito de Família'),
        ('Direito das Sucessões', 'Direito das Sucessões'),
        ('Direito do Menor', 'Direito do Menor'),
        ('Direito Comercial', 'Direito Comercial'),
        ('Direito Bancário', 'Direito Bancário'),
        ('Direitos Intelectuais', 'Direitos Intelectuais'),
        ('Direito autoral', 'Direito autoral'),
        ('Direito Marítimo', 'Direito Marítimo'),
        ('Direito Aeronáutico', 'Direito Aeronáutico'),
        ('Direito Internacional Privado', 'Direito Internacional Privado'),
        ('Direito do Consumidor', 'Direito do Consumidor'),
        ('Direito do Trabalho', 'Direito do Trabalho'),
        ('Direito Processual do Trabalho', 'Direito Processual do Trabalho'),
    )
    """

    # Modelos usados no projeto
    nome = models.CharField(max_length=300, default='')
    sobrenome = models.CharField(max_length=200, default='')
    cutter = models.CharField(max_length=20, default='')
    titulo = models.CharField(max_length=300, default='')
    sub_titulo = models.CharField(max_length=300, default='', blank=True, null=True)
    curso = models.CharField(max_length=200, default='Direito')
    instituicao = models.CharField(max_length=300, default='Faculdade Serra do Carmo')
    cidade = models.CharField(max_length=100, default='Palmas')
    ano = models.PositiveIntegerField(default=2017)
    folhas = models.PositiveIntegerField(default=1)
    figuras = models.CharField(
    	max_length=20,
    	choices=TEM_FIGURAS,
    	default='Sim'
    )
    referencias = models.PositiveIntegerField(default=1)
    anexos = models.PositiveIntegerField(default=1, blank=True, null=True)
    encardenacao = models.CharField(
        max_length=20,
        choices=ENCARDENACAO,
        default='Brochura'
    )
    orientador = models.CharField(max_length=200, default='')
    genero_orientador = models.CharField(
        max_length=20,
        choices=GENERO,
        default='Masculino',
    )
    titulo_orientador = models.CharField(
        max_length=50,
        choices=TITULO_ORIENTADOR,
        default='Mestre',
    )
    coorientador = models.CharField(max_length=200, default='', blank=True, null=True)
    genero_coorientador = models.CharField(
        max_length=20,
        choices=GENERO,
        default='Masculino',
        blank=True,
        null=True,
    )
    titulo_coorientador = models.CharField(
        max_length=50,
        choices=TITULO_ORIENTADOR,
        default='Mestre',
        blank=True,
        null=True,
    )
    tipo_trabalho = models.CharField(
        max_length=12,
        choices=TIPO_TRABALHO,
        default='Monografia'
    )
    titulo_obtido = models.CharField(
        max_length=15,
        choices=TITULO_OBTIDO,
        default='Bacharelado',
    )
    assunto1 = models.CharField(
        max_length=100,
        default='Direito',
        choices=CDU,
    )
    assunto2 = models.CharField(
        max_length=100,
        default='',
        blank=True,
        choices=CDU,
        null=True
    )
    assunto3 = models.CharField(
        max_length=100,
        default='',
        blank=True,
        choices=CDU,
        null=True
    )
    assunto4 = models.CharField(
        max_length=100,
        default='',
        blank=True,
        choices=CDU,
        null=True
    )
    assunto5 = models.CharField(
        max_length=100,
        default='',
        blank=True,
        choices=CDU,
        null=True
    )
    fonte = models.CharField(
        max_length=15,
        choices=FONTE,
        default='Times',
    )
    tamanho_fonte = models.PositiveIntegerField(validators=[
        MaxValueValidator(14), MinValueValidator(9)], default=11)

    def __str__(self):
        """Devolve um das varíaveis como representação do modelo"""
        return self.titulo
