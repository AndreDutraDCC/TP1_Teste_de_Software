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
        
    #Cria um vértice no grafo de nome igual a label. Se nenhuma for fornecida, o label é o sucessor do maior int entre os labels do grafo, ou 0 se for o primeiro int
    def create_vertex(self,label = ""):
        if label == "":
            label = max([id for id in self._vert_id.keys() if isinstance(id,int)], default = -1)+1
        
        if self.has_vertex(label):
            raise Exception("Já existe um vértice registrado com esse nome no grafo.")
        
        self._vert_id[label] = self.n_vert

        self._adj_l+=[[]]
        self.n_vert+=1

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
        
        if not self.direc:
            self._adj_l[self._vert_id[v]].append(u)
        
        for idx,e in enumerate(self._weights):
            if e[0] == u and e[1] == v:
                self._weights[idx][2] = weight
                return
            elif e[0] == v and e[1] == u and not self.direc:
                self._weights[idx][2] = weight
                return
        
        self._weights.append((u,v,weight))

    
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

        if not self.direc:
            self._adj_l[self._vert_id[v]].remove(u)
        
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
    
    # Dfs on vertex v
    def _dfs(self, v):
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
        
        q = queue.Queue()
        q.put(ini)

        self._reach = []
        while not q.empty():
            v     = q.get()
            self._reach.append(v)
            idx_v = self._vert_id[v]
            
            for u in self._adj_l[idx_v]:
                idx_u = self._vert_id[u]
                if not self._visited[idx_u]:
                    q.put(u)
                    self._visited[idx_u] = True

        ret = self._reach
        self._reach = []
        
        return ret
    
    
    # -------------------------- Início de um Disjoint Set Union --------------------------------
    
    # Find com Path Compression
    # Sozinho possui complexidade O(nlogn) amortizado.
    def _find(self, x):
        if(self._p[x] == x):
            return x
        else:
            self._p[x] = self._find(self._p[x])
            return self._p[x]
    
    # Une dois componentes conexos com Small to Large
    # Sozinho possui complexidade O(nlogn) amortizado.
    def _union(self, x, y):
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