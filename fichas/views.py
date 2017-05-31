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

from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.rl_config import defaultPageSize

from unicodedata import normalize
import csv

from .models import Ficha
from .forms import FichaForm

largura_pagina = defaultPageSize[0]
altura_pagina = defaultPageSize[1]

linhas = []
topo_res = 12
passada_vert = 0.45

esquerda = 6
recuo = 0

assuntos = []

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

            request = salvaInformacoes(request, nova_ficha)

            return HttpResponseRedirect(reverse('fichas:ficha'))

    context = {'form': form}
    return render(request, 'fichas/index.html', context)

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
    request.session['figuras'] = nova_ficha.figuras
    request.session['encardenacao'] = nova_ficha.encardenacao
    
    request.session['orientador'] = nova_ficha.orientador
    request.session['coorientador'] = nova_ficha.coorientador
    
    request.session['referencias'] = nova_ficha.referencias
    request.session['anexos'] = nova_ficha.anexos

    request.session['assunto1'] = nova_ficha.assunto1
    request.session['assunto2'] = nova_ficha.assunto2
    request.session['assunto3'] = nova_ficha.assunto3
    request.session['assunto4'] = nova_ficha.assunto4
    request.session['assunto5'] = nova_ficha.assunto5

    request.session['tipo_trabalho'] = nova_ficha.tipo_trabalho
    request.session['titulo_obtido'] = nova_ficha.titulo_obtido
    request.session['fonte'] = nova_ficha.fonte
    if nova_ficha.fonte == 'Arial':
        request.session['tamanho_fonte'] = 10
    else:
        request.session['tamanho_fonte'] = 11
    
    return request

def ficha(request):
    """Página onde o documento em pdf é gerado"""
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='inline; filename="ficha-catalográfica.pdf"'

    draw_canvas = canvas.Canvas(response)

    draw_canvas = defineFonte(request, draw_canvas)
    draw_canvas = desenhaRetangulo(request, draw_canvas)
    draw_canvas = criaFicha(request, draw_canvas)
    
    draw_canvas.showPage()
    draw_canvas.save()
    return response

def defineFonte(request, draw_canvas):
    """Define a fonte da ficha"""
    # monospace_font = "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf"
    arial_font = "/usr/share/fonts/truetype/msttcorefonts/arial.ttf"
    arial_bold_font = "/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf"
    times_font = "/usr/share/fonts/truetype/msttcorefonts/Times_New_Roman.ttf"
    times_bold_font = "/usr/share/fonts/truetype/msttcorefonts/Times_New_Roman_Bold.ttf"

    # pdfmetrics.registerFont(TTFont('Monospace', monospace_font))
    pdfmetrics.registerFont(TTFont('Arial', arial_font))
    pdfmetrics.registerFont(TTFont('Arial_Bold', arial_bold_font))
    pdfmetrics.registerFont(TTFont('Times', times_font))
    pdfmetrics.registerFont(TTFont('Times_Bold', times_bold_font))

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
    draw_canvas.setLineWidth(0.1)
    #draw_canvas.setStrokeColor((158, 158, 158))
    draw_canvas.rect(4*cm, 5.5*cm, 13.5*cm, 7.5*cm, stroke=1, fill=False)
    return draw_canvas

def criaFicha(request, draw_canvas):
    """Realiza os passos necessários para construir a ficha catalográfica"""
    linhas.clear()
    
    # Pré-processamento das informações
    nome = processaNome(request)
    pista = processaPista(request)
    cutter = processaCutter(request)
    titulo = processaTitulo(request)
    trabalho = processaTrabalho(request)
    
    # Processamento das informações
    linhas.append(nome)
    linhas.append(titulo)
    linhas.append(trabalho)
    linhas.append("Orientação: Prof(a). " + request.session['orientador'] + ".")
    linhas.append(request.session['tipo_trabalho'] + " (" + request.session['titulo_obtido'] + ") - " + request.session['instituicao'] + ", curso de " + request.session['curso'] + ".")
    linhas.append("Referências bibliográficas: f." + str(request.session['referencias']))
    linhas.append("Anexos: f." + str(request.session['anexos']))
    linhas.append(pista)
    
    # Impressão das informações na ficha
    draw_canvas = escreveCabecalho(draw_canvas, request)
    draw_canvas = escreveRodape(draw_canvas, request)
    draw_canvas = escreveCutter(draw_canvas, cutter)
    draw_canvas = escreveCdd(draw_canvas)
    
    global topo_res
    topo_res = 12.3
    
    for i in range(0, len(linhas)):
        draw_canvas = escreveInformacoes(draw_canvas, selecionaBloco(i, request), i)
        
    topo_res = 12
    
    return draw_canvas
    
def processaNome(request):
    """Arruma o bloco de nome antes de imprimir na ficha"""
    nome = request.session['sobrenome'] + ", " + request.session['nome']
    
    global recuo
    recuo = stringWidth(nome[:4], request.session['fonte'], request.session['tamanho_fonte'])/cm
    
    return nome

def processaPista(request):
    """Arruma o bloco de assuntos antes de imprimir na ficha"""
    pista = ""
    for i in range(1, 6):
        if request.session['assunto' + str(i)] is None:
            break
        pista += str(i) + ". " + request.session['assunto' + str(i)] + ". "
    pista += "I. Título."
    return pista
    
def processaCutter(request):
    """Cria o dicionário com os valores do arquivo cutter.csv"""
    nome = request.session['sobrenome']
    
    with open('fichas/static/csv/cutter.csv', 'r') as arquivo:
        leitor = csv.DictReader(arquivo)
        dicionario = {}
        for linha in leitor:
            dicionario[removeAcentuacao(linha['texto']).lower()] = linha['codigo']
        lista = list(dicionario.items())
        lista = sorted(lista, key=lambda x: x[0])
    cutter = selecionaCutter(removeAcentuacao(nome).lower(), lista, 0)
    return nome[0].title() + str(cutter) + request.session['titulo'][0].lower()
    
def selecionaCutter(nome, lista, i):
    """Função recursiva que seleciona o par chave - valor correto"""
    nova_lista = []
    
    for tupla in lista:
        if i >= len(nome):
            return int(lista[0][1])
            
        if i >= len(tupla[0]):
            continue
            
        if nome[i] == tupla[0][i]:
            nova_lista.append(tupla)
    
    if nova_lista:
        return selecionaCutter(nome, nova_lista, i + 1)
    else:
        return lista[0][1]

def removeAcentuacao(texto):
    """Remove a acentuação do texto"""
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
    
def processaTitulo(request):
    """Arruma o bloco de titulo antes de imprimir na ficha"""
    titulo = ""
    if request.session['sub_titulo'] is None:
        titulo = request.session['titulo'] + " / " + request.session['nome'] + " " + request.session['sobrenome'] + ". - " + str(request.session['ano']) + "."
    else:
        titulo = request.session['titulo'] + ": " + request.session['sub_titulo'] + " / " + request.session['nome'] + " " + request.session['sobrenome'] + ". " + request.session['cidade'] +" - TO, " + str(request.session['ano']) + "."
    return titulo

def processaTrabalho(request):
    """Define se existe ou não figuras antes de imprimir na ficha"""
    figuras = str(request.session['folhas']) + "f."
    if request.session['figuras'] == 'Sim':
        figuras += " il. "
    figuras += 'enc.' + request.session['encardenacao'].lower() + '. capa dura'
    return figuras

def selecionaBloco(index, request):
    """Seleciona o bloco de linhas correspondente"""
    linha = linhas[index]
    bloco = []
    para_prox_linha = ""
    linha_formatada = ""
    
    for i in range(0, len(linha)):
        linha_formatada += para_prox_linha
        para_prox_linha = ""
        linha_formatada += linha[i]
        largura = stringWidth(linha_formatada, request.session['fonte'], request.session['tamanho_fonte'])/cm
        if (largura >= 10.2):
            for j in range(len(linha_formatada) - 1, 0, -1):
                if linha_formatada[j] != ' ':
                    para_prox_linha = linha_formatada[j] + para_prox_linha
                    linha_formatada = linha_formatada[:-1]
                else:
                    break
            bloco.append(linha_formatada)
            linha_formatada = ""
    
    if linha_formatada is not None:
        bloco.append(linha_formatada)
    
    return bloco
    
def escreveCabecalho(draw_canvas, request):
    """Escreve o cabeçalho da ficha"""
    draw_canvas.setFont(request.session['fonte'] + '_Bold', request.session['tamanho_fonte'])
    cabecalho1 = "Dados de Catalogação na publicação (CIP) Internacional"
    cabecalho2 = "(Seção de processamento técnico da Biblioteca Serra do Carmo)"
    largura1 = stringWidth(cabecalho1, request.session['fonte'], request.session['tamanho_fonte'])
    largura2 = stringWidth(cabecalho2, request.session['fonte'], request.session['tamanho_fonte'])
    draw_canvas.drawString((largura_pagina - largura1)/2, (topo_res + 2)*cm, cabecalho1)
    draw_canvas.drawString((largura_pagina - largura2)/2, (topo_res + 1.5)*cm, cabecalho2)
    draw_canvas.setFont(request.session['fonte'], request.session['tamanho_fonte'])
    return draw_canvas
    
def escreveRodape(draw_canvas, request):
    """Escreve o rodapé da ficha"""
    global assuntos
    reducao = 7.2
    passo = 0.5
    
    rodape = "Índices para catalógo sistemático:"
    draw_canvas.drawString((esquerda - 1.5)*cm, (topo_res - reducao)*cm, rodape)
    assuntos = retornaAssuntos(request)
    reducao += passo
    
    i = 1
    for assunto in assuntos:
        texto = str(i) + '. ' + assunto[1] + ' ' + assunto[0]
        draw_canvas.drawString((esquerda - 1.5)*cm, (topo_res - (reducao + passo))*cm, texto)
        i += 1
        passo += 0.5
    return draw_canvas
    
def retornaAssuntos(request):
    """Retorna os assuntos e códigos correspondentes armazeandos no .csv"""
    assuntos = []
    with open('fichas/static/csv/cdd.csv', 'r') as arquivo:
        leitor = csv.DictReader(arquivo)
        dicionario = {}
        for linha in leitor:
            dicionario[linha['cdd']] = linha['assunto']
        assuntos = list(dicionario.items())
        assuntos = sorted(assuntos, key=lambda x: x[0])
    
    lista = []
    i = 1
    while i < 6:
        for assunto in assuntos:
            a = request.session['assunto' + str(i)]
            if a is not None and assunto[1] == a:
                lista.append(assunto)
                break
        i += 1
    
    return lista
    
def escreveCutter(draw_canvas, cutter):
    """Escreve o cutter gerado"""
    global esquerda
    margem = esquerda - 1.5
    draw_canvas.drawString(margem*cm, (12.3 - passada_vert)*cm, cutter)
    return draw_canvas
    
def escreveCdd(draw_canvas):
    """Escreve o cdd correspondente ao assunto principal"""
    draw_canvas.drawString((esquerda + 8.5)*cm, (topo_res - 6)*cm, 'CDD - ' + assuntos[0][0])
    return draw_canvas

def escreveInformacoes(draw_canvas, bloco, index):
    """Escreve as informações passadas pelo usuário"""
    global esquerda
    global topo_res
    topo = topo_res
    margem = adicionaMargem(index, esquerda)
    
    for i in range(0, len(bloco)):
        draw_canvas.drawString(margem*cm, topo*cm, bloco[i])
        margem = 6
        topo -= passada_vert
    topo_res = topo
    adicionaNovaLinha(index, topo)

    return draw_canvas

def adicionaMargem(i, margem):
    """Adiciona a margem se necessário"""
    if i != 0:
        margem += recuo
    return margem

def adicionaNovaLinha(i, topo):
    """Adiciona uma nova linha se necessário"""
    global topo_res
    if i == 1 or i == 2 or i == 4 or i == 6:
        topo -= 0.3
    topo_res = topo
