# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------

'''

    Nome: Vítor Garcia Comissoli
    NUSP: 11810411

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''
import random
import numpy as np
from numpymagem import NumPymagem
from numpymutil import mostre_video
from numpymutil import salve_video

# Escreva aqui outras constantes que desejar
ALTURA  = 120
LARGURA = 160
BLACK = 0
WHITE = 250

#-------------------------------------------------------------------------- 

def main():
    ''' (None) -> None
    Escreva o seu programa que cria o vídeo como descrito no enunciado.
    
    O código abaixo serve para ilustrar como usar a função mostre_video()
    que recebe uma lista com NumPymagens e as mostra em um vídeo na tela
    do seu computador usando PyGame. Por isso lembre-se de seguir as 
    instruções para instalar PyGame no seu computador.

    Remova ou altere o código para gerar o seu próprio vídeo. Não se esqueça
    de criar funções para facilitar o entendimento do seu vídeo.

    Você pode (mas não precisa!) salvar o seu vídeo em um formato mp4, para
    mostrar sua obra no fórum da disciplina. Para isso, antes de salvar, 
    você deve instalar o software ffmpeg que você pode baixar de 
    https://ffmpeg.org/download.html. 
    '''
    #-----------------------------------------------------------------------
    # CRIE A SEGUIR O SEU VÍDEO
    
    video = []
    preto = NumPymagem(ALTURA, LARGURA, BLACK)    
    branco = NumPymagem(ALTURA, LARGURA, WHITE)
    print(f"Está compatível com numpymutil: {type(preto.data) is np.ndarray}")
    cor = BLACK

    circ(WHITE, BLACK, video) # 200
     
    to_white(cor, video) # 60
        
    circ(BLACK, WHITE, video) # 200
    
    to_black(cor, video) # 60
    
    retangulos(WHITE, BLACK, video) # 150
    
    to_white(cor, video) # 60
    
    retangulos(BLACK, WHITE, video) # 150
    
    to_black(cor, video) # 60
    
    #-----------------------------------------------------------------------        
    # A CRIAÇÃO DO SEU VÏDEO TERMINA AQUI
        
    #------------------------------------------------------------------
    # selecione `True` ou `False` para as variáveis `mostre` e `salve`
    # para mostrar o vídeo mostre deve ser True, em caso contrário False    
    mostre = True # DEVE SER True no momento da entrega do EP
    # para gravar o vídeo salve deve ser True, em caso contrário False
    salve = False 

    #------------------------------------------------------------------
    # deste ponto em diante, nada deve ser alterado
    if mostre:
        mostre_video(video)
        
    if salve:
        print("Salvando vídeo")
        salve_video(video)

#-------------------------------------------------------------------------- 
#
# ESCREVA OUTRAS FUNÇÕES E CLASSES QUE DESEJAR
#
#-------------------------------------------------------------------------- 

def to_black(cor, video):
    for i in range(60): # volta para preto
        cor = (cor-3)%WHITE
        cinza = NumPymagem(ALTURA, LARGURA, cor)
        video.append(cinza)
    
def to_white(cor, video):
    for i in range(60): # muda fundo para branco, gradualmente
        cor = (cor+3)%WHITE
        cinza = NumPymagem(ALTURA, LARGURA, cor)
        video.append(cinza)
    

def circ(cor_bola, cor_fundo, video):
    
    no_imagens = 900
    
    # Parte de Discos:
    cor_disco = cor_bola
    
    raio_disco = 10
    diametro_disco = 2 * raio_disco
    
    lin_disco = ALTURA // 2
    col_disco = LARGURA // 2
    
    passo = 1.5 * (LARGURA-diametro_disco) / no_imagens

    # 4 Discos:
    
    lin_disco1 = lin_disco
    lin_disco2 = lin_disco
    lin_disco3 = lin_disco
    lin_disco4 = lin_disco

    col_disco1 = col_disco
    col_disco2 = col_disco
    col_disco3 = col_disco
    col_disco4 = col_disco

    for i in range(200):
        img = NumPymagem(ALTURA, LARGURA, cor_fundo)
        
        for j in range (3):
            col_disco1 += int(i*passo)
            lin_disco1 += int(i*passo)
        
            col_disco2 -= int(i*passo)
            lin_disco2 -= int(i*passo)
        
            col_disco3 += int(i*passo)
            lin_disco3 -= int(i*passo)
        
            col_disco4 -= int(i*passo)
            lin_disco4 += int(i*passo)
        
            img.pinte_disco(cor_disco, raio_disco, lin_disco, col_disco)
            img.pinte_disco(cor_disco, raio_disco, lin_disco1, col_disco1)
            img.pinte_disco(cor_disco, raio_disco, lin_disco2, col_disco2)
            img.pinte_disco(cor_disco, raio_disco, lin_disco3, col_disco3)
            img.pinte_disco(cor_disco, raio_disco, lin_disco4, col_disco4)
            
        lin_disco1 = lin_disco
        lin_disco2 = lin_disco
        lin_disco3 = lin_disco
        lin_disco4 = lin_disco

        col_disco1 = col_disco
        col_disco2 = col_disco
        col_disco3 = col_disco
        col_disco4 = col_disco
            
        video.append(img)

def retangulos(cor_ret, cor_fundo, video):
    
    no_imagens = 130
    
    altura = 120
    largura = 160
    
    inicio_l = ((LARGURA - largura)//2)
    inicio_a = ((ALTURA - altura)//2)
    fim_l = inicio_l + largura
    fim_a = inicio_a + altura
    
    passo = largura / no_imagens
    
    for i in range(150):
        img = NumPymagem(ALTURA, LARGURA, cor_fundo)
        
        img.pinte_retangulo(cor_ret, inicio_l, inicio_a, fim_l, fim_a)
        cor_ret2 = cor_ret
        
        if cor_ret2 == BLACK:
            cor_ret2 = 125
        else:
            cor_ret2 = BLACK
        
            inicio_l += int(i*passo)
            inicio_a += int(i*passo)
            fim_l -= int(i*passo)
            fim_a -= int(i*passo)
        
        img.pinte_retangulo(cor_ret2, inicio_l, inicio_a, fim_l, fim_a)
    
        video.append(img)
#-------------------------------------------------------------------------- 
if __name__ == '__main__':
    main()
