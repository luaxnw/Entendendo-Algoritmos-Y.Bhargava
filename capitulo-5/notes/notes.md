# Tabela Hash

A tabela hash é uma função estrutura de dados que recebe uma string e retorna um número.
- Todas às vezes que uma string for repetida como entrada, o retorno número deve ser o mesmo. Você escreve "maçã" e retorna 3, toda vez que for digitado maçã será retornado 3.
- A função sempre retorna um valor diferente, nunca repetindo as saídas.
- A função mapeia consistentemente um nome para o mesmo índice. Quando uma string nova é adicionado, a função procura em que índice inserir ela, e depois disso a função será utilizada para encontrar esse valor.
- Mapeia diferentes strings para diferentes índices.
- A função tem conhecimento do tamanho do array e sempre retornará os valores conforme o tamanho do array.

**Em Python** a estrutura de hash são os dicionários.
```python

table = dict()
table = {'note_1': 7.5, 'note_2': 6.3} 

```
## Utilização 

- Usada quando precisamos mapear algum item com relação a outro, como um nome e telefone e uma lista telefônica.
- Usada quando precisamos buscar um item com uma chave de acesso.

**Resolução de DNS:**
A resolução de DNS é o processo automatizado de traduzir nomes de domínio legíveis por humanos (ex: exemplo.com) em endereços IP numéricos (ex: 192.0.2.1) que os computadores usam para localizar recursos na internet. Tabelas hash podem ser usadas nesta aplicação.

**Caching:**
Caching é uma técnica de armazenamento temporário de dados frequentes em local de acesso rápido (cache), reduzindo o tempo de resposta e a carga sobre servidores ou bancos de dados. Ao evitar consultas repetidas à fonte original, o cache melhora drasticamente o desempenho, escalabilidade e a experiência do usuário em aplicações web e sistemas. Os dados de caching são armazenados em tabelas hash.

Exemplo: Quando uma URL é solicitado ao Facebook, o servidor verifica se esta URL está no cache. Caso esteja, ele retorna os dados do cache, caso não, ele salva os novos dados no cache.

Assim, o servidor trabalha apenas se a URL não estiver no cache, porque quando está no cache os dados são retirados dali mesmo.

## Desempenho

O caso médio para busca, inserção e remoção em tabelas hash sempre serão O(1). Porém, no pior do casos pode ser O(n). Então é necessário implementar da forma correta.

**Fator de carga:**
É a relação entre o número de elementos e o tamanho da tabela, sendo calculado com n/m. Indica o quão cheio a tabela está e determina a frequência de colisões. Um fator de carga ideal está entre 0,5 e 0,75.
Fator de carga maior que 1 indica que há mais itens do que espaço.

## Como o dado é armazenado

Como já vimos, quando a função hash recebe uma string ela retorna uma valor númerico, sendo a string a chave e valor o índice. Esses dados são armazenados em arrays, onde o índice de cada valor é calculado assim: 

```python
# Supondo um array com espaço de 7 elementos e valor 42

hash("abc") = 94202
index = 94202 % 7
tabela[3] = {"abc": 42}
```

