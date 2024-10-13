import re

class ValidadorEmail:
    @staticmethod
    def validar(email):
        padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(padrao, email):
            return "E-mail inválido"
        return None
