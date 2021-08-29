from kivy.lang import Builder
from kivy.properties import ColorProperty, StringProperty
from kivy.uix.label import Label

from components.adaptive_widget import AdaptiveWidget
from core.theming import ThemableBehavior

Builder.load_string(
    """
#: import icons core.icon_definitions.icons

<PLabel>
    font_name: 'Lexend'
    color:
        self.text_color if self.text_color \
        else self.theme_cls.text_color

<PIcon>
    text: u'{}'.format(icons[self.icon]) if self.icon in icons else ''
    font_name: 'Icons'
    font_size: sp(40)
"""
)


class PLabel(ThemableBehavior, AdaptiveWidget, Label):
    text_color = ColorProperty(None)


class PIcon(PLabel):
    icon = StringProperty()
