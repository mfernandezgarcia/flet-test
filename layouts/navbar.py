from flet import UserControl, AppBar, Text, colors, PopupMenuButton, PopupMenuItem


class Navbar(UserControl):
    def __init__(self):
        super().__init__()
        print("Ejecutando el constructor desde navbar")

    def build(self):
        print("Ejecutando el build desde navbar")
        return AppBar(
            actions=[
                PopupMenuButton(
                    items=[
                        PopupMenuItem(text="Configuración"),
                        PopupMenuItem(text="Cerrar sesión"),
                    ]
                )
            ],
            bgcolor=colors.DEEP_ORANGE,
            center_title=False,
            color=colors.WHITE,
            elevation=10,
            leading_width=40,
            title=Text("Real Food")
        )
