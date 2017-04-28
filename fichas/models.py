from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models

class Ficha(models.Model):
    """A ficha catalográfica padrão que será usada na aplicação"""

    # Opções para os campos de mútipla escolha
    FONTE = (
        ('Arial', 'Arial'),
        ('Times', 'Times New Roman'),
        ('Monospace', 'Monoespaçada'),
    )

    TIPO_TRABALHO = (
        ('Monografia', 'Monografia'),
        ('Dissertação', 'Dissertação'),
        ('Tese', 'Tese'),
    )

    # Modelos usados no projeto
    nome = models.CharField(max_length=50, default='')
    sobrenome = models.CharField(max_length=200, default='')
    cutter = models.CharField(max_length=10, default='')
    titulo = models.CharField(max_length=200, default='')
    sub_titulo = models.CharField(max_length=200, default='')
    curso = models.CharField(max_length=200, default='')
    ano = models.PositiveIntegerField(default=2017)
    orientador = models.CharField(max_length=200, default='')
    coorientador = models.CharField(max_length=200, default='', blank=True,
        null=True)
    tipo_trabalho = models.CharField(
        max_length=12,
        choices=TIPO_TRABALHO,
        default='Monografia'
    )
    fonte = models.CharField(
        max_length=15,
        choices=FONTE,
        default='Arial',
    )
    tamanho_fonte = models.PositiveIntegerField(validators=[
        MaxValueValidator(42), MinValueValidator(4)], default=12)

    def __str__(self):
        """Devolve um das varíaveis como representação do modelo"""
        return self.titulo
