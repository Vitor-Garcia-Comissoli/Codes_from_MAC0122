# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM OUTRO import ...
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
    monitores e colegas). Com exceção de material de MAC0122, caso
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
# CONSTANTES
ARQUIVO = 'grafo.txt'

#------------------------------------------------------------
def main():
    ''' (None) -> None
    Essa função main() testa a classe Grafo.
    '''
    v, w, x = 'C', 'H', 'X'
    g = Grafo( ARQUIVO )
    print(g)

    print(f"V(): {g.V()}")
    print(f"A(): {g.A()}")
    print(f"Vertices: {g.vertices()}")

    print(f"Adjacentes de {v}: {g.adjacentes(v)}")
    print(f"Grau de {v}: {g.grau(v)}")
    print(f"Tem vertice {v}: {g.tem_vertice(v)}")
    print(f"Tem vertice {w}: {g.tem_vertice(w)}")
    print(f"Tem vertice {x}: {g.tem_vertice(x)}")
    print(f"Tem aresta {v}-{w}: {g.tem_aresta(v,w)}")
    print(f"Tem aresta {x}-{w}: {g.tem_aresta(x,w)}" )

    print("\nInserindo aresta H-X")
    g.insira_aresta('X', 'H')
    print(g)
    print(f"V(): {g.V()}")
    print(f"A(): {g.A()}")
    print(f"Vertices: {g.vertices()}")

    print(f"Adjacentes de {v}: {g.adjacentes(v)}")
    print(f"Grau de {v}: {g.grau(v)}")
    print(f"Tem vertice {v}: {g.tem_vertice(v)}")
    print(f"Tem vertice {w}: {g.tem_vertice(w)}")
    print(f"Tem vertice {x}: {g.tem_vertice(x)}")
    print(f"Tem aresta {v}-{w}: {g.tem_aresta(v,w)}")
    print(f"Tem aresta {x}-{w}: {g.tem_aresta(x,w)}")

#-----------------------------------------------------------------
class Grafo:
    '''
        Siga as especificações do enunciado para construir a classe Grafo.

        Coloque o seu código a seguir.
    '''
    
    def __init__(self, arquivo = None, arg = None):
        if arquivo == None:
            self.dicio = {}
            self.lista_vert = []
            # self.num_arestas = 0
        
        else:
            
            if type(arg) == str:
                argumento = True
            else:
                argumento = False
            
            f = open(arquivo, 'r', encoding='utf8')
            arq = str(f.read())
            
            dicio = {}
            lista_vert = []
            # num_arestas = 0
            
            seq = arq.split('\n')
            for i in range(len(seq)):
                if seq[i] == '':
                    None
                else:
                    if argumento:
                        if arg in seq[i]:
                            string = seq[i]
                            valores = string.split(arg)
                              
                        else:
                            string = seq[i]
                            valores = string.split()
                    else:
                        string = seq[i]
                        valores = string.split()
                    dicio[valores[0]] = valores[1:len(valores)]
                    lista_vert += [valores[0]]
            '''
            usados = []
            for i in range(len(lista_vert)):
                val = lista_vert[i]
                if i == 0:
                    num_arestas += len(dicio[val])
                    usados += [val]
                    
                else:
                    for j in range(len(dicio[val])):
                        if dicio[val][j] not in usados:
                            num_arestas += 1
                            usados += [val]
            '''                
            self.dicio = (dicio)
            self.lista_vert = (lista_vert)
            # self.num_arestas = num_arestas
        
    def __str__(self):
        
        s = ''
        
        if self.dicio == {}:
            return ''
        
        for i in range(len(self.lista_vert)):
            val = self.lista_vert[i]
            s += f'{val} | '
            for j in range(len(self.dicio[val])):
                if j == len(self.dicio[val]) - 1:
                    s += f'{self.dicio[val][j]}\n'
                else:
                    s += f'{self.dicio[val][j]}, '
        return s
        
    def insira_aresta(self, v, w):
        
        if type(v) != str or type(w) != str:
            return None
        
        v = v.strip()
        w = w.strip()
        
        if v == '' or w == '':
            return None
        
        if v in self.dicio:
            self.dicio[v] += [w]
            self.dicio[v] = (self.dicio[v])
        else:
            self.dicio[v] = [w]
            self.lista_vert += [v]
            self.lista_vert = (self.lista_vert)
            
        if w in self.dicio:
            self.dicio[w] += [v]
            self.dicio[w] = (self.dicio[w])
        else:
            self.dicio[w] = [v]
            self.lista_vert += [w]
            self.lista_vert = (self.lista_vert)
            
        # self.num_arestas += 1
        
    def tem_vertice(self, v):
        
        if v in self.dicio:
            return True
        else:
            return False
        
    def V(self):
        
        return len(self.dicio)
        
    def A(self):
        
        num_arestas = 0
        usados = []
        for i in range(len(self.lista_vert)):
            val = self.lista_vert[i]
            if i == 0:
                num_arestas += len(self.dicio[val])
                usados += [val]
                    
            else:
                for j in range(len(self.dicio[val])):
                    if self.dicio[val][j] not in usados:
                        num_arestas += 1
                        usados += [val]
                        
        return num_arestas
        
        # return self.num_arestas
        
    def vertices(self):
        
        return self.lista_vert
        
    def adjacentes(self, v):
        
        if self.tem_vertice(v) == True:
            return self.dicio[v]
        
    def grau(self, v):
        
        if self.tem_vertice(v) == True:
            return len(self.dicio[v])
        
    def tem_aresta(self, v, w):
        
        if self.tem_vertice(v) == True and self.tem_vertice(w) == True:
            if w in self.dicio[v]:
                return True
            
        return False
        
if __name__ == "__main__":
    main()