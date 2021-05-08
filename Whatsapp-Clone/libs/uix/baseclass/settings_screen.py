import utils
from kivymd.uix.screen import MDScreen

utils.load_kv("settings_screen.kv")


class SettingsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
