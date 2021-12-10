import unittest
from os import name,remove#,system
import subprocess

def clear():
    if name == 'nt':
        subprocess.run("cls",shell = True)
    else:
        subprocess.run("clear",shell = True)

import warnings
warnings.filterwarnings("ignore")

class TestMenu(unittest.TestCase):
    #Fixture do teste
    def setUp(self):
        self.input = open("input", "w")
        
    def tearDown(self):
        remove("input")
        remove("output")
        
    def inputClose(self):
        self.input.close()
        
    def isEqualFiles(self, path1, path2):
        with open(path1, "r") as f1, open(path2, "r") as f2:
            return f1.read() == f2.read()
    
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
        self.inputClose()
        
        subprocess.run("python Menu.py < input > output",shell = True)
        clear()
        
        self.assertTrue(self.isEqualFiles("expected_outputs/test1.out",'output'))
        
    def testGraphOptionsMenu(self):
        self.createUndirectedGraph()
        self.input.write("2\n")
        self.input.write("1\n")
        self.inputClose()
        
        subprocess.run("python Menu.py < input > output",shell = True)
        clear()
        self.assertTrue(self.isEqualFiles("expected_outputs/test2.out",'output'))
        
    def testDFS(self):
        self.createUndirectedGraph()
        self.createVertex("1")
        self.createVertex("1")
        self.input.write("2\n")
        self.input.write("1\n")
        self.input.write("5\n")
        self.input.write("6\n")
        self.input.write("0\n")
        self.inputClose()
        
        subprocess.run("python Menu.py < input > output",shell = True)
        clear()
        self.assertTrue(self.isEqualFiles("expected_outputs/test3.out",'output'))
        
    def testBFS(self):
        self.createUndirectedGraph()
        self.createVertex("1")
        self.createVertex("1")
        self.input.write("2\n")
        self.input.write("1\n")
        self.input.write("5\n")
        self.input.write("5\n")
        self.input.write("0\n")
        self.inputClose()
        
        subprocess.run("python Menu.py < input > output",shell = True)
        clear()
        self.assertTrue(self.isEqualFiles("expected_outputs/test4.out",'output'))
        
    def testConnectedComponents(self):
        self.createUndirectedGraph()
        self.createVertex("1")
        self.createVertex("1")
        self.input.write("2\n")
        self.input.write("1\n")
        self.input.write("5\n")
        self.input.write("4\n")
        self.inputClose()
        
        subprocess.run("python Menu.py < input > output",shell = True)
        clear()
        self.assertTrue(self.isEqualFiles("expected_outputs/test5.out",'output'))
        
        
    
if __name__ == '__main__':
    unittest.main()