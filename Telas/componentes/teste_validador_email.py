import unittest
from validar_email import ValidadorEmail

class TestValidadorEmail(unittest.TestCase):

    def test_email_valido(self):
        self.assertIsNone(ValidadorEmail.validar("usuario@dominio.com"))

    def test_email_invalido_sem_arroba(self):
        self.assertEqual(ValidadorEmail.validar("usuariodominio.com"), "E-mail inválido")

    def test_email_invalido_sem_dominio(self):
        self.assertEqual(ValidadorEmail.validar("usuario@dominio"), "E-mail inválido")

    def test_email_invalido_caracteres_especiais(self):
        self.assertEqual(ValidadorEmail.validar("usuario@dominio!com"), "E-mail inválido")

if __name__ == "__main__":
    unittest.main()
