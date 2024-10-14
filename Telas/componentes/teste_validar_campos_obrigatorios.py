import unittest
from validar_campos_obrigatorios import ValidadorCamposObrigatorios

class TestValidadorCamposObrigatorios(unittest.TestCase):
    def setUp(self):
        self.validador = ValidadorCamposObrigatorios()

    def test_campos_preenchidos(self):
        resultado = self.validador.validar("jose marcos", "email@example.com", "senha123", "senha123")
        self.assertIsNone(resultado)

    def test_campos_vazios(self):
        resultado = self.validador.validar("", "email@example.com", "senha123", "senha123")
        self.assertEqual(resultado, "Preencha todos os campos")
        
if __name__ == "__main__":
    unittest.main()