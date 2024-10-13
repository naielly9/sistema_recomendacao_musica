import flet as ft
from .telaBase import TelaBase
from .componentes.campoTexto import CampoTexto
from .componentes.identidadeVisual import GRADIENTE, exibir_logo, ALINHAMENTO_COLUNA, ALINHAMENTO_LINHA
from .componentes.elementosGraficos import GeneroMusical, ImagensPopulares, LimparAplicarTema

class TelaPrincipal(TelaBase):
    def __init__(self, page: ft.Page, username: str, email: str):
        super().__init__(page)
        self.username = username
        self.email = email

    def ao_clicar_login(self, e):
        LimparAplicarTema(self.page)
        from .telaLogin import TelaLogin
        login_screen = TelaLogin(self.page)
        login_screen.mostrar()
        
    def ao_clicar_sobre_nos(self, e):
        LimparAplicarTema(self.page)
        from .telaSobreNos import TelaSobreNos
        SobreNos_screen = TelaSobreNos(self.page)
        SobreNos_screen.mostrar()
        
    def ao_clicar_trocar_tema(self, e):
        if self.theme_mode == ft.ThemeMode.DARK:
            self.theme_mode = ft.ThemeMode.LIGHT
        else:
            self.theme_mode = ft.ThemeMode.DARK
        self.page.theme_mode = self.theme_mode
        self.page.update() 

    def mostrar(self):
        self.page.title = "Listen"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.update()

        self.page.appbar = ft.AppBar(
            leading=ft.PopupMenuButton(
                icon=ft.icons.MENU,
                items=[
                    ft.PopupMenuItem(text="Trocar Tema", on_click=self.ao_clicar_trocar_tema),
                    ft.PopupMenuItem(text="Sobre Nos", on_click=self.ao_clicar_sobre_nos),
                    ft.PopupMenuItem(text="Sair", on_click=self.ao_clicar_login)
                ],
            ),
            title=ft.Text("Listen", style="titleLarge"),
            actions=[
                ft.PopupMenuButton(
                    icon=ft.icons.PERSON,
                    items=[
                        ft.PopupMenuItem(text=f"\nUser: {self.username} \nConta: {self.email}\n"),
                    ],
                )
            ],
            center_title=True,
        )

        genero_rap = GeneroMusical("Telas/Imagens/rap.webp", "Rap")
        genero_rock = GeneroMusical("Telas/Imagens/rock.jpg", "Rock")
        genero_eletronica = GeneroMusical("Telas/Imagens/eletronica.jpg", "Eletrônica")
        genero_sertanejo = GeneroMusical("Telas/Imagens/sertanejo.jpeg", "Sertanejo")
        genero_trap = GeneroMusical("Telas/Imagens/trap.jpg", "Trap")

        genres_images = ft.Row(
            wrap=False,
            scroll="always",
            spacing=10,
            controls=[genero_rap, genero_rock, genero_eletronica, genero_trap,genero_sertanejo]
        )
        seccao_generos = ft.Container(
            content=ft.Column(
                [
                    ft.Text("Gêneros", style="titleMedium"),
                    genres_images,
                ],
                spacing=10,
            ),
            padding=15
        )

        lista_imagens = [
            "Telas/Imagens/MBDT.jpg",
            "Telas/Imagens/MADDCITY.jpg",
            "Telas/Imagens/FATG.jpg",
            "Telas/Imagens/BORNTODIE.jpg",
            "Telas/Imagens/HAPPIERTHANEVER.jpg",
            "Telas/Imagens/HMHAS.jpg",
            "Telas/Imagens/NOTHINGWASAME.jpg",
            "Telas/Imagens/MISEDUCATION .jpg",
        ]
        imagens_populares = ImagensPopulares(lista_imagens)

        seccao_popular = ft.Container(
            content=ft.Column(
                [
                    ft.Text("Popular", style="titleMedium"),
                    imagens_populares,
                ],
                spacing=10,
            ),
            padding=15  
        )

        self.page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
                ft.NavigationDestination(icon=ft.icons.SEARCH, label="Pesquisar"),
                ft.NavigationDestination(icon=ft.icons.STAR, label="Avaliar"),
                ft.NavigationDestination(icon=ft.icons.NOTIFICATIONS, label="Notificação"),
            ],
        )
        conteudo_principal = ft.Container(
            expand=True,
            content=ft.Column(
                [
                    seccao_generos,
                    seccao_popular,
                ],
            ),
        )

        self.page.add(conteudo_principal)
