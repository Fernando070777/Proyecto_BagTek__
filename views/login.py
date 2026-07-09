from flet import Container,Text,Column,Alignment,FontWeight,MainAxisAlignment,CrossAxisAlignment,TextField,Icons,ElevatedButton,CircleAvatar,Colors
import flet as ft
class Login(Container):
    def __init__(self):
        super().__init__()
        
        self._txt_usuario = TextField(icon=Icons.PERSON, label="usuario@correo.com",text_style=ft.TextStyle(size=16,
        color=ft.Colors.WHITE, font_family="ComicSans"),
        label_style=ft.TextStyle(color=ft.Colors.LIGHT_BLUE_700),
        hint_style=ft.TextStyle(color=ft.Colors.WHITE_30),)

        self._txt_contrasenia = TextField(icon=Icons.LOCK, label="*************",text_style=ft.TextStyle(size=16,
        color=ft.Colors.WHITE, font_family="ComicSans"),
        label_style=ft.TextStyle(color=ft.Colors.LIGHT_BLUE_700),
        hint_style=ft.TextStyle(color=ft.Colors.WHITE_30),)

        self.txt_resultado = Text()
        self.content=Column(
            alignment=MainAxisAlignment.START,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            width=480,height=512,
              spacing=48,
            controls=[

                Text("Inicio de Sesion", size=32, weight=FontWeight.BOLD),
                CircleAvatar(
                foreground_image_src="/home/fernando777/workspaces/3erParcial/01_Temperatura_Reactor/Recursos/Logo.png",
                    radius=50,height=200, width=200
                ),          
                Text("User", size=32, weight=FontWeight.BOLD),
                self._txt_usuario,
                Text("Password", size=32, weight=FontWeight.BOLD),
                self._txt_contrasenia,
                ElevatedButton("Iniciar Sesion", on_click=self._click_enviar, color=ft.Colors.BLACK), 
                self.txt_resultado

            ]
        )


    def _click_enviar(self):
        print("Enviado a consola")
        usuario = self._txt_usuario.value.strip()
        password = self._txt_contrasenia.value.strip()

        if usuario == "Admin" and password == "777":
            self.txt_resultado.value = "Acceso Correcto"
        
        else:
            self.txt_resultado.value = "Acceso Incorrecto"

        print(f"""
        usuario: {usuario}
        password: {password}
        """)
    