from flet import UserControl, NavigationDestination, icons, colors, NavigationBarLabelBehavior
from flet import NavigationBar as FletNavigationBar


class NavigationBar(UserControl):
    def __init__(self):
        super().__init__()
        print("Ejecutando el constructor desde navigation_bar")

    def build(self):
        print("Ejecutando el build desde navigation_bar")
        return FletNavigationBar(
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
