class no:
    def __init__(self, carga:any):
        self.carga = carga
        self.prox = None
    
    def __str__(self):
        return f'{self.carga}'
    
class pilha_encadeada:
    #CONSTRUTOR
    def __init__(self):
        self.__head = None
        self.__tamanho = -1
        
    #MÉTODOS ESPECIAIS
    def __len__(self):
        return self.__tamanho +1
    
    def __str__(self):
        if self.__vazia():
            return '||'
        pilha = '|'
        cursor = self.__head
        while(cursor != None):
            pilha += f'{cursor.carga}, '
            cursor = cursor.prox
        pilha = pilha.rstrip(', ') + '|'
        return pilha
    
    #MÉTODOS DE CLASSE
    def __vazia(self):
        return self.__head == None
    
    #MÉTODOS DE INSTÂNCIA
    def topo(self):
        if self.__vazia():
            print('não tem topo pois a pilha está vazia')
        else:
            return self.__head.carga

    def pesquisa(self, elemento):
        cursor = self.__head
        while(cursor != None):
            if cursor.carga == elemento:
                return cursor.carga
            cursor = cursor.prox
        print(f'{elemento} não encontrado na pilha')

    def empilha(self, carga:any):
        self.__tamanho += 1
        novo = no(carga)
        novo.prox = self.__head
        self.__head = novo

    def desempilha(self):
        if self.__vazia():
            print('Pilha vazia. Não é possível remover elementos')
        else:
            self.__tamanho -= 1
            carga = self.__head.carga
            self.__head = self.__head.prox
            return carga