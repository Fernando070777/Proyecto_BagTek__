from flet import Page
from views.panel_temperatura import PanelTemperatura

class Ventata:
    def __init__(self, ventana: Page)->None:
        self._ventana = ventana
        self._ventana.window.width = 1280
        self._ventana.window.height = 1280        
        self._ventana.title= "Temperatura"
        self._ventana.add(PanelTemperatura())