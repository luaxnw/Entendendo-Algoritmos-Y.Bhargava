Programação dinâmica
===============

Dependendo do problema e do conjunto de soluções, podemos ter um tipo de programa com execução O(n²), o que não é nada rápido. Lembrando que em um caso assim, cada item adicionado duplica o número de passos/conjuntos possíveis. Vimos no caítulo anterior uma maneira de fazer um cálculo aproximado do melhor conjunto para atender os requisitos. Talvez não seja a melhor opção, por isso usamos a programação **dinâmica**.

# Como funciona
Em códigos muito complexos, podemos criar uma estrutura de dados para controlar o que já foi lido, uma forma de não analisar dados repetidos. é uma ferramenta poderosa para resolver subproblemas utilizando estas respostas para resolver um problema geral. Porém a programação dinâmica só funciona quando os seus subproblemas são discretos, ou seja, quando eles não são dependentes entre si.

```python
def fibNaoDinamico(n):
    if n == 0 or n == 1:
        return n
    return fibNaoDinamico(n - 1) + fibNaoDinamico(n - 2)


def fibDinamico(n, arrayAux):
    if n == 0 or n == 1:
        return n
    
    if arrayAux[n] is None:
        arrayAux[n] = fibDinamico(n-1,arrayAux) + fibDinamico(n-2,arrayAux)
    return arrayAux[n]
```


## Quando usar
A programação dinâmica é útil quando você está tentando otimizar em relação a um limite. No problema da mochila, era necessário maximizar o valor dos itens roubados, limitados pela capacidade
da mochila. Você pode utilizar a programação dinâmica quando o problema puder ser separado em subproblemas discretos que não dependam um do outro.