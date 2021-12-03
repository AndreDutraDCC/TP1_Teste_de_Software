import queue

class Graph:
    def __init__(self,direcionado = False):
        self.n_vert = 0
        self.direc = direcionado
        self._vert_id    = dict()
        self._adj_l = []
        self._weights = []
        
        # Auxiliares para os algoritmos de visitação
        self._visited = []
        self._reach   = []
        
        # Auxiliar para o Disjoint Set Union
        self._p       = dict()
        self._pSize   = dict()
        
        # Auxiliar para os algoritmos de ciclo
        self._color   = dict()
        
        # Auxiliar para o toposort
        self._entry_degree = dict()
        
    # ----------------------- Funções Primitivas ---------------------------
    
    #Cria um vértice no grafo de nome igual a label. Se nenhuma for fornecida, o label é o sucessor do maior int entre os labels do grafo, ou 0 se for o primeiro int
    def create_vertex(self,label = ""):
        if label == "":
            label = max([id for id in self._vert_id.keys() if isinstance(id,int)], default = -1)+1
        
        if self.has_vertex(label):
            raise Exception("Já existe um vértice registrado com esse nome no grafo.")
        
        self._vert_id[label] = self.n_vert

        self._adj_l+=[[]]
        self.n_vert+=1
        self._entry_degree[label] = 0

        return label
    
    #Checa se o vértice de label u pertence ao grafo
    def has_vertex(self,u):
        return u in self._vert_id.keys()
    
    #Retorna os labels de todos os vértices do grafo
    def get_vertices(self):
        return list(self._vert_id.keys())

    #Cria uma aresta u→v no grafo (ou em ambas dieções se não direcionado) e de peso weight. O peso por padrão é 1
    def create_edge(self,u,v,weight = 1):
        if not self.has_vertex(u):
            raise Exception("O vértice "+str(u)+" não está registrado no grafo")
        if not self.has_vertex(v):
            raise Exception("O vértice "+str(v)+" não está registrado no grafo")
        
        if v not in self._adj_l[self._vert_id[u]]:
            self._adj_l[self._vert_id[u]].append(v)
        self._entry_degree[v] += 1
        
        if not self.direc:
            self._adj_l[self._vert_id[v]].append(u)
            self._entry_degree[u] += 1
            
        for idx,e in enumerate(self._weights):
            if e[0] == u and e[1] == v:
                self._weights[idx][2] = weight
                return
            elif e[0] == v and e[1] == u and not self.direc:
                self._weights[idx][2] = weight
                return
        
        self._weights.append((u,v,weight))

    #Indica se a aresta u→v pertence ao grafo
    def has_edge(self,u,v):
        for e in self._weights:
            if e[0] == u and e[1] == v:
                return True
            elif e[0] == v and e[1] == u and not self.direc:
                return True
        
        return False
    
    #Retorna o peso da aresta u→v se ela existir
    def get_weight(self,u,v):
        for e in self._weights:
            if e[0] == u and e[1] == v:
                return e[2]
            elif e[0] == v and e[1] == u and not self.direc:
                return e[2]
        
        raise Exception("Aresta não existe")
        
    # Retorna lista de arestas na forma [Peso, V1, V2]
    def get_edges(self):
        edges = []
        
        for v in self.get_vertices():
            idx_v = self._vert_id[v]
            for u in self._adj_l[idx_v]:
                weight = self.get_weight(v, u)
                edges.append([weight, v, u])
                
        return edges
    
    #Deleta a aresta u→v do grafo (em ambas as direções se for não direcionado)
    def del_edge(self,u,v):
        if not self.has_edge(u,v):
            return
        
        self._adj_l[self._vert_id[u]].remove(v)
        self._entry_degree[v] -= 1
        
        if not self.direc:
            self._adj_l[self._vert_id[v]].remove(u)
            self._entry_degree[u] -= 1
        
        for e in self._weights:
            if e[0] == u and e[1] == v:
                self._weights.remove(e)
                return
            elif e[0] == v and e[1] == u and not self.direc:
                self._weights.remove(e)
                return
    
    #Deleta o vértice u do grafo e todas as arestas adjacentes a ele
    def del_vertex(self,u):
        if not self.has_vertex(u):
            return
        
        for v in self._adj_l[self._vert_id[u]]:
            self.del_edge(u,v)
        
        if self.direc:
            for v in self._vert_id.keys():
                if u in self._adj_l[self._vert_id[v]]:
                    self.del_edge(v,u)
        
        self._adj_l[self._vert_id[u]] = self._adj_l[-1]
        self._adj_l.pop()

        vid_keys = list(self._vert_id.keys())
        vid_values = list(self._vert_id.values())
        idx_of_last = vid_values.index(self.n_vert-1)
        substit_key = vid_keys[idx_of_last]

        self._vert_id[substit_key] = self._vert_id[u]
        self._vert_id.pop(u)

        self.n_vert-=1
    
    # --------------------- Algoritmos ----------------------------------
    
    # Dfs on vertex v
    def _dfs(self, v):
        if not self.has_vertex(v):
            raise Exception("O vértice "+str(v)+" não está registrado no grafo")
            
        idx_v       = self._vert_id[v]
        self._visited[v]  = True
        for u in self._adj_l[idx_v]:
            idx_u = self._vert_id[u]
            if not self._visited[idx_u]:
                self._dfs(u)
        
        self._reach.append(v)
        
    # Retorna uma lista com todos os vértices que ini alcança, na ordem de uma DFS
    def dfs(self, ini):
        if not self.has_vertex(ini):
            raise Exception("O vértice "+str(ini)+" não está registrado no grafo")
        
        # Inicializando os vetores de visitação
        idx_ini = self._vert_id[ini]
        self._visited = [False for i in range(self.n_vert)]
        self._visited[idx_ini] = True
        
        self._reach = []
        self._dfs(ini)
        
        ret = self._reach
        self._reach = []
        
        return ret
    
    # Retorna uma lista com todos os vértices que ini alcança, na ordem de uma BFS
    def bfs(self, ini): 
        if not self.has_vertex(ini):
            raise Exception("O vértice "+str(ini)+" não está registrado no grafo")

        idx_ini      = self._vert_id[ini]
        self._visited      = [False for i in range(self.n_vert)]
        self._visited[idx_ini] = True
        
        # Usamos uma fila pois numa BFS queremos uma estrutura do tipo FIFO
        q = queue.Queue()
        q.put(ini)

        self._reach = []
        while not q.empty():
            v     = q.get()
            self._reach.append(v)
            idx_v = self._vert_id[v]
            
            # Visitamos todos os filhos que não foram visitados ainda
            for u in self._adj_l[idx_v]:
                idx_u = self._vert_id[u]
                if not self._visited[idx_u]:
                    q.put(u)
                    self._visited[idx_u] = True

        ret = self._reach
        self._reach = []
        
        return ret
    
    # Retorna um dicionário com a menor distância de ini até os outros vértices
    # Algoritmo de Dijkstra - Complexidade O(E log(V))
    def dijkstra(self, ini):
        if not self.has_vertex(ini):
            raise Exception("O vértice "+str(ini)+" não está registrado no grafo")
        
        # Inicializando os vetores de visitação
        idx_ini                = self._vert_id[ini]
        self._visited          = [False for i in range(self.n_vert)]
        self._visited[idx_ini] = True
        
        distance = dict()
        for k in self.get_vertices():
            distance[k] = float("inf")
        
        # Mantemos uma fila de prioridade, assim, o candidato com menor distância é analisado primeiro
        q = queue.PriorityQueue()
        q.put([0, ini])
        distance[ini] = 0
        
        while not q.empty():
            dist, v  = q.get()
            
            # Distancias maiores podem ser inseridas na priority_queue, pulamos essas
            if dist > distance[v]:
                continue
                
            idx_v    = self._vert_id[v]
            for u in self._adj_l[idx_v]:
                idx_u = self._vert_id[u]
                w     = self.get_weight(v, u)
                # Checamos se compensa adicionar essa distância
                if distance[u] > distance[v] + w:
                    distance[u] = distance[v] + w
                    q.put([distance[u], u])        
        
        return distance
    
    # -------------------------- Início de um Disjoint Set Union --------------------------------
    
    # Find com Path Compression
    # Sozinho possui complexidade O(nlogn) amortizado.
    def _find(self, x):
        if not self.has_vertex(x):
            raise Exception("O vértice "+str(x)+" não está registrado no grafo")
        
        if(self._p[x] == x):
            return x
        else:
            self._p[x] = self._find(self._p[x])
            return self._p[x]
    
    # Une dois componentes conexos com Small to Large
    # Sozinho possui complexidade O(nlogn) amortizado.
    def _union(self, x, y):
        if not self.has_vertex(x):
            raise Exception("O vértice " + str(x)+ " não está registrado no grafo")
        if not self.has_vertex(y):
            raise Exception("O vértice " + str(y)+ " não está registrado no grafo")
        
        # X = Cabeça do componente de X
        # Y = Cabeça do componente de Y
        x = self._find(x)
        y = self._find(y)
        
        if(x == y):
            return False
        
        # Garantindo que x é o componente maior
        if self._pSize[x] < self._pSize[y]:
            aux = y
            y   = x
            x   = aux
        
        # Pai de Y passa a ser X
        self._p[y]  =  x
        self._pSize[x] += self._pSize[y]
        
        return True
    
    # A união das duas técnicas possui complexidade igual à Inversa da Função de Ackermann.
    # No caso dessa classe, a constante fica alta por causa do hash do Dict. 
    # Mas em um caso sem labels, seria praticamente O(1).
    
    # -------------------------- Fim do Disjoint Set Union --------------------------------------
    
    # Retorna outro objeto do tipo Graph. A Minimum Spanning Tree do Grafo atual.
    # Atenção: Em casos de grafos desconexos, o algoritmo retorna a Minimum Spanning Forest
    def MST(self):
        # Inicialmente vamos criar um vetor de arestas da forma [Peso, Vertice 1, Vertice 2]
        edges = self.get_edges()
        
        # Novo grafo
        mst = Graph()
        
        # Inicializando variáveis do DSU e novo grafo
        for k in self.get_vertices():
            mst.create_vertex(k)
            self._p[k]     = k
            self._pSize[k] = 1
            
        # Agora a gente itera pelas arestas, começando pelos menores pesos e vai construindo nossa árvore
        edges = sorted(edges)
        for w, a, b in edges:
            if(self._union(a, b)):
                mst.create_edge(a, b, weight = w)
                
        self._p = dict()
        self._pSize = dict()
        
        return mst
    
    # Transforma o grafo numa árvore, mantendo os vértices com o maior grau possível
    # Para grafos desconexos, retorna uma floresta
    def treefy(self):
        # Inicialmente vamos criar um vetor de arestas da forma [Peso, Vertice 1, Vertice 2]
        edges = self.get_edges()
        
        # Novo grafo
        tree = Graph()
        
        # Inicializando variáveis do DSU e novo grafo
        for k in self.get_vertices():
            tree.create_vertex(k)
            self._p[k]     = k
            self._pSize[k] = 1
            
        # Agora a gente itera pelas arestas e constrói uma árvore toda ve
        for w, a, b in edges:
            if(self._union(a, b)):
                tree.create_edge(a, b, weight = w)
                
        self._p = dict()
        self._pSize = dict()
        
        return tree
    
    # DFS que atualiza a cor dos vértices para encontrar um ciclo
    # 0 = Não Visitado, 1 = Visitando, 2 = Visitado
    # Parametros: Vértice a Executar, Pai do Vértice a executar
    def _dfs_color(self, v, p):
        if not self.has_vertex(v):
            raise Exception("O vértice " + str(v) + " não está registrado no grafo.")
            
        # Checamos se já visitamos esse vértice completamente antes
        if(self._color[v] == 2):
            return False
        
        # Se checamos em um vértice no estado de "Visitando", encontramos um ciclo
        if(self._color[v] == 1):
            return True
        
        # Marcamos o vértice como "Visitando"
        self._color[v] = 1
        idx_v = self._vert_id[v]
        
        # Visitamos todos os vizinhos, com exceção do pai (Para evitar loop)
        for u in self._adj_l[idx_v]:
            if u != p:
                if self._dfs_color(u, v):
                    return True
            
        self._color[v] = 2
        return False
    
    # Identifica se existe algum ciclo no grafo
    def has_cycle(self):
        
        # Inicializando as cores
        for v in self.get_vertices():
            self._color[v] = 0
            
        for v in self.get_vertices():
            if(self._color[v] != 2):
                if(self._dfs_color(v, -1)):
                    return True
        
        # Não encontramos ciclo
        return False
    
    # Retorna o número de componentes conexos do grafo
    def components(self):
        ans = 0
        
        # Inicializando os vetores de visitação
        self._visited = [False for i in range(self.n_vert)]
        
        # Checamos para cada vértice se ele foi visitado
        # Caso não tenha sido, acrescentamos mais um componente à resposta e rodamos uma dfs
        for v in self.get_vertices():
            idx_v = self._vert_id[v]
            if not self._visited[idx_v]:
                self._dfs(v)
                ans += 1
                
        self._reach = []
        
        return ans
    
    # DFS para o toposort
    def _topodfs(self, v):
        idx_v = self._vert_id[v]
        
        # Não existem ciclos no grafo
        # então eu não preciso me preocupar com o fato de os vértices terem ou não sido visitados 
        for u in self._adj_l[idx_v]:
            self._topodfs(u)
        
        self._reach.append(v)
        
    
    # Retorna uma ordenação topológica dos vértices
    # Isso significa que, se existe uma aresta de u para v, então u vem antes de v na ordenação
    def toposort(self):
        if not self.direc:
            raise Exception("Ordenação topológica só é definida para grafos direcionados!")
            
        if self.has_cycle():
            raise Exception("Não é possível definir uma ordenação topológica em um grafo com ciclos.")
        
        # Primeiro a gente precisa encontrar um vértice com grau de entrada 0
        # i.e. um vértice que possa ser o início da nossa ordenação topológica
        ini = []
        for k in self.get_vertices():
            if self._entry_degree[k] == 0:
                ini.append(k)
                
        if len(ini) == 0:
            raise Exception("Não foi encontrado um vértice com grau de entrada 0")
        
        self._reach   = []
        
        # Obtemos a ordenação topológica inversa
        for k in ini:
            self._topodfs(k)
        
        # E invertemos ela de volta
        answer = self._reach
        answer.reverse()
        
        self._reach = []
        
        return answer
    
    # Diz se o grafo é fortemente conexo.
    # Ser fortemente conexo só é definido para grafos direcionados e diz se, a partir de um vértice, é possível chegar em todos os demais
    def strongly_connected(self):
        if not self.direc:
            raise Exception("Conexão forte só é definida para grafos direcionados!")
        
        num_v = 0
        
        # Iremos definir o grafo reverso de G
        gR = Graph(direcionado = True)
        
        for v in self.get_vertices():
            gR.create_vertex(v)
            num_v += 1
            
        # Revertendo as arestas
        for w, v, u in self.get_edges():
            gR.create_edge(u, v, weight = w)
        
        # A proposta é muito simples
        
        # Se existe algum vértice v que todo mundo alcança
        # e ao mesmo tempo esse vértice v alcança todo mundo
        # então todos alcançam todos.
        
        # A prova é facil. Se eu quero ir de a pra b
        # basta eu ir de a pra v e então ir de v pra b
        
        for v in self.get_vertices():
            i_reach  = self.bfs(v)
            reach_me = gR.bfs(v)
            
            if(len(i_reach) == num_v and len(reach_me) == num_v):
                return True
               
        return False
    
    # Retorna se um grafo é bipartido. Basicamente se tiver ciclo de tamanho
    # ímpar é impossível mas vamos resolver com uma coloração preto e branco
    def bipartite(self):
        
        ini = None
        for k in self.get_vertices():
            self._color[k] = -1
            if(ini is None):
                ini = k
        idx_ini = self._vert_id[ini]
        
        q = queue.Queue()
        q.put(ini)
        
        self._color[ini] = 0
        while not q.empty():
            v     = q.get()
            
            idx_v = self._vert_id[v]            
            cur_color = self._color[v]
            new_color = (cur_color + 1) % 2 # <- 0 vira 1 e 1 vira 0
            
            # Visitamos todos os filhos que não foram visitados ainda
            for u in self._adj_l[idx_v]:
                if self._color[u] == cur_color:
                    return False
                if self._color[u] == -1:
                    q.put(u)
                    self._color[u] = new_color

        # Não encontramos conflito
        return True