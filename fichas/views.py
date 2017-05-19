from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.conf.urls.static import static
from django.conf import settings

from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.lib.styles import ParagraphStyle

from .models import Ficha
from .forms import FichaForm

<<<<<<< HEAD
linhas = []
topo_res = 9.5
passada_vert = 0.5

=======
>>>>>>> 588ebd80e15dd4246742cd026d53a3ee5e2d4e39
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
<<<<<<< HEAD

            request = salvaInformacoes(request, nova_ficha)

=======
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
>>>>>>> 588ebd80e15dd4246742cd026d53a3ee5e2d4e39
            return HttpResponseRedirect(reverse('fichas:ficha'))

    context = {'form': form}
    return render(request, 'fichas/index.html', context)

<<<<<<< HEAD
def salvaInformacoes(request, nova_ficha):
    """Salva as informações do formulário para serem impressas na ficha"""
    request.session['nome'] = nova_ficha.nome
    request.session['sobrenome'] = nova_ficha.sobrenome
    request.session['cutter'] = nova_ficha.cutter
    request.session['titulo'] = nova_ficha.titulo
    request.session['sub_titulo'] = nova_ficha.sub_titulo
    request.session['curso'] = nova_ficha.curso
    request.session['instituicao'] = nova_ficha.instituicao
    request.session['cidade'] = nova_ficha.cidade
    request.session['ano'] = nova_ficha.ano
    request.session['folhas'] = nova_ficha.folhas
    request.session['orientador'] = nova_ficha.orientador
    request.session['coorientador'] = nova_ficha.coorientador
    request.session['figuras'] = nova_ficha.figuras

    request.session['assunto1'] = nova_ficha.assunto1
    request.session['assunto2'] = nova_ficha.assunto2
    request.session['assunto3'] = nova_ficha.assunto3
    request.session['assunto4'] = nova_ficha.assunto4
    request.session['assunto5'] = nova_ficha.assunto5

    request.session['tipo_trabalho'] = nova_ficha.tipo_trabalho
    request.session['titulo_obtido'] = nova_ficha.titulo_obtido
    request.session['fonte'] = nova_ficha.fonte
    request.session['tamanho_fonte'] = nova_ficha.tamanho_fonte
    
    return request

def ficha(request):
    """Página onde o documento em pdf é gerado"""
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='inline; filename="ficha-catalográfica.pdf"'
=======
def ficha(request):
    """Página onde o documento em pdf é gerado"""
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='inline; filename="Ficha Catalográfica.pdf"'
>>>>>>> 588ebd80e15dd4246742cd026d53a3ee5e2d4e39
    draw_canvas = canvas.Canvas(response)

    draw_canvas = defineFonte(request, draw_canvas)
    draw_canvas = desenhaRetangulo(request, draw_canvas)
<<<<<<< HEAD
    draw_canvas = criaFicha(request, draw_canvas)
=======
    draw_canvas = escreveInformacoes(request, draw_canvas)
>>>>>>> 588ebd80e15dd4246742cd026d53a3ee5e2d4e39

    draw_canvas.showPage()
    draw_canvas.save()
    return response

def defineFonte(request, draw_canvas):
    """Define a fonte da ficha"""
    monospace_font = "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf"
    arial_font = "/usr/share/fonts/truetype/msttcorefonts/arial.ttf"
    times_font = "/usr/share/fonts/truetype/msttcorefonts/Times_New_Roman.ttf"

    pdfmetrics.registerFont(TTFont('Monospace', monospace_font))
    pdfmetrics.registerFont(TTFont('Arial', arial_font))
    pdfmetrics.registerFont(TTFont('Times', times_font))

    draw_canvas.setFont(request.session['fonte'], request.session['tamanho_fonte'])

    #if request.session['fonte'] == 'Times':
    #    draw_canvas.setFont('Times-Roman', request.session['tamanho_fonte'])
    #elif request.session['fonte'] == 'Arial':
    #    draw_canvas.setFont('arial', request.session['tamanho_fonte'])
    #else:
    #    draw_canvas.setFont('Monospace', request.session['tamanho_fonte'])
    return draw_canvas

def desenhaRetangulo(request, draw_canvas):
    """Desenha o retângulo padrão de ficha catalográfica"""
<<<<<<< HEAD
    draw_canvas.setLineWidth(0.1)
    #draw_canvas.setStrokeColor((158, 158, 158))
    draw_canvas.rect(4*cm, 3*cm, 12.5*cm, 7.5*cm, stroke=1, fill=False)
    return draw_canvas

def criaFicha(request, draw_canvas):
    """Realiza os passos necessários para construir a ficha catalográfica"""
    linhas.clear()
    
    # Pré-processamento das informações
    pista = processaPista(request)
    cutter = processaCutter(request)
    titulo = processaTitulo(request)
    figuras = processaFiguras(request)
    
    # Processamento das informações
    linhas.append(request.session['sobrenome'] + ", " + request.session['nome'])
    linhas.append(titulo)
    linhas.append(figuras)
    linhas.append(request.session['tipo_trabalho'] + " (" + request.session['titulo_obtido'] + " em " + request.session['curso'] + ") - " + request.session['instituicao'] + ", " + request.session['cidade'] + ", " + str(request.session['ano']) + ".")
    linhas.append("Orientação: " + request.session['orientador'] + ".")
    linhas.append(pista)
    
    # Impressão das informações na ficha
    draw_canvas = escreveCutter(draw_canvas, cutter)
    
    for i in range(0, 6):
        draw_canvas = escreveInformacoes(draw_canvas, selecionaBloco(i), i)
        
    global topo_res
    topo_res = 9.5
    
    return draw_canvas

def processaPista(request):
    """Arruma o bloco de assuntos antes de imprimir na ficha"""
    pista = ""
    for i in range(1, 7):
        if request.session['assunto' + str(i)] is None:
            break
        pista += str(i) + ". " + request.session['assunto' + str(i)] + ". "
    pista += "I. Título."
    return pista
    
def processaCutter(request):
    """Arruma o cutter antes de imprimir na ficha"""
    cutter = request.session['sobrenome'][0] + request.session['cutter'] + request.session['titulo'][0].lower()
    return cutter
    
def processaTitulo(request):
    """Arruma o bloco de titulo antes de imprimir na ficha"""
    titulo = ""
    if request.session['sub_titulo'] is None:
        titulo = request.session['titulo'] + " / " + request.session['nome'] + " " + request.session['sobrenome'] + ". - " + str(request.session['ano']) + "."
    else:
        titulo = request.session['titulo'] + ": " + request.session['sub_titulo'] + " / " + request.session['nome'] + " " + request.session['sobrenome'] + ". - " + str(request.session['ano']) + "."
    return titulo

def processaFiguras(request):
    """Define se existe ou não figuras antes de imprimir na ficha"""
    figuras = str(request.session['folhas']) + "f."
    if request.session['figuras'] == 'Sim':
        figuras += " : il."
    return figuras

def selecionaBloco(index):
    """Seleciona o bloco de linhas correspondente"""
    linha = linhas[index]
    bloco = []
    linha_formatada = ""
    
    for i in range(0, len(linha)):
        linha_formatada += linha[i]
        if (i % 50 == 0 and i != 0) or i == len(linha) - 1:
            if linha[i].isalpha() and i != len(linha) - 1:
                linha_formatada += '-'
            bloco.append(linha_formatada)
            linha_formatada = ""
    
    return bloco
    
def escreveCutter(draw_canvas, cutter):
    """Escreve o cutter gerado"""
    esquerda = 4.5
    draw_canvas.drawString(esquerda*cm, (topo_res - passada_vert)*cm, cutter)
    return draw_canvas

def escreveInformacoes(draw_canvas, bloco, index):
    """Escreve as informações passadas pelo usuário"""
    global topo_res
    esquerda = 6
    topo = topo_res
    esquerda = adicionaMargem(index, esquerda)
    
    for i in range(0, len(bloco)):
        draw_canvas.drawString(esquerda*cm, topo*cm, bloco[i])
        esquerda = 6
        topo -= passada_vert
    topo_res = topo
    adicionaNovaLinha(index, topo)

    return draw_canvas

def adicionaMargem(i, esquerda):
    """Adiciona a margem se necessário"""
    if i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
        esquerda += 0.8
    return esquerda

def adicionaNovaLinha(i, topo):
    """Adiciona uma nova linha se necessário"""
    global topo_res
    if i == 2 or i == 4:
        topo -= 0.5
    topo_res = topo
=======
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
>>>>>>> 588ebd80e15dd4246742cd026d53a3ee5e2d4e39
