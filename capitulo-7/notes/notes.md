# Algoritmo de Dijkstra

Em grafos não ponderados e árvores vamos utilizar a pesquisa em largura para fazer a pesquisa entre os elementos e encontrar o caminho mínimo, que é onde há menos arestas para percorrer. O alogoritmo de Dijkstra funciona em casos de grafos ponderados, que são grafos que cada aresta está atribuída um custo, como um tempo. Então esse algoritmo efetua a pesquisa em grafos ou árvores (raramente em árvores, pois elas possuem um único caminho entre vértices) que possuem arestas ponderadas e determinam o caminho mais rápido.

![](dijkstra-algoritmo.png)

1. Encontre o vértice mais barato. Este é o vértice em que você consegue chegar no menor tempo possível.
2. Atualize o custo dos vizinhos do vértice escolhido (vértices com pesos desconhecidos terão o peso definido como infinito).
3. Repita até que tenha feito isso para todos os vértices do grafo.
4. Calcule o caimho final.

# Implementação

Vamos precisar fazer uma tabela hash (dicionário) para o grafo, pesos e pais:

```python

grafo = {}
grafo["voce"] = ["Alice", "Clara", "Joao"]

grafo["inicio"] = {} # cria outra tabela para contar os pesos
grafo["inicio"]["a"] = 5
grafo["inicio"]["b"] = 2 

print(grafo["inicio"].keys()) # mostra as chaves (a e b)
print(grafo["inicio"]["a"]) # mostra apenas a chave selecionada.

grafo["a"] = {} # cria tabela hash para cada vértice 
grafo["a"]["fim"] = 1 # em ordem, vértice, seu vizinho e peso
 
grafo["b"] = {} 
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

grafo["fim"] = {} # vértice fim não tem vizinho.

# para melhor entedimento, será criado uma tabela como os custos

custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

# agora para os pais

pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

# Agora um array para registrar os já lidos

processados = []
```
Agora vamos para o looping que seguirá os passos:
1. Enquanto houver grafos a serem processados.
2. Pegue o vértice que está mais próximo do início
3. Atualize os custos para seus vizinhos.
4. Se qualquer valor de custo for atualizado, atualize os pais também.
5. Marque o vértice como processado e refaça

```python
nodo = ache_no_custo_mais_baixo(custos)
while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys():
        novo_custo = custo + vizinho[n]
        if custos[n] > novo_custo
        custos[n] = novo_custo
        pais[n] = nodo
    processados.append(nodo)
    nodo = ache_no_custo_mais_baixo(custos) 
```