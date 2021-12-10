import unittest
import os
import filecmp

import warnings
warnings.filterwarnings("ignore")

class TestMenu(unittest.TestCase):
    #Fixture do teste
    def setUp(self):
        self.input = open("input", "w")
    
    def tearDown(self):
        pass
#         os.remove("input")
#         os.remove("output")
        
    #Funções auxiliares, para evitar repetição de código
    def createDirectedGraph(self):
        self.input.write("1\n")
        self.input.write("1\n")
        self.input.write("V\n")
        self.input.write("V\n")
    
    def createUndirectedGraph(self):
        self.input.write("1\n")
        self.input.write("2\n")
        self.input.write("V\n")
        self.input.write("V\n")
        
    def createVertex(self, graphIndex):
        self.input.write("2\n")
        self.input.write(str(graphIndex)+"\n")
        self.input.write("1\n")
        self.input.write("\n") #<- Create vertex without name
        self.input.write("V\n")
        self.input.write("V\n")
        
    def createEdge(self, graphIndex, v1, v2):
        self.input.write("2\n")
        self.input.write(str(graphIndex)+"\n")
        self.input.write("2\n")
        self.input.write(str(v1)+"\n")
        self.input.write(str(v2)+"\n")
        self.input.write("V\n")
        self.input.write("V\n")
    
    #----------------------------------- Métodos de Teste -----------------------------------------
    
    def testListGraphMenu(self):
        self.createDirectedGraph()
        self.input.write("2\n")
        self.assertTrue(True)
        os.system("python Menu.py < input > output")
        os.system("clear")

        self.assertTrue(filecmp.cmp("expected_outputs/test1.out",\
                                    'output'))
        
    def testGraphOptionsMenu(self):
        self.createDirectedGraph()
#         self.input.write("2\n")
        self.input.write("1\n")
        os.system("python Menu.py < input > output")
        os.system("clear")
        
        self.assertTrue(filecmp.cmp("expected_outputs/test2.out",\
                                    'output'))
        
        
    
if __name__ == '__main__':
    unittest.main()