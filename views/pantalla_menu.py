from flet import Container, Row, Column, ElevatedButton, Text

class PantallaMenu(Container):
    def __init__(self):
        super().__init__()

        self.content = Column(
            horizontal_alignment="center",  
            spacing=20,                     
            controls=[
                Row(
                    alignment="center", 
                    controls=[
                        Text("Menu principal",
                             size=40,
                        weight="bold",
                        color="black87")
                    ]
                ),
                Row(
                    alignment="center",     
                    controls=[
                        ElevatedButton("Modulo de alertas"),
                        ElevatedButton("Modulo Administrador"),
                        ElevatedButton("Panel de control"),
                    ]
                ), 
            
                Row(
                    alignment="center",     
                    controls=[
                        ElevatedButton("Base de datos"),
                        ElevatedButton("Portal de Monitoreo de Alertas"),
                        ElevatedButton("Gestor de Dispositivos de BAGXpert"),
                    ]
                )
                
            ]
        )