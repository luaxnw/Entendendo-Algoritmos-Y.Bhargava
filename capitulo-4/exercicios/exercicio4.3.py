#Encontre o valor mais alto em uma lista.

def maior_valor_lista(lista):
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i
    return maior

# testando

lista = [1,5,-7,12,8,9]
maior = maior_valor_lista(lista)

print(maior)