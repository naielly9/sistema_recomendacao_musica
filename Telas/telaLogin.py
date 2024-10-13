import flet as ft
from database import Database
from .telaPrincipal import TelaPrincipal
from .telaCadastro import TelaCadastro
from .telaBase import TelaBase
from .componentes.campoTexto import CampoTexto
from .componentes.identidadeVisual import GRADIENTE, exibir_logo, ALINHAMENTO_COLUNA, ALINHAMENTO_LINHA
from .componentes.botao import Botao, BotaoTexto

class TelaLogin(TelaBase):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        self.db = Database()
        self.page.snack_bar = ft.SnackBar(content=ft.Text(""))
        
    def ao_clicar_login(self, e):
        username = self.username_field.value
        senha = self.password_field.value
        
        user = self.db.validate_user(username, senha)
        if user:
            username, email = user[1], user[2]
            self.page.clean()
        
            principal_screen = TelaPrincipal(self.page, username, email)
            principal_screen.mostrar()
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("Usuário ou senha inválidos"), open=True)
            self.page.update()

    def ao_clicar_registro(self, e):
        # Ir para a próxima página
        self.page.clean()
        tela_cadastro = TelaCadastro(self.page)
        tela_cadastro.mostrar()
        
    def mostrar(self):
        self.page.title = "listen"
        self.username_field = CampoTexto("Username")
        self.password_field = CampoTexto("Senha", senha=True)

        logo = exibir_logo(self.page.window_width)  # Certifique-se de chamar a função

        conteudo_login = ft.Container(
            expand=True,
            gradient=GRADIENTE,
            content=ft.Column(
                [
                    ft.Row(
                        [
                            logo
                        ],
                        **ALINHAMENTO_LINHA
                    ),
                    ft.Container(height=20),  # Espaço entre a logo e os campos
                    self.username_field,
                    self.password_field,
                    Botao("Login", self.ao_clicar_login, primario=True),
                    BotaoTexto("Não tem cadastro? Cadastre-se", self.ao_clicar_registro)
                ],
                **ALINHAMENTO_COLUNA
            )
        )

        self.page.add(conteudo_login)
        
