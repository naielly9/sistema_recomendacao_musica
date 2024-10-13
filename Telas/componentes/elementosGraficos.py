import flet as ft

class GeneroMusical(ft.UserControl):
    def __init__(self, imagem: str, nome: str):
        super().__init__()
        self.imagem = imagem
        self.nome = nome

    def build(self):
        return ft.Stack(
            controls=[
                ft.Image(
                    src=self.imagem,
                    fit=ft.ImageFit.COVER,
                    width=300,
                    height=300,
                    border_radius=ft.border_radius.all(10),
                ),
                ft.Container(
                    content=ft.Text(self.nome, color="white", style="headlineSmall"),
                    alignment=ft.alignment.center,
                    padding=10,
                ),
            ]
        )
    
class ImagensPopulares(ft.UserControl):
    def __init__(self, imagens: list):
        super().__init__()
        self.imagens = imagens  # Lista de URLs das imagens

    def build(self):
        # Cria os containers com as imagens
        containers = [
            ft.Container(
                content=ft.Image(src=imagem, fit=ft.ImageFit.COVER),
                width=150,
                height=150,
                border_radius=ft.border_radius.all(10),
            ) for imagem in self.imagens
        ]

        return ft.Row(
            wrap=False,
            scroll="always",
            spacing=10,
            controls=containers
        )


def LimparAplicarTema(page: ft.Page):
        """Limpa a página, remove AppBar e NavigationBar, e aplica o tema padrão."""
        page.clean()
        page.appbar = None
        page.navigation_bar = None
        theme_mode = ft.ThemeMode.DARK  # Altere para o tema desejado
        page.theme_mode = theme_mode  # Aplica o tema
        page.update()