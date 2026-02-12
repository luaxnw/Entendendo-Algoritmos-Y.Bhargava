# Pesquisa em Largura

A pesquisa em largura (Breadth-First Search - BFS) é um algoritmo que percorre os elementos de grafos ou árvores, lendo vizinhos de nível em nível, partindo de um nó raiz. Tem os **objetivos** de procurar um caminho entre vértices A e B e o menor caminho entre eles.

# Filas

Filas são um tipo de estrutura de dados que funciona como uma fila da vida real. Possuindo apenas funções de adicionar no fim da fila ou remover no início, enqueue e dequeue respectivamente. Esse tipo de estrutura possui a nomenclatura de FIFO, ou First-in, First-out. Em comparação com a pilha que é LIFO, ou Last-in, Last-out.

# Implementação do algoritmo

1. Crie um fila com os elementos a serem lidos.
2. Faça uma lista para guardar quais elementos foram lidos, garantindo que não serão lidos mais de uma vez.
3. Faça dequeue e leia esse elemento removido.
4. Se for o alvo finalize, caso não, prossiga com os dequeue. A cada nova chave registrada será carregado todos seus valores conjuntos. Supondo que alice é a atual chave e possui vértice A e esse por sua vez possui vértice B, C, D etc. quando descartamos alice e o próximo elemento lido é A, todos os vértices de A (B,C,D) são colocados na lista.
5. Repita até localizar o alvo ou não.

```python

from collections import deque

def pessoa_e_alvo(nome):
    return nome[-1] == 'm' # -1 no index representa último elemento

grafo = {}
grafo["voce"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []

fila_pesquisa = deque()
fila_pesquisa += grafo["voce"]

while fila_pesquisa != []: # podemos tirar o != [], pois lista vazia = false e oposto = true
    pessoa = fila_pesquisa.popleft() # pessoa assume o elemento removido da lista
    if pessoa_e_alvo(pessoa):
        print(f"{pessoa} é o alvo ")
        return True
    else:
        fila_pesquisa += grafo[pessoa] # caso não seja o alvo, chama a nova pesoa como chave, para
return False                            # verificar os seus valores

```

# Tempo de Execução

Se você procurar um vendedor de mangas em toda a sua rede, cada aresta (lembre-se de que aresta é a seta ou a conexão entre uma pessoa e outra) será analisada. Portanto o tempo de execução é, no
mínimo, O(número de arestas). Além disso, também será mantida uma lista com as pessoas já verificadas. Adicionar uma pessoa à lista leva um tempo constante: O(1). Fazer isso para cada pessoa terá tempo de execução O(número de pessoas) no total. Assim, a pesquisa em largura tem tempo de execução O(número de pessoas + número de arestas), que é frequentemente escrito como O(V+A) (V para número de vértices, А para número de arestas).

# Recapitulando 

- A pesquisa em largura lhe diz se há um caminho de A para B.
- Se esse caminho existir, a pesquisa em largura lhe dará o caminho mínimo.
- Grafos não direcionados não contêm setas, e a relação acontece nos dois sentidos
- Você precisa verificar as pessoas na ordem em que elas foram adicionadas à lista de pesquisa. Portanto a lista de pesquisa deve ser uma fila; caso contrário, você não obterá o caminho mínimo.
- Cada vez que você precisar verificar alguém, procure não verificálo novamente. Caso contrário poderá acabar em um loop infinito.