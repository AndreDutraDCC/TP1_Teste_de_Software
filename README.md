# TP1_Teste_de_Software

## Integrantes

* André Luiz Moreira Dutra - 2019006345
* João Antônio Oliveira Pedrosa - 2019006752
* Átila - 


## O Sistema

### GRAPH

O sistema consiste em apenas uma classe chamada Graph, com diversos métodos representando algoritmos clássicos de grafos, todos desenvolvidos do zero pelos integrantes do grupo. Além dos métodos primitivos para inserção e deleção de arestas e vértices, a classe conta com várias funcionalidades como:

- Encontrar todos os vértices atingíveis a partir de um vértice - Breadth First Search $\mathcal{O}(V)$ e Depth First Search $\mathcal{O}(V)$
- Determinar existência de ciclos - Algoritmo de Coloração $\mathcal{O}(V)$
- Número de Componentes Conexos - Depth First Search $\mathcal{O}(V)$
- Encontrar a menor distância de um vértice para todos os vértices que ele consegue atingir - Algoritmo de Dijkstra $\mathcal{O}(E \log V))$
- Estrutura para manter componentes conexos - Disjoint Set Union $\mathcal{O}(Ackermann^{-1}(V))$
- Árvore Geradora Mínima - Algoritmo de Kruskal $\mathcal{O}(V \log V)$
- Ordenação Topológica - $\mathcal{O}(V)$
- Descobrir se é fortemente conexo - $V$ Kosarajus $\mathcal{O}(V^2)$
- Descobrir se é bipartido - Algoritmo de Coloração $\mathcal{O}(V)$

