# BIG O

A notação Big O serve para dizer o quão rápido um algoritmo cresce. Supondo um tamanho N em uma lista, a notação diz que o crescimento é O(n), permitindo comparar os números de operações. Basicamente, diz o comportamento do algoritmo em velocidade e tempo baseados na entrada recebida.

- Geralmente descreve o pior caso, para garantir que ele nunca será mais lento que o limite especificado. Como em situação que de 16 entradas que utilizo notação O(log n)
resultando em O(log 16) = 4 ---> 4 representa passos máximos para esse algoritmo, o pior dos casos.
- Não mede a velocida em segundos, mas a taxa de variação conforme dados são processados. Sendo uma medida que representa a quantidade de crescimento do número de operações.
- O tempo é de execução em algoritmos é expresso pela notação Big O.
- Um algoritmo é bom quando cresce lentamente à medida que o tamanho da entrada aumenta.

## Aqui temos cinco tempos de execução Big O que você encontrará (mais rápido ao mais lento)

- O(log n), também conhecido como tempo logarítmico. Exemplo: pesquisa binária.
- O(n), conhecido como tempo linear. Exemplo: pesquisa simples.
- O(n * log n). Exemplo: um algoritmo rápido de ordenação, como a ordenação quicksort (explicada no Capítulo 4).
- O(n²). Exemplo: um algoritmo lento de ordenação, como ordenação por seleção (explicada no Capítulo 2).
- O(n!). Exemplo: um algoritmo bastante lento, como o do caixeiroviajante (Funciona como permutação).

### Resumindo

Não importa o número exato dado pela notação, mas sim o quanto ela cresce dependendo da entrada (n). Descrevendo uma taxa de crescimento do tempo do algoritmo em função do tamanho da entrada.