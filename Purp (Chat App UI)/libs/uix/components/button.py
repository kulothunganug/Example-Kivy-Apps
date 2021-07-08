from kivy.animation import Animation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ColorProperty, OptionProperty
from kivy.uix.behaviors import ButtonBehavior

from components.label import PIcon, PLabel
from core.theming import ThemableBehavior

Builder.load_string(
    """
<PButton>
    size_hint: None, None
    size: self.texture_size[0] + dp(10), self.texture_size[1] + dp(10)
    padding: [dp(10), dp(10)]
    font_size: sp(16)

    canvas.before:
        Color:
            rgba: root.bg_color
        RoundedRectangle:
            radius: [dp(18),]
            size: self.size
            pos: self.pos

    canvas.after:
        Color:
            rgba: 0.5, 0.5, 0.5, 0.5
        Line:
            width: dp(1)
            rounded_rectangle:
                (self.x, self.y, self.width, self.height, dp(18))

<PIconButton>
    size_hint: None, None
    size: self.texture_size
    padding: [dp(10), dp(10)]

    canvas.before:
        Color:
            rgba: self.bg_color
        Ellipse:
            size: self.size
            pos: self.pos

    canvas.after:
        Color:
            rgba: 0.5, 0.5, 0.5, 0.5
        Line:
            ellipse: (self.x, self.y, self.width, self.height)
            width: dp(1)
"""
)


class BaseButton(ButtonBehavior, ThemableBehavior):
    mode = OptionProperty(
        "contained", options=["contained", "outlined", "unstyled", "custom"]
    )

    bg_color = ColorProperty([0, 0, 0, 0])

    bg_normal = ColorProperty([0, 0, 0, 0])

    bg_down = ColorProperty([0, 0, 0, 0])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(lambda x: self.on_mode(None, self.mode))
        self.theme_cls.bind(
            theme_style=lambda *args: self.on_mode(None, self.mode)
        )

    def on_mode(self, *args):
        raise NotImplementedError()

    def on_state(self, instance, value):
        anim = Animation(
            bg_color=self.bg_down if value == "down" else self.bg_normal,
            d=0.2,
            t="in_out_cubic",
        )
        anim.start(self)


class PButton(BaseButton, PLabel):
    def on_mode(self, instance, value):
        if value == "contained":
            self.canvas.after.clear()
            self.bg_color = self.theme_cls.primary_color
            self.bg_normal = self.theme_cls.primary_color
            self.bg_down = self.theme_cls.primary_dark
            self.text_color = (1, 1, 1, 1)
        elif value == "outlined":
            self.bg_down = (0.5, 0.5, 0.5, 0.5)
            self.bg_normal = self.theme_cls.bg_normal
            self.bg_color = self.theme_cls.bg_normal
        elif value == "custom":
            self.canvas.after.clear()
            self.bg_color = self.bg_normal


class PIconButton(BaseButton, PIcon):
    def on_mode(self, instance, value):
        if value == "contained":
            self.canvas.after.clear()
            self.bg_color = self.theme_cls.primary_color
            self.bg_normal = self.theme_cls.primary_color
            self.bg_down = self.theme_cls.primary_dark
            self.text_color = (1, 1, 1, 1)
        elif value == "outlined":
            self.bg_down = self.theme_cls.bg_dark
            self.bg_normal = self.theme_cls.bg_normal
            self.bg_color = self.theme_cls.bg_normal
        elif value == "unstyled":
            self.bg_down = self.theme_cls.bg_dark
            Clock.schedule_once(lambda x: self.canvas.after.clear())
        else:
            self.bg_color = self.bg_normal
            Clock.schedule_once(lambda x: self.canvas.after.clear())
