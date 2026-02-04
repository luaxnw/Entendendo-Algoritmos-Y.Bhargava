#Escreva uma função recursiva que conte o número de itens em uma lista

def contaValores(lista):
    
    if lista == []:
        return 0
    return 1 + contaValores(lista[1:])

#Resposta

lista = [1,5,6,2,6]
teste = contaValores(lista)
print(teste)