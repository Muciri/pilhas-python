from pilha_sequencial import pilha_sequencial
from pilha_encadeada import pilha_encadeada


#TESTE DA PILHA SEQUENCIAL
print('=-=-=-=-=-=-TESTE DA PILHA SEQUENCIAL=-=-=-=-=-=-')
teste = pilha_sequencial(10)

print(teste)
print(len(teste))

teste.empilha(10)
teste.empilha(20)
teste.empilha(30)
teste.empilha(40)
teste.empilha(50)

print(teste)
print(len(teste))

print(teste.topo())
print(teste.busca_elemento(3))


print( teste.busca_posicao(30) )
print( teste.busca_posicao(60) )

#TESTE DA PILHA ENCADEADA
print('=-=-=-=-=-=-TESTE DA PILHA ENCADEADA=-=-=-=-=-=-')
pilha = pilha_encadeada()

print(len(pilha))  # Saída: 0 (Pilha vazia)
print(pilha)       # Saída: ||

pilha.empilha(5)
pilha.empilha(10)
pilha.empilha(15)

print(len(pilha))  # Saída: 3
print(pilha)       # Saída: |15, 10, 5|

print(pilha.topo())  # Saída: 15

print(pilha.desempilha())  # Saída: 15
print(len(pilha))          # Saída: 2
print(pilha)               # Saída: |10, 5|

pilha.pesquisa(10)  # Saída: 10
pilha.pesquisa(20)  # Saída: "20 não encontrado na pilha"