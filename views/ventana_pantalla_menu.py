from flet import Page
from views.pantalla_menu import PantallaMenu

class VentanaPantallaMenu:
    def __init__(self, ventana: Page)->None:
        self._ventana_pantalla_menu = self._ventana_pantalla_menu
        self._ventana_pantalla_menu.window.width = 1280
        self._ventana_pantalla_menu.window.height = 720        
        self._ventana_pantalla_menu.title= "Inicio de Sesion"
        self._ventana_pantalla_menu.add(PantallaMenu())