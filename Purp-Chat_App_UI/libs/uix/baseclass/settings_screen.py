from kivy.clock import Clock
from kivy.properties import StringProperty

from components.boxlayout import PBoxLayout
from components.dialog import PDialog
from components.screen import PScreen
from utils.configparser import config


class SettingsScreen(PScreen):
    theme_icon = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.change_theme_icon)

    def change_theme_icon(self, *args):
        self.theme_icon = (
            "moon" if self.theme_cls.theme_style == "Light" else "sun"
        )

    def open_about(self):
        PDialog(content=AboutDialogContent()).open()

    def change_theme(self):
        def _change_theme(i):
            self.theme_cls.theme_style = (
                "Dark" if self.theme_cls.theme_style == "Light" else "Light"
            )
            config.set_theme_style(self.theme_cls.theme_style)
            self.change_theme_icon()
        Clock.schedule_once(_change_theme, .2)


class AboutDialogContent(PBoxLayout):
    pass
