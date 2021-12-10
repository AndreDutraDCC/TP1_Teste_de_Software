import unittest
import io
import sys
from Menu import Menu
#import subprocess

#ret = subprocess.run("python3 test_Menu.py<input.txt", capture_output = True, shell = True)
#output = ret.stdout.decode()


class testMenu(unittest.TestCase):
    def setUp(self):
        self.menu = Menu()
        #output = io.StringIO()
        #sys.stdout = output

    def testState0Interface(self):
        output = io.StringIO()
        sys.stdout = output
        sys.stdin = io.StringIO('X')
        self.menu.main()
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__
        self.assertEqual('\nGraph API\n\n1) Novo Grafo\n2) Grafos Existentes\nX) Sair\n\nOpção: \n', output.getvalue())

    #def testCreateVertex(self):






if __name__ == '__main__':
    unittest.main()