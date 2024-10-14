class ValidadorCamposObrigatorios:
    def validar(self, usuario, email, senha, confirmar_senha):
        if not usuario or not email or not senha or not confirmar_senha:
            return "Preencha todos os campos"
        return None
