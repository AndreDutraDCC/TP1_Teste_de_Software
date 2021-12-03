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
        self.assertRaises(Exception,self.grafo.get_weight,2,0)

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

    def testDijkstraOnUndirectedGraphWithCycles(self):
        self.createUndirectedGraphWithCycles()

    def testDijkstraOnUndirectedDisconnectedGraph(self):
        self.createUndirectedDisconnectedGraph()

    def testDijkstraOnDirectedTree(self):
        self.createDirectedTree()

    def testDijkstraOnDirectedGraphWithCycles(self):
        self.createDirectedGraphWithCycles()

    def testDijkstraOnDirectedDisconnectedGraph(self):
        self.createDirectedDisconnectedGraph()

    def testDijkstraRaiseExceptionIfStartVertexDoesntExist(self):
        pass

    #Métodos de teste da MST
    def testMSTOnUndirectedTree(self):
        self.createUndirectedTree()

    def testMSTOnUndirectedGraphWithCycles(self):
        self.createUndirectedGraphWithCycles()

    def testMSTOnUndirectedDisconnectedGraph(self):
        self.createUndirectedDisconnectedGraph()

    def testRaiseExceptionIfMSTIsCalledForDirectedGraph(self):
        pass

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
