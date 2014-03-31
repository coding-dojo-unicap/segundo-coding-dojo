# coding: utf-8

import unittest

from spock import resultado


class Test(unittest.TestCase):
    #def test(self):
    #    self.assertEqual(  nome_funcao  ,  retorno   )
    
    def test_spock(self):
        self.assertEqual(resultado("Pedra", "Pedra"), 0)
    def test_pedra_papel(self):
        self.assertEqual(resultado("Pedra", "Papel"), 2)
    def test_pedra_tesoura(self):
        self.assertEqual(resultado("Pedra", "Tesoura"), 1)
    def test_pedra_spock(self):
        self.assertEqual(resultado("Pedra", "Spock"), 2 )
    def teste_pedra_Largato(self):
        self.assertEqual(resultado("Pedra", "Largato"), 1)
    def test_papel_tesoura(self):
        self.assertEqual(resultado("Papel", "Tesoura"), 2)
    def test_papel_spock(self):
        self.assertEqual(resultado("Papel", "Spock"),1)
    def test_papel_lagarto(self):
        self.assertEqual(resultado("Papel", "Lagarto"),2)
    def test_papel_papel(self):
        self.assertEqual(resultado("Papel", "Papel"),0)
    def test_tesoura_papel(self):
        self.assertEqual(resultado("Tesoura","Papel"),1)
    

if __name__ == '__main__':
    unittest.main()
