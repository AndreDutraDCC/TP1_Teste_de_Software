from Graph_API import Graph
from os import system,name

#def clear():
#    if name == 'nt':
#        system("cls")
#    else:
#        system("clear")

class Menu:
    def __init__(self):
        self.graphs = []
        self.state = 0
        self.graph_id = 0
        self.n_graphs = 0
        self.action = ""
    
    def main(self):
        print("")
#        clear()
        while(True):
            if self.state == 0:
                self.first_menu()
            
            elif self.state == 1:
                self.new_graph_menu()
            
            elif self.state == 2:
                self.graphs_menu()
            
            elif self.state == 3:
                self.one_graph_menu()
            
            elif self.state == 4:
                self.actions_menu()
            
            elif self.state == 5:
                self.one_action_menu()
            
            else: return
            print("\n")
#            clear()
            
        
    #state 0
    def first_menu(self):
        print("Graph API\n")
        print("1) Novo Grafo")
        print("2) Grafos Existentes")
        print("X) Sair")

        option = input("\nOpção: ")
        if option == "1":
            self.state = 1
        elif option == "2":
            self.state = 2
        elif option == 'X' or option == 'x':
            self.state = 6
        else:
            self.state = 0
    
    #state 1
    def new_graph_menu(self):
        print("Novo Grafo\n")
        print("1) Direcionado")
        print("2) Não Direcionado")
        print("V) Voltar")

        option = input("\nOpção: ")
        if option == "1":
            self.graphs.append(Graph(directed=True))
            self.graph_id = self.n_graphs
            self.n_graphs += 1
            self.state = 3
        elif option == "2":
            self.graphs.append(Graph())
            self.graph_id = self.n_graphs
            self.n_graphs += 1
            self.state = 3
        elif option == 'V' or option == 'v':
            self.state = 0
        else:
            self.state = 1

    #state 2
    def graphs_menu(self):
        print("Grafos Existentes\n")
        for i in range(1,self.n_graphs+1):
            print(str(i)+") Grafo "+str(i))
        print("V) Voltar")

        option = input("\nOpção: ")
        try:
            option = int(option)
        except:
            pass
        if option in range(1,self.n_graphs+1):
            self.graph_id = option-1
            self.state = 3
        elif option == 'V' or option == 'v':
            self.state = 0
        else:
            self.state = 2

    #state 3
    def one_graph_menu(self):
        g = self.graphs[self.graph_id]
        print("Grafo "+str(self.graph_id+1)+"\n")
        print("Tipo: "+("Direcionado" if g.direc else "Não direcionado"))
        
        print("\nVértices:\n")
        for v in g.get_vertices():
            print(v)
        
        print("\nArestas:\n")
        
        egs = []

        if not g.direc:
            for w,u,v in g.get_edges():
                if (w,u,v) not in egs and (w,v,u) not in egs:
                    egs.append((w,u,v))
        else:
            egs = g.get_edges()
        
        sep = " → " if g.direc else " – "
        for w,u,v in egs:
            print(str(u)+sep+str(v)+": "+str(w))
        
        print("\n1) Novo vértice")
        print("2) Nova aresta")
        print("3) Remover vértice")
        print("4) Remover Aresta")
        print("5) Algoritmos")
        print("\nE) Excluir grafo")
        print("V) Voltar")

        option = input("\nOpção: ")
        if option == "1":
            try:
                nome = input("Nome do vértice (ou Enter para um vértice sem nome):")
                try:
                    nome = int(nome)
                except: pass
                g.create_vertex(nome)
            except Exception as e:
                print("")
                print(e)
                input("\nPressione Enter para continuar")

        elif option == "2":
            try:
                u = input("Vértice inicial: ")
                v = input("Vértice final: ")
                w = input("Peso (ou Enter para uma aresta sem peso): ")
                
                try:
                    u = int(u)
                except: pass
                try:
                    v = int(v)
                except: pass
                try:
                    w = float(w) if w != "" else 1
                except:
                    w = 1
                g.create_edge(u,v,w)
            except Exception as e:
                print("")
                print(e)
                input("\nPressione Enter para continuar")

        elif option == "3":
            nome = input("Nome do vértice:")
            try:
                nome = int(nome)
            except: pass
            g.del_vertex(nome)

        elif option == "4":
            u = input("Vértice inicial: ")
            v = input("Vértice final: ")
            try:
                u = int(u)
            except: pass
            try:
                v = int(v)
            except: pass
            g.del_edge(u,v)
        
        elif option == "5":
            self.state = 4
        
        elif option == "E" or option == "e":
            cert = input("Tem certeza de que deseja deletar o grafo atual? (s/n): ")
            if cert == "S" or cert == "s":
                self.graphs.pop(self.graph_id)
                self.n_graphs -= 1
                self.graph_id = 0
                self.state = 2
        
        elif option == "V" or option == "v":
            self.state = 2
        
        else:
            self.state = 3
        
    #state 4
    def actions_menu(self):
        print("Algoritmos\n")
        print("1)É fortemente conectado?")
        print("2) É bipartido?")
        print("3) Possui Ciclos?")
        print("4) Número de componentes conexos")
        print("5) BFS")
        print("6) DFS")
        print("7) Ordenação topológica")
        print("8) Caminhos mínimos")
        print("9) Árvore Geradora Mínima")
        print("10) Árvore de grau máximo")
        print("V) Voltar")

        option = input("\nOpção: ")
        try:
            option = int(option)
        except:
            pass
        if option in range(1,11):
            self.action = option
            self.state = 5
        elif option == 'V' or option == 'v':
            self.state = 3
        else:
            self.state = 4
        
    #state 5
    def one_action_menu(self):
        g = self.graphs[self.graph_id]
        if self.action == 1:
            print("É fortemente conectado?\n")
            try:
                print("Sim" if g.is_strongly_connected() else "Não")
            except Exception as e:
                print(e)
        
        elif self.action == 2:
            print("É bipartido?\n")
            print("Sim" if g.is_bipartite() else "Não")

        elif self.action == 3:
            print("Possui ciclos?\n")
            print("Sim" if g.has_cycle() else "Não")
        
        elif self.action == 4:
            print("Número de componentes conexos\n")
            print(g.components())
        
        elif self.action == 5:
            print("BFS\n")
            ini = input("Vértice inicial: ")
            try:
                ini = int(ini)
            except: pass
            
            try:
                vs = g.bfs(ini)
                print(*vs)
            except Exception as e:
                print(e)
            
        
        elif self.action == 6:
            print("DFS\n")
            ini = input("Vértice inicial: ")
            try:
                ini = int(ini)
            except: pass
            try:
                vs = g.dfs(ini)
                print(*vs)
            except Exception as e:
                print(e)
            
        
        elif self.action == 7:
            print("Ordenação topológica\n")
            try:
                vs = g.toposort()
                print(*vs)
            except Exception as e:
                print(e)
            
        
        elif self.action == 8:
            print("Caminhos mínimos\n")
            ini = input("Vértice inicial: ")
            try:
                ini = int(ini)
            except: pass
            try:
                d = g.dijkstra(ini)
                print("Distâncias mínimas a cada vértice a partir do inicial"+str(ini)+":")
                for v,w in d:
                    print(str(ini)+"→ "+str(v)+": "+str(w))
            except Exception as e:
                print(e)
            
        
        elif self.action == 9:
            print("Árvore geradora mínima\n")
            try:
                mst = g.MST()
                self.graphs.append(mst)
                self.n_graphs+=1
                print("O grafo resultante foi adicionado à lista de grafos")
            except Exception as e:
                print(e)
        
        elif self.action == 10:
            print("Árvore de grau máximo\n")
            tf = g.treefy()
            self.graphs.append(tf)
            self.n_graphs+=1
            print("O grafo resultante foi adicionado à lista de grafos")
        
        input("\nPressione Enter para voltar")
        self.state = 4
            
if __name__ == '__main__':
    m = Menu()
    m.main()        


        


