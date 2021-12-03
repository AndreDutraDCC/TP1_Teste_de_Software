import unittest
from Graph_API import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.grafo = Graph()

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
        self.assertEqual(self.grafo.get_weight(0,1),2)

    def testRaiseExceptionIfCreateEdgeByNonExistentVertex(self):
        self.grafo.create_vertex()
        self.grafo.create_vertex()
        self.assertRaises(Exception,self.grafo.create_edge,1,2)

    def testCreateDeleteEdges(self):
        self.grafo.create_vertex()
        self.grafo.create_vertex()
        self.grafo.create_edge(0,1)
        self.grafo.del_edge(0,1)
        self.assertFalse(self.grafo.has_edge(0,1))

    def testRaiseExceptionIfGetWeightFromNonExistentEdge(self):
        self.grafo.create_vertex()
        self.grafo.create_vertex()
        self.assertRaises(Exception,self.grafo.get_weight,0,1)

    #Métodos de teste do DFS
    def testDfsOnUndirectedTree(self):
        pass

    def testDfsOnUndirectedGraphWithCycles(self):
        pass

    def testDfsOnUndirectedDisconnectedGraph(self):
        pass

    def testDfsOnDirectedTree(self):
        pass

    def testDfsOnDirectedGraphWithCycles(self):
        pass

    def testDfsOnDirectedDisconnectedGraph(self):
        pass

    def testDfsRaiseExceptionIfStartVertexDoesntExist(self):
        pass

    #Métodos de teste do BFS
    def testBfsOnUndirectedTree(self):
        pass

    def testBfsOnUndirectedGraphWithCycles(self):
        pass

    def testBfsOnUndirectedDisconnectedGraph(self):
        pass

    def testBfsOnDirectedTree(self):
        pass

    def testBfsOnDirectedGraphWithCycles(self):
        pass

    def testBfsOnDirectedDisconnectedGraph(self):
        pass

    def testBfsRaiseExceptionIfStartVertexDoesntExist(self):
        pass

    #Métodos de teste do Dijkstra
    def testDijkstraOnUndirectedTree(self):
        pass

    def testDijkstraOnUndirectedGraphWithCycles(self):
        pass

    def testDijkstraOnUndirectedDisconnectedGraph(self):
        pass

    def testDijkstraOnDirectedTree(self):
        pass

    def testDijkstraOnDirectedGraphWithCycles(self):
        pass

    def testDijkstraOnDirectedDisconnectedGraph(self):
        pass

    def testDijkstraRaiseExceptionIfStartVertexDoesntExist(self):
        pass

    #Métodos de teste da MST
    def testMSTOnUndirectedTree(self):
        pass

    def testMSTOnUndirectedGraphWithCycles(self):
        pass

    def testMSTOnUndirectedDisconnectedGraph(self):
        pass

    def testRaiseExceptionIfMSTIsCalledForDirectedGraph(self):
        pass

    #Métodos de teste do Treefy

    def testTreefyOnUndirectedTree(self):
        pass

    def testTreefyOnUndirectedGraphWithCycles(self):
        pass

    def testTreefyOnUndirectedDisconnectedGraph(self):
        pass

    def testTreefyOnDirectedTree(self):
        pass

    def testTreefyOnDirectedGraphWithCycles(self):
        pass

    def testTreefyOnDirectedDisconnectedGraph(self):
        pass

    #def testTreefyRaiseExceptionIfStartVertexDoesntExist(self):
    #    pass

    #Métodos de teste para o algoritmo de ciclos

    def testUndirectedTreeDoesntHaveCycle(self):
        pass

    def testUndirectedGraphWithCyclesHasCycle(self):
        pass

    def testUndirectedDisconnectedGraphHasCycle(self):
        pass

    def testDirectedTreeDoesntHaveCycle(self):
        pass

    def testDirectedGraphWithCyclesHasCycle(self):
        pass

    def testDirectedDisconnectedGraphHasCycles(self):
        pass

    #Métodos de teste para o algoritmo de componentes

    def testUndirectedTreeHasOneComponent(self):
        pass

    def testUndirectedGraphWithCyclesHasOneComponent(self):
        pass

    def testUndirectedDisconnectedGraphHasManyComponents(self):
        pass

    def testDirectedTreeDoesntHasOneComponent(self):
        pass

    def testDirectedGraphWithCyclesHasManyComponents(self):
        pass

    def testDirectedDisconnectedGraphHasManyComponents(self):
        pass

    


    

        


    #fim da classe


if __name__ == '__main__':
    unittest.main()
