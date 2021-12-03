import unittest
from Graph_API import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.grafo = Graph()

    #Vertex related test methods
    def testCreateOneVertexWithLabel(self):
        self.assertEqual(self.grafo.create_vertex("a"),"a")
        self.assertTrue(self.grafo.has_vertex("a"))
    
    def testCreateNamelessVertex(self):
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
    
    #Edge related test methods
    def testCreateWeightedEdge(self):
        self.grafo.create_vertex()
        self.grafo.create_vertex()
        self.grafo.create_edge(0,1,2)
        self.assertEqual(self.grafo.get_weight(0,1),2)

    def testRaiseExceptionIfCreateEdgeByNonExistentVertex(self):
        pass

    def testCreateDeleteEdges(self):
        pass

    def testRaiseExceptionIfGetWeightFromNonExistentEdge(self):
        pass

    #DFS test methods
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

    #BFS test methods
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

    #Dijkstra test methods
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

    #MST test methods
    def testMSTOnUndirectedTree(self):
        pass

    def testMSTOnUndirectedGraphWithCycles(self):
        pass

    def testMSTOnUndirectedDisconnectedGraph(self):
        pass




    


    

        


    #fim da classe


if __name__ == '__main__':
    unittest.main()
