import unittest
from Graph_API import Graph

class TestGraph(unittest.TestCase):
    #Fixture do teste
    def setUp(self):
        self.grafo = Graph()
        self.grafo_d = Graph(directed=True)
    
    #Funções auxiliares, para evitar repetição de código
    def createUndirectedTree(self):
        self.grafo.create_vertex()
        self.grafo.create_vertex()
        self.grafo.create_vertex()
        self.grafo.create_vertex()
        self.grafo.create_vertex()
        
        self.grafo.create_edge(0,1,3)
        self.grafo.create_edge(1,3,5)
        self.grafo.create_edge(1,2,4)
        self.grafo.create_edge(2,4,1)

    def createUndirectedGraphWithCycles(self):
        self.grafo.create_vertex()
        self.grafo.create_vertex()
        self.grafo.create_vertex()
        self.grafo.create_vertex()
        
        self.grafo.create_edge(0,1,4)
        self.grafo.create_edge(0,3,10)
        self.grafo.create_edge(1,2,3)
        self.grafo.create_edge(2,0,5)
        self.grafo.create_edge(2,3,7)

    def createUndirectedDisconnectedGraph(self):
        self.grafo.create_vertex()
        self.grafo.create_vertex()
        self.grafo.create_vertex()
        self.grafo.create_vertex()
        self.grafo.create_vertex()
        
        self.grafo.create_edge(0,2,13)
        self.grafo.create_edge(2,1,2)
        self.grafo.create_edge(1,0,12)
        self.grafo.create_edge(4,3,8)

    def createDirectedTree(self):
        self.grafo_d.create_vertex()
        self.grafo_d.create_vertex()
        self.grafo_d.create_vertex()
        self.grafo_d.create_vertex()
        self.grafo_d.create_vertex()
        
        self.grafo_d.create_edge(0,1,3)
        self.grafo_d.create_edge(1,3,5)
        self.grafo_d.create_edge(1,2,4)
        self.grafo_d.create_edge(2,4,1)

    def createDirectedGraphWithCycles(self):
        self.grafo_d.create_vertex()
        self.grafo_d.create_vertex()
        self.grafo_d.create_vertex()
        self.grafo_d.create_vertex()
        
        self.grafo_d.create_edge(0,1,4)
        self.grafo_d.create_edge(0,3,10)
        self.grafo_d.create_edge(1,2,3)
        self.grafo_d.create_edge(2,0,5)
        self.grafo_d.create_edge(2,3,7)
        self.grafo_d.create_edge(3,2,7)

    def createDirectedDisconnectedGraph(self):
        self.grafo_d.create_vertex()
        self.grafo_d.create_vertex()
        self.grafo_d.create_vertex()
        self.grafo_d.create_vertex()
        self.grafo_d.create_vertex()
        
        self.grafo_d.create_edge(0,2,13)
        self.grafo_d.create_edge(2,1,2)
        self.grafo_d.create_edge(1,0,12)
        self.grafo_d.create_edge(4,3,8)
    
    #----------------------------------- Métodos de Teste -----------------------------------------
    
    #Métodos de teste relacionados a vértices
    def testCreateOneVertexWithLabel(self):
        self.assertEqual(self.grafo.create_vertex("a"),"a")
        self.assertTrue(self.grafo.has_vertex("a"))
    
    def testCreateLabellessVertex(self):
        self.assertEqual(self.grafo.create_vertex(),0)
        self.assertTrue(self.grafo.has_vertex(0))
        
    def testCreateMultipleVertices(self):
        self.grafo.create_vertex(55)
        self.grafo.create_vertex()
        self.grafo.create_vertex("a")

        self.assertTrue(55 in self.grafo.get_vertices())
        self.assertTrue(56 in self.grafo.get_vertices())
        self.assertTrue("a" in self.grafo.get_vertices())
    
    def testRaiseExceptionWhenVertexLabelAlreadyExists(self):
        self.grafo.create_vertex("a")
        self.assertRaises(Exception,self.grafo.create_vertex,"a")
    
    def testCreateDeleteVertices(self):
        self.grafo.create_vertex()
        self.grafo.create_vertex()
        self.grafo.del_vertex(0)
        self.grafo.create_vertex(7)

        self.assertTrue(self.grafo.has_vertex(1))
        self.assertTrue(self.grafo.has_vertex(7))
        self.assertFalse(self.grafo.has_vertex(0))
    
    #Métodos de teste relacionados a arestas
    def testCreateWeightedEdge(self):
        self.grafo.create_vertex()
        self.grafo.create_vertex()
        self.grafo.create_edge(0,1,2)
        self.assertTrue(self.grafo.has_edge(0,1))
        self.assertTrue(self.grafo.has_edge(1,0))
        self.assertEqual(self.grafo.get_weight(0,1),2)
    
    def testCreateDirectedWeightedEdge(self):
        self.grafo_d.create_vertex()
        self.grafo_d.create_vertex()
        self.grafo_d.create_edge(0,1,2)
        self.assertTrue(self.grafo_d.has_edge(0,1))
        self.assertFalse(self.grafo_d.has_edge(1,0))
        self.assertEqual(self.grafo_d.get_weight(0,1),2)

    def testRaiseExceptionIfCreateEdgeByNonExistentVertex(self):
        self.grafo.create_vertex()
        self.grafo.create_vertex()

        self.assertRaises(Exception,self.grafo.create_edge,1,2,5)
        self.assertRaises(Exception,self.grafo.create_edge,3,0,10)

    def testCreateDeleteEdges(self):
        self.grafo_d.create_vertex()
        self.grafo_d.create_vertex()
        self.grafo_d.create_vertex()

        self.grafo_d.create_edge(0,1,3)
        self.grafo_d.create_edge(1,0,5)
        self.grafo_d.create_edge(0,2,10)
        self.grafo_d.del_edge(0,1)
        self.grafo_d.create_edge(0,1,2)
        self.grafo_d.del_edge(0,2)

        self.assertTrue(self.grafo_d.has_edge(0,1))
        self.assertTrue(self.grafo_d.has_edge(1,0))
        self.assertFalse(self.grafo_d.has_edge(0,2))
        self.assertEqual(self.grafo_d.get_weight(0,1),2)        

    def testRaiseExceptionIfGetWeightFromNonExistentEdge(self):
        self.assertRaises(Exception,self.grafo.get_weight,0,1)
        self.grafo.create_vertex()
        self.grafo.create_vertex()
        self.assertRaises(Exception,self.grafo.get_weight,0,1)


    #Métodos de teste do DFS
    def testDfsOnUndirectedTree(self):
        self.createUndirectedTree()

    def testDfsOnUndirectedGraphWithCycles(self):
        self.createUndirectedGraphWithCycles()

    def testDfsOnUndirectedDisconnectedGraph(self):
        self.createUndirectedDisconnectedGraph()

    def testDfsOnDirectedTree(self):
        self.createDirectedTree()

    def testDfsOnDirectedGraphWithCycles(self):
        self.createDirectedGraphWithCycles()

    def testDfsOnDirectedDisconnectedGraph(self):
        self.createDirectedDisconnectedGraph()

    def testDfsRaiseExceptionIfStartVertexDoesntExist(self):
        pass

    #Métodos de teste do BFS
    def testBfsOnUndirectedTree(self):
        self.createUndirectedTree()

    def testBfsOnUndirectedGraphWithCycles(self):
        self.createUndirectedGraphWithCycles()

    def testBfsOnUndirectedDisconnectedGraph(self):
        self.createUndirectedDisconnectedGraph()

    def testBfsOnDirectedTree(self):
        self.createDirectedTree()

    def testBfsOnDirectedGraphWithCycles(self):
        self.createDirectedGraphWithCycles()

    def testBfsOnDirectedDisconnectedGraph(self):
        self.createDirectedDisconnectedGraph()

    def testBfsRaiseExceptionIfStartVertexDoesntExist(self):
        pass

    #Métodos de teste do Dijkstra
    def testDijkstraOnUndirectedTree(self):
        self.createUndirectedTree()
        self.assertEqual(self.grafo.dijkstra(0), {0:0, 1:3, 2:7, 3:8, 4:8})

    def testDijkstraOnUndirectedGraphWithCycles(self):
        self.createUndirectedGraphWithCycles()
        self.assertEqual(self.grafo.dijkstra(0), {0:0, 1:4, 2:5, 3:10})

    def testDijkstraOnUndirectedDisconnectedGraph(self):
        self.createUndirectedDisconnectedGraph()
        self.assertEqual(self.grafo.dijkstra(0), {0:0, 1:12, 2:13, 3:float('inf'), 4:float('inf')})

    def testDijkstraOnDirectedTree(self):
        self.createDirectedTree()
        self.assertEqual(self.grafo_d.dijkstra(0), {0:0, 1:3, 2:7, 3:8, 4:8})

    def testDijkstraOnDirectedGraphWithCycles(self):
        self.createDirectedGraphWithCycles()
        self.assertEqual(self.grafo_d.dijkstra(0), {0:0, 1:4, 2:7, 3:10})

    def testDijkstraOnDirectedDisconnectedGraph(self):
        self.createDirectedDisconnectedGraph()
        self.assertEqual(self.grafo_d.dijkstra(0), {0:0, 1:15, 2:13, 3:float('inf'), 4:float('inf')})

    def testDijkstraRaiseExceptionIfStartVertexDoesntExist(self):
        self.createUndirectedTree()
        self.assertRaises(Exception,self.grafo.dijkstra,5)

    #Métodos de teste da MST
    def testMSTOnUndirectedTree(self):
        self.createUndirectedTree()
        mst = self.grafo.MST()
        self.assertEqual(set(mst.get_vertices()),{0,1,2,3,4})
        self.assertEqual(set(mst.get_edges()),{(3,0,1), (3,1,0), (4,1,2), (4,2,1), (5,1,3), (5,3,1), (1,2,4), (1,4,2)})

    def testMSTOnUndirectedGraphWithCycles(self):
        self.createUndirectedGraphWithCycles()
        mst = self.grafo.MST()
        self.assertEqual(set(mst.get_vertices()),{0,1,2,3})
        self.assertEqual(set(mst.get_edges()),{(4,0,1), (4,1,0), (3,1,2), (3,2,1), (7,2,3), (7,3,2)})

    def testMSTOnUndirectedDisconnectedGraph(self):
        self.createUndirectedDisconnectedGraph()
        mst = self.grafo.MST()
        self.assertEqual(set(mst.get_vertices()),{0,1,2,3,4})
        self.assertEqual(set(mst.get_edges()),{(12,0,1), (12,1,0), (2,1,2), (2,2,1), (8,3, 4), (8,4,3)})

    def testRaiseExceptionIfMSTIsCalledForDirectedGraph(self):
        self.createDirectedTree()
        self.assertRaises(Exception,self.grafo_d.MST)

    #Métodos de teste do Treefy

    def testTreefyOnUndirectedTree(self):
        self.createUndirectedTree()

    def testTreefyOnUndirectedGraphWithCycles(self):
        self.createUndirectedGraphWithCycles()

    def testTreefyOnUndirectedDisconnectedGraph(self):
        self.createUndirectedDisconnectedGraph()

    def testTreefyOnDirectedTree(self):
        self.createDirectedTree()

    def testTreefyOnDirectedGraphWithCycles(self):
        self.createDirectedGraphWithCycles()

    def testTreefyOnDirectedDisconnectedGraph(self):
        self.createDirectedDisconnectedGraph()

    #def testTreefyRaiseExceptionIfStartVertexDoesntExist(self):
    #    pass

    #Métodos de teste para o algoritmo de ciclos

    def testUndirectedTreeDoesntHaveCycle(self):
        self.createUndirectedTree()

    def testUndirectedGraphWithCyclesHasCycle(self):
        self.createUndirectedGraphWithCycles()

    def testUndirectedDisconnectedGraphHasCycle(self):
        self.createUndirectedDisconnectedGraph()

    def testDirectedTreeDoesntHaveCycle(self):
        self.createDirectedTree()

    def testDirectedGraphWithCyclesHasCycle(self):
        self.createDirectedGraphWithCycles()

    def testDirectedDisconnectedGraphHasCycles(self):
        self.createDirectedDisconnectedGraph()

    #Métodos de teste para o algoritmo de componentes

    def testUndirectedTreeHasOneComponent(self):
        self.createUndirectedTree()

    def testUndirectedGraphWithCyclesHasOneComponent(self):
        self.createUndirectedGraphWithCycles()

    def testUndirectedDisconnectedGraphHasTwoComponents(self):
        self.createUndirectedDisconnectedGraph()

    def testDirectedTreeDoesntHasFiveComponents(self):
        self.createDirectedTree()

    def testDirectedGraphWithCyclesHasOneComponent(self):
        self.createDirectedGraphWithCycles()

    def testDirectedDisconnectedGraphHasThreeComponents(self):
        self.createDirectedDisconnectedGraph()

    


    

        


    #fim da classe


if __name__ == '__main__':
    unittest.main()
