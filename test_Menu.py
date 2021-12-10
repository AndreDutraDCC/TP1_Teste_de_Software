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
        os.remove("input")
#         os.remove("output")
        
    def inputClose(self):
        self.input.close()
        
    def isEqualFiles(self, path1, path2):
        # reading files
        f1 = open(path1, "r")  
        f2 = open(path2, "r")  

        for line1 in f1:
            for line2 in f2:
                if line1 == line2:  
                    break
                else:
                    print("AQUI O ERRO\n\n")
                    print(line1)
                    print(line2)
                    print("\n\n\n")
                    return False
        
        # closing files
        f1.close()                                       
        f2.close()      
        
        return True
    
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
        
        os.system("python Menu.py < input > output")
#         os.system("clear")

        self.assertTrue(self.isEqualFiles(
            "expected_outputs/test1.out",\
                                    'output'))
        
    def testGraphOptionsMenu(self):
        self.createUndirectedGraph()
        self.input.write("2\n")
        self.input.write("1\n")
        self.inputClose()
        
        os.system("python Menu.py < input > output")
#         os.system("clear")
        self.assertTrue(self.isEqualFiles(\
                        "expected_outputs/test2.out",\
                                    'output'))
        
        
    
if __name__ == '__main__':
    unittest.main()