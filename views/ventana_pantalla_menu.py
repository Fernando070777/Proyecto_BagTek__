from flet import Page
from views.pantalla_menu import PantallaMenu
import flet as ft

class Ventana:
    def __init__(self, ventana: Page) -> None: 
        self._ventana = ventana
        self._ventana.title = "Menu"
        
        self._ventana.window.width = 1200
        self._ventana.window.height = 720
        
        self._ventana.bgcolor = "white" 
        
        self._ventana.add(PantallaMenu())