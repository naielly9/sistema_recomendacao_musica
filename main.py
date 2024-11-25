import flet as ft
from Telas.telaSplash import TelaSplash

def main(page: ft.Page):
    tela_splash = TelaSplash(page)
    tela_splash.mostrar()

ft.app(main, view=ft.AppView.WEB_BROWSER)

