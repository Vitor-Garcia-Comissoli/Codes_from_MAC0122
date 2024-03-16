# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
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
        
        Utilizei-me somente dos conceitos ensinados na matéria anterior
        (MAC0110) e das aulas de revisão desta matéria.

'''

#--------------------------------------------------------------------------        
def imagem_nova(nlin, ncol, valor=0):
    ''' (int, int, obj) -> list

    Recebe dois inteiros nlin e ncol e um valor. 
    Cria e retorna uma imagem de dimensão nlin x ncol com valor em cada 
    posição.

    Exemplos:
    >>> t = imagem_nova(3,4,-1)
    >>> t
    [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
    >>> tt = imagem_nova(3,3,0)
    >>> tt
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    >>> 
    '''
    matriz = []
    
    for i in range(nlin):
        lin = ncol * [valor]
        matriz += [lin]
        
    return matriz
    '''
    print("imagem_nova(): Vixe! Essa função ainda não foi feita.")
    '''
#--------------------------------------------------------------------------        
def imagem_carrega(dest, orig):
    ''' (list, list) -> None

    Recebe duas imagens de mesma dimensão e carrega o conteúdo de orig 
    na imagem dest.

    Exemplo:

    >>> t = [[12, -122, 3],[1, 2, 3]]
    >>> tt = [[11, 22, 33],[44, 55, 66]]
    >>> imagem_carrega(tt, t)
    >>> t
    [[12, -122, 3], [1, 2, 3]]
    >>> tt
    [[12, -122, 3], [1, 2, 3]]
    >>> tt[0][0] = 777
    >>> t
    [[12, -122, 3], [1, 2, 3]]
    >>> tt
    [[777, -122, 3], [1, 2, 3]]
    '''
    nlin = len(dest)
    ncol = len(dest[0])
    
    for i in range(nlin):
        for j in range(ncol):
            dest[i][j] = orig[i][j]
    
    return
    
    '''
    print("imagem_carrega(): Vixe! Essa função ainda não foi feita.")
    '''
#--------------------------------------------------------------------------        
def imagem_clone(imagem):
    ''' (list) -> list

    Recebe uma imagem e retorna um clone da imagem.

    Exemplo:
    >>> t = [[12, -122, 3],[1, 2, 3]]
    >>> tt = imagem_clone(t)
    >>> t
    [[12, -122, 3], [1, 2, 3]]
    >>> tt
    [[12, -122, 3], [1, 2, 3]]
    >>> tt[0][0] = 111111
    >>> t
    [[12, -122, 3], [1, 2, 3]]
    >>> tt
    [[111111, -122, 3], [1, 2, 3]]
    >>> 
    '''
    nlin = len(imagem)
    ncol = len(imagem[0])
    
    clone = imagem_nova(nlin, ncol)
    
    for i in range(nlin):
        for j in range(ncol):
            clone[i][j] = imagem[i][j]
    
    return clone
    
    '''
    print("imagem_clone(): Vixe! Essa função ainda não foi feita.")
    '''
#--------------------------------------------------------------------------        
def imagem_regiao(imagem, left, top, right, bottom):
    ''' (list, int, int, int, int) -> list

    Recebe uma imagem e 4 valores que definem um região retangular onde:
    top define a primeira linha, bottom define a última linha,  
    left define a primeira coluna, e right define a última coluna da região.
    A função cria e retorna uma imagem de dimensão
    (bottom - top) linhas por (right-left) colunas, 
    com conteúdo igual à região correspondente na imagem. 
    Observe que os pontos na linha bottom e coluna right NÃO 
    fazem parte da região retangular.
    
    Exemplo:
    >>> imagem_regiao([[1, 2, 3, 4, 5], 
                       [2, 3, 4, 5, 6], 
                       [3, 4, 5, 6, 7], 
                       [4, 5, 6, 7, 8] ], 1, 0, 4, 3)
    [[2,3,4], [3,4,5], [4, 5, 6]]
    >>> imagem_regiao([[1, 2, 3, 4, 5], 
                       [6, 7, 8, 9, 0], 
                       [0, 9, 8, 7, 6], 
                       [1, 2, 3, 4, 5] ], 1, 2, 3, 4)
    [[9,8], [2,3]]
    '''
    nlin = (bottom - top)
    ncol = (right - left)
    
    matriz = imagem_nova(nlin, ncol, 0)
    
    a = top
    b = left
    
    for i in range(nlin):
        for j in range(ncol):
            matriz[i][j] = imagem[a][b]
            b += 1
            
        b = left
        a += 1
        
    return matriz

    '''
    print("imagem_regiao(): Vixe! Essa função ainda não foi feita.")
    '''
#--------------------------------------------------------------------------            
