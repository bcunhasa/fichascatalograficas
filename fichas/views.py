from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.lib.styles import ParagraphStyle

from .models import Ficha
from .forms import FichaForm

def index(request):
    """A página inicial do app Fichas Catalográficas"""
    if request.method == 'GET':
        # Requisição GET: abre formulário em branco
        form = FichaForm()
    else:
        # Requisição POST: Dados do formulário são processados
        form = FichaForm(request.POST)
        if form.is_valid():
            nova_ficha = form.save(commit=False)
            request.session['nome'] = nova_ficha.nome
            request.session['sobrenome'] = nova_ficha.sobrenome
            request.session['cutter'] = nova_ficha.cutter
            request.session['titulo'] = nova_ficha.titulo
            request.session['sub_titulo'] = nova_ficha.sub_titulo
            request.session['curso'] = nova_ficha.curso
            request.session['ano'] = nova_ficha.ano
            request.session['orientador'] = nova_ficha.orientador
            request.session['coorientador'] = nova_ficha.coorientador
            request.session['tipo_trabalho'] = nova_ficha.tipo_trabalho
            request.session['fonte'] = nova_ficha.fonte
            request.session['tamanho_fonte'] = nova_ficha.tamanho_fonte
            return HttpResponseRedirect(reverse('fichas:ficha'))

    context = {'form': form}
    return render(request, 'fichas/index.html', context)

def ficha(request):
    """Página onde o documento em pdf é gerado"""
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='inline; filename="Ficha Catalográfica.pdf"'
    draw_canvas = canvas.Canvas(response)

    draw_canvas = defineFonte(request, draw_canvas)
    draw_canvas = desenhaRetangulo(request, draw_canvas)
    draw_canvas = escreveInformacoes(request, draw_canvas)

    draw_canvas.showPage()
    draw_canvas.save()
    return response

def defineFonte(request, draw_canvas):
    """Define a fonte da ficha"""
    pdfmetrics.registerFont(TTFont('Monospace', 'Monospace.ttf'))
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
    pdfmetrics.registerFont(TTFont('Times', 'times.ttf'))
    draw_canvas.setFont(request.session['fonte'],
        request.session['tamanho_fonte'])
    return draw_canvas

def desenhaRetangulo(request, draw_canvas):
    """Desenha o retângulo padrão de ficha catalográfica"""
    draw_canvas.rect(4*cm, 3*cm, 12.5*cm, 7.5*cm, fill=False)
    return draw_canvas

def escreveInformacoes(request, draw_canvas):
    """Escre as informações passadas pelo usuário por meio do formulário"""

    draw_canvas.drawString(4.5*cm, 9*cm, request.session['sobrenome'] + ", " +
        request.session['nome'])

    draw_canvas.drawString(4.5*cm, 8.5*cm, "d" + request.session['cutter'] +
        "t    " + request.session['titulo'] + " / " + request.session['nome'] +
        " " + request.session['sobrenome'] + "; " + " orientador " +
        request.session['orientador'] + " co-orientador " +
        request.session['coorientador'] + ". -- Palmas. " +
        str(request.session['ano']) + ". 34p.")

    draw_canvas.drawString(4.5*cm, 8*cm, request.session['tipo_trabalho'] +
        " (" + request.session['curso'] + ") -- " +
        "Faculdade Serra do Carmo, " + str(request.session['ano']) + ".")

    draw_canvas.drawString(4.5*cm, 7.5*cm, request.session['curso'])
    draw_canvas.drawString(4.5*cm, 7*cm, str(request.session['ano']))
    draw_canvas.drawString(4.5*cm, 6.5*cm, request.session['orientador'])
    draw_canvas.drawString(4.5*cm, 6*cm, request.session['coorientador'])
    draw_canvas.drawString(4.5*cm, 5.5*cm, request.session['tipo_trabalho'])

    return draw_canvas
