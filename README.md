# TP1_Teste_de_Software

## Integrantes

* André Luiz Moreira Dutra - 2019006345
* João Antônio Oliveira Pedrosa - 2019006752
* Átila Augusto Carvalho -  2019006442


## O Sistema

A proposta da Graph_API é oferecer um framework de manipulação de grafos para a linguagem Python 3.8, com classes e métodos para representar os grafos e os algoritmos aplicáveis a eles, usando apenas bibliotecas e frameworks nativos. O sistema funciona nos sistemas operacionais Ubuntu (e outras distribuições Linux), Windows e MacOS.

### GRAPH

A API consiste em apenas uma classe chamada Graph, representando o grafo, com diversos métodos representando algoritmos clássicos de grafos, todos desenvolvidos do zero pelos integrantes do grupo. Além dos métodos primitivos para inserção e deleção de arestas e vértices, a classe conta com várias funcionalidades como:

- Encontrar todos os vértices atingíveis a partir de um vértice - Breadth First Search O(V) e Depth First Search O(V)
- Determinar existência de ciclos - Algoritmo de Coloração O(V)
- Número de Componentes Conexos - Depth First Search O(V)
- Encontrar a menor distância de um vértice para todos os vértices que ele consegue atingir - Algoritmo de Dijkstra O(E log V)
- Estrutura para manter componentes conexos - Disjoint Set Union O(Ackermann^(-1)(V))
- Árvore Geradora Mínima - Algoritmo de Kruskal O(V log V)
- Ordenação Topológica - O(V)
- Descobrir se é fortemente conexo - V Kosarajus O(V^2)
- Descobrir se é bipartido - Algoritmo de Coloração O(V)

### MENU

Para permitir que usuários não habituados à linguagem também possam usar as funcionalidades da API sem precisar instanciar a classe Graph, também é oferecido o módulo Menu.py, que traz um menu interativo para o uso da API no terminal. O menu apresenta opções para criar novos grafos, modificar os grafos criados e aplicar nos grafos os respectivos algoritmos. Cada opção é selecionada dando entrada com o caractere correspondente, de maneira intuitiva. Para inicializar o menu, basta executar no terminal:

python3 Menu.py

## Tecnologias usadas

O sistema foi programado usando a linguagem Python (versão 3.8), e para os testes foi usado o framework de testes nativo unittest. Apenas bibliotecas e frameworks nativos foram utilizados no processo, como incentivo à implementação clássica dos algoritmos oferecidos.