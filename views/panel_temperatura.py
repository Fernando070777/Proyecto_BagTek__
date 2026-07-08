from flet import Container,Text,Column,Slider,FilledButton,Alignment,FontWeight,MainAxisAlignment,CrossAxisAlignment

class PanelTemperatura(Container):
    def __init__(self):
        super().__init__()
        
        self._txt_temperatura = Text("10",size=30)
        self._sld_tempereatura = Slider(min=1, max=200)
        self._btn_ajustar = FilledButton("Ajustar", on_click= self._click_ajustar_temperatura)
        self.content=Column(
            alignment=MainAxisAlignment.START,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            width=480,height=512,
              spacing=48,
            controls=[

                Text("Reactor de temperatura", size=32, weight=FontWeight.BOLD),
                self._txt_temperatura,
                self._sld_tempereatura,
                self._btn_ajustar,
                
            ]
        )

    def _click_ajustar_temperatura(self) -> None:
        temperatura = self._sld_tempereatura.value
        self._txt_temperatura.value = f"{temperatura}∘"
    