from flet import Page
from views.login import Login

class Ventata:
    def __init__(self, ventana: Page)->None:
        self._ventana = ventana
        self._ventana.window.width = 1280
        self._ventana.window.height = 720        
        self._ventana.title= "Inicio de Sesion"
        self._ventana.add(Login())