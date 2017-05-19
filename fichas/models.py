from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models

class Ficha(models.Model):
    """A ficha catalográfica padrão que será usada na aplicação"""

    # Opções para os campos de mútipla escolha
    FONTE = (
        ('Arial', 'Arial'),
        ('Times', 'Times New Roman'),
<<<<<<< HEAD
        #('Monospace', 'Monoespaçada'),
=======
        ('Monospace', 'Monoespaçada'),
>>>>>>> 588ebd80e15dd4246742cd026d53a3ee5e2d4e39
    )

    TIPO_TRABALHO = (
        ('Monografia', 'Monografia'),
        ('Dissertação', 'Dissertação'),
        ('Tese', 'Tese'),
    )
    
    TEM_FIGURAS = (
<<<<<<< HEAD
   	    ('Sim', 'Sim'),
   	    ('Nao', 'Não'),
    )
    
    TITULO_OBTIDO = (
        ('Bacharelado', 'Bacharelado'),
        ('Mestrado', 'Mestrado'),
        ('Doutorado', 'Doutorado'),
=======
   	('Sim', 'Sim'),
   	('Nao', 'Não'),
>>>>>>> 588ebd80e15dd4246742cd026d53a3ee5e2d4e39
    )

    # Modelos usados no projeto
    nome = models.CharField(max_length=50, default='')
    sobrenome = models.CharField(max_length=200, default='')
    cutter = models.CharField(max_length=10, default='')
    titulo = models.CharField(max_length=200, default='')
<<<<<<< HEAD
    sub_titulo = models.CharField(max_length=200, default='', blank=True, null=True)
    curso = models.CharField(max_length=200, default='')
    instituicao = models.CharField(max_length=200, default='Faculdade Serra do Carmo')
    cidade = models.CharField(max_length=100, default='Palmas')
=======
    sub_titulo = models.CharField(max_length=200, default='')
    curso = models.CharField(max_length=200, default='')
>>>>>>> 588ebd80e15dd4246742cd026d53a3ee5e2d4e39
    ano = models.PositiveIntegerField(default=2017)
    folhas = models.PositiveIntegerField(default=1)
    figuras = models.CharField(
    	max_length=20,
    	choices=TEM_FIGURAS,
    	default='Sim'
    )
    orientador = models.CharField(max_length=200, default='')
    coorientador = models.CharField(max_length=200, default='', blank=True,
        null=True)
    tipo_trabalho = models.CharField(
        max_length=12,
        choices=TIPO_TRABALHO,
        default='Monografia'
    )
<<<<<<< HEAD
    titulo_obtido = models.CharField(
        max_length=15,
        choices=TITULO_OBTIDO,
        default='Bacharelado',
    )
    assunto1 = models.CharField(max_length=25, default='', blank=True, null=True)
    assunto2 = models.CharField(max_length=25, default='', blank=True, null=True)
    assunto3 = models.CharField(max_length=25, default='', blank=True, null=True)
    assunto4 = models.CharField(max_length=25, default='', blank=True, null=True)
    assunto5 = models.CharField(max_length=25, default='', blank=True, null=True)
    fonte = models.CharField(
        max_length=15,
        choices=FONTE,
        default='Times',
    )
    tamanho_fonte = models.PositiveIntegerField(validators=[
        MaxValueValidator(42), MinValueValidator(4)], default=11)
=======
    assunto1 = models.CharField(max_length=20, default='')
    assunto2 = models.CharField(max_length=20, default='')
    assunto3 = models.CharField(max_length=20, default='')
    assunto4 = models.CharField(max_length=20, default='')
    assunto5 = models.CharField(max_length=20, default='')
    fonte = models.CharField(
        max_length=15,
        choices=FONTE,
        default='Arial',
    )
    tamanho_fonte = models.PositiveIntegerField(validators=[
        MaxValueValidator(42), MinValueValidator(4)], default=12)
>>>>>>> 588ebd80e15dd4246742cd026d53a3ee5e2d4e39

    def __str__(self):
        """Devolve um das varíaveis como representação do modelo"""
        return self.titulo
