from pilha_sequencial import pilha_sequencial



#teste de pilha sequencial
teste = pilha_sequencial(10)

teste.empilha(10)
teste.empilha(20)
teste.empilha(30)
teste.empilha(40)
teste.empilha(50)


print(teste)


print( teste.busca_posicao(30) )
print( teste.busca_posicao(60) )

