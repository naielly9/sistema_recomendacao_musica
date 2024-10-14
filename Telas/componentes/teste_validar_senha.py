import unittest
from validar_senha import ValidadorSenhas

class TestValidadorSenhas(unittest.TestCase):
    def setUp(self):
        self.validador = ValidadorSenhas()

    def test_senhas_iguais(self):
        resultado = self.validador.validar("senha123", "senha123")
        self.assertIsNone(resultado)

    def test_senhas_diferentes(self):
        resultado = self.validador.validar("senha123", "senha456")
        self.assertEqual(resultado, "As senhas não coincidem")

if __name__ == "__main__":
    unittest.main()