import os
import sys

root_dir = os.path.split(os.path.abspath(sys.argv[0]))[0]
sys.path.insert(0, os.path.join(root_dir, "libs", "applibs"))
sys.path.insert(0, os.path.join(root_dir, "libs", "uix"))


from kivy.app import App
from kivy.core.window import Window
from kivy.utils import platform

import components
from androspecific import statusbar
from core.theming import ThemeManager
from root import Root
from utils.configparser import config

if platform != "android":
    Window.size = (350, 650)


class PurpApp(App):
    theme_cls = ThemeManager()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title = "Purp"
        self.icon = "assets/images/logo_w.png"

        self.theme_cls.theme_style = config.get_theme_style()

        Window.keyboard_anim_args = {"d": 0.2, "t": "linear"}
        Window.softinput_mode = "below_target"

    def build(self):
        self.root = Root()
        self.root.set_current("auth")

    def on_start(self):
        statusbar.set_color(self.theme_cls.primary_color)
