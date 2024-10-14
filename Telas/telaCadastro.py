import flet as ft
import re
from database import Database
from .componentes.campoTexto import CampoTexto
from .componentes.botao import Botao, BotaoTexto
from .telaBase import TelaBase
from .componentes.identidadeVisual import GRADIENTE, exibir_logo
from .componentes.validar_email import ValidadorEmail
from .componentes.validar_campos_obrigatorios import ValidadorCamposObrigatorios
from .componentes.validar_senha import ValidadorSenhas

class TelaCadastro(TelaBase):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        self.db = Database()

    def validar_email(self, email):
        return ValidadorEmail.validar(email)

    def validar_campos_obrigatorios(self, usuario, email, senha, confirmar_senha):
        return ValidadorCamposObrigatorios.validar(usuario, email, senha, confirmar_senha)

    def validar_senhas(self, senha, confirmar_senha):
        return ValidadorSenhas.validar(senha, confirmar_senha)
    
    def ao_clicar_registrar(self, e):
        usuario = self.campo_usuario.value
        email = self.campo_email.value
        senha = self.campo_senha.value
        confirmar_senha = self.campo_confirmar_senha.value

        erro = self.validar_campos_obrigatorios(usuario, email, senha, confirmar_senha) or \
               self.validar_email(email) or \
               self.validar_senhas(senha, confirmar_senha)
    
        if erro:
            self.page.snack_bar = ft.SnackBar(ft.Text(erro), open=True)
        else:
            self.db.add_user(usuario, email, senha)
            self.page.snack_bar = ft.SnackBar(ft.Text("Cadastrado com sucesso!"), open=True)
            # Transição para a tela de login
            self.page.clean()
            from .telaLogin import TelaLogin 
            login_screen = TelaLogin(self.page)
            login_screen.show()

        self.page.update()

    def ao_clicar_voltar(self, e):
        self.page.clean()
        from .telaLogin import TelaLogin  
        login_screen = TelaLogin(self.page)
        login_screen.mostrar()

    def mostrar(self):
        self.page.title = "listen"
        self.campo_usuario = CampoTexto("Usuário")
        self.campo_email = CampoTexto("E-mail")
        self.campo_senha = CampoTexto("Senha", senha=True)
        self.campo_confirmar_senha = CampoTexto("Confirmar senha", senha=True)
        
        logo = exibir_logo(self.page.window_width)
        
        conteudo = ft.Container(
            expand=True,  
            gradient=GRADIENTE,
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Container(),
                            logo,
                            ft.Container()
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    self.campo_usuario,
                    self.campo_email,
                    self.campo_senha,
                    self.campo_confirmar_senha,
                    Botao("Registrar", self.ao_clicar_registrar, primario=True),
                    BotaoTexto("Voltar para Login", self.ao_clicar_voltar),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                expand=True  
            )
        )
        
        self.page.add(conteudo)