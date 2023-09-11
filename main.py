import flet as ft
# from layouts.navbar import Navbar as CustomNavbar
# from layouts.navigation_bar import NavigationBar
from flet import NavigationDestination, icons, colors, NavigationBarLabelBehavior, NavigationBar, AppBar, Text, colors, PopupMenuButton, PopupMenuItem, GridView


def main(page: ft.Page):
    page.title = "Real Good"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.GREY_100

    def route_change(e: ft.RouteChangeEvent):
        page.add(ft.Text(f"Route changed: {e.route}!"))

    page.on_route_change = route_change

    page.appbar = AppBar(
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

    page.navigation_bar = NavigationBar(
        bgcolor=colors.WHITE,
        destinations=[
            NavigationDestination(icon=icons.HOME, label="Home"),
            NavigationDestination(
                icon=icons.COMMUTE, label="Commute")
        ],
        elevation=40,
        label_behavior=NavigationBarLabelBehavior.ONLY_SHOW_SELECTED,
        # on_change=lambda destination: print(destination.label)
    )
    
    # grid_container = GridView()

    page.add(ft.Text("Body!"))
    page.add(ft.Text("Another text"))


if __name__ == "__main__":
    ft.app(target=main)
