class no:
    def __init__(self, carga:any):
        self.carga = carga
        self.next = None
    
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
    
    #MÉTODOS DE CLASSE
    def __vazia(self):
        return self.__head == None
    
    
