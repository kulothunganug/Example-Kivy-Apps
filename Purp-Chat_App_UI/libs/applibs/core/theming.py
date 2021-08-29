from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.event import EventDispatcher
from kivy.properties import ColorProperty, OptionProperty
from kivy.utils import get_color_from_hex as gch

from core import font_definitions


class ThemeManager(EventDispatcher):
    primary_color = ColorProperty("684bbf")

    primary_light = ColorProperty("9b78f2")

    primary_dark = ColorProperty("34218e")

    bg_normal = ColorProperty()

    bg_light = ColorProperty()

    bg_dark = ColorProperty()

    text_color = ColorProperty()

    theme_style = OptionProperty("Light", options=["Light", "Dark"])

    def on_theme_style(self, instance, value):
        Window.clearcolor = gch("FAFAFA" if value == "Light" else "121212")
        if value == "Light":
            self.text_color = "000000"
            self.bg_light = "ffffff"
            self.bg_dark = "c7c7c7"
            self.bg_normal = "FAFAFA"
        else:
            self.text_color = "FFFFFF"
            self.bg_light = "383838"
            self.bg_dark = "000000"
            self.bg_normal = "121212"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        font_definitions.register_fonts()
        Clock.schedule_once(
            lambda x: self.on_theme_style(None, self.theme_style)
        )


class ThemableBehavior(EventDispatcher):
    def __init__(self, **kwargs):
        self.theme_cls = App.get_running_app().theme_cls
        super().__init__(**kwargs)
