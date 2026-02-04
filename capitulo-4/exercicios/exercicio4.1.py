# Escreva o código para a função soma, vista anteriormente.

def somaLista(lista):
    total = 0
    for element in lista:
        total += element
    return total

#teste

list = [1,6,8,9,10,2]
teste = somaLista(list)
print(list,"\n")
print(f"soma lista--> {teste}\n")
    
