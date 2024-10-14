class ValidadorSenhas:
    def validar(self, senha, confirmar_senha):
        if senha != confirmar_senha:
            return "As senhas não coincidem"
        return None
