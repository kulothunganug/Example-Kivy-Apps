__all__ = "TextFieldRound"

from functools import partial

from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.textinput import TextInput
from kivymd.theming import ThemableBehavior
from kivymd.uix.label import MDIcon

Builder.load_string(
    """
#: import images_path kivymd.images_path

<TextFieldRound>:
    multiline: False
    height: self.line_height + dp(10)
    size_hint: .8, .2
    background_active: f'{images_path}transparent.png'
    hint_text_color: self.theme_cls.disabled_hint_text_color
    background_normal: f'{images_path}transparent.png'
    foreground_color: self.theme_cls.text_color
    font_name: 'Exo2Light'
    padding:
        self._lbl_icon_left.texture_size[1] + dp(10) \
        if self.icon_left else dp(15), \
        (self.height / 2) - (self.line_height / 2), \
        self._lbl_icon_right.texture_size[1] + dp(20) \
        if self.icon_right else dp(15), \
        0

    canvas.before:
        Color:
            rgba: (0.5, 0.5, 0.5, 0.5) if self.focus \
                    else self.theme_cls.bg_darkest
        Ellipse:
            angle_start: 180
            angle_end: 360
            pos: self.pos[0] - self.size[1] / 2, self.pos[1]
            size: self.size[1], self.size[1]
        Ellipse:
            angle_start: 360
            angle_end: 540
            pos: self.size[0] + self.pos[0] - self.size[1]/2.0, self.pos[1]
            size: self.size[1], self.size[1]
        Rectangle:
            pos: self.pos
            size: self.size


        # Texture of left Icon.
        Color:
            rgba: self.theme_cls.primary_color
        Rectangle:
            texture: self._lbl_icon_left.texture
            size:
                self._lbl_icon_left.texture_size if self.icon_left \
                else (0, 0)
            pos:
                self.x, \
                self.center[1] - self._lbl_icon_left.texture_size[1] / 2

        # Texture of right Icon.
        Color:
            rgba: self.theme_cls.primary_color
        Rectangle:
            texture: self._lbl_icon_right.texture
            size:
                self._lbl_icon_right.texture_size if self.icon_right \
                else (0, 0)
            pos:
                (self.width + self.x) \
                - (self._lbl_icon_right.texture_size[1]), \
                self.center[1] - self._lbl_icon_right.texture_size[1] / 2

        Color:
            rgba:
                self.hint_text_color if not self.text \
                else root.foreground_color
"""
)


class TextFieldRound(ThemableBehavior, TextInput):
    icon_left = StringProperty()

    icon_right = StringProperty()

    password_mode = BooleanProperty()

    def __init__(self, **kwargs):
        self._lbl_icon_left = MDIcon()
        self._lbl_icon_right = MDIcon()
        super().__init__(**kwargs)

    def on_icon_left(self, instance, value):
        self._lbl_icon_left.icon = value

    def on_icon_right(self, instance, value):
        self._lbl_icon_right.icon = value

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.icon_right:
            icon_x = (
                (self.width + self.x)
                - (self._lbl_icon_right.texture_size[1])
                - dp(8)
            )
            icon_y = self.center[1] - self._lbl_icon_right.texture_size[1] / 2

            if touch.pos[0] > icon_x and touch.pos[1] > icon_y:
                if self.password_mode:
                    self.icon_right = "eye"
                    self.password_mode = False
                else:
                    self.icon_right = "eye-off"
                    self.password_mode = True
                self.password = self.password_mode

                cursor = self.cursor
                self.cursor = (0, 0)
                Clock.schedule_once(partial(self.set_cursor, cursor))
        return super(TextFieldRound, self).on_touch_down(touch)

    def set_cursor(self, pos, dt):
        self.cursor = pos
