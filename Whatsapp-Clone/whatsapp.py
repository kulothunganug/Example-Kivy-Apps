import os
import platform

from kivy.core.window import Window
from kivymd.app import MDApp
from libs.uix.baseclass.root import Root

Window.size = (400, 700)

# This is needed for supporting Windows 10 with OpenGL < v2.0
if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"


colors = {
    "Green": {
        "50": "000000",
        "100": "000000",
        "200": "000000",
        "300": "000000",
        "400": "000000",
        "500": "075e55",
        "600": "000000",
        "700": "000000",
        "800": "000000",
        "900": "00cc3f",
        "A100": "000000",
        "A200": "000000",
        "A400": "000000",
        "A700": "000000",
    },
    "Light": {
        "StatusBar": "E0E0E0",
        "AppBar": "F5F5F5",
        "Background": "FAFAFA",
        "CardsDialogs": "FFFFFF",
        "FlatButtonDown": "cccccc",
    },
    "Dark": {
        "StatusBar": "000000",
        "AppBar": "212121",
        "Background": "303030",
        "CardsDialogs": "424242",
        "FlatButtonDown": "999999",
    },
}


class whatsapp(MDApp):  # NOQA: N801
    def __init__(self, **kwargs):
        super(whatsapp, self).__init__(**kwargs)
        Window.soft_input_mode = "below_target"
        self.title = "WhatsApp"
        self.icon = "assets/images/logo.png"

        self.theme_cls.colors = colors
        self.theme_cls.primary_palette = "Green"

        self.theme_cls.accent_palette = "Green"
        self.theme_cls.accent_hue = "900"

        self.theme_cls.theme_style = "Light"

    def build(self):
        return Root()
