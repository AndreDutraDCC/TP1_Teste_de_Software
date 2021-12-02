import unittest
from Graph_API import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.grafo = Graph()
    
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
    
    
        


    #fim da classe


if __name__ == '__main__':
    unittest.main()