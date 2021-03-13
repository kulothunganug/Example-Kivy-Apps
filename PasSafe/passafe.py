from kivy.core.window import Window
from kivymd.app import MDApp

from libs.uix.baseclass.root import Root

from config import fonts


class PasSafe(MDApp):
    def __init__(self, **kwargs):
        super(PasSafe, self).__init__(**kwargs)
        Window.soft_input_mode = "below_target"
        self.title = "PasSafe"
        self.icon = "assets/images/logo.png"

        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.primary_hue = "900"

        self.theme_cls.font_styles.update(fonts.font_styles)

    def build(self):
        return Root()
