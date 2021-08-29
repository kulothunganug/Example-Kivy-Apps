from kivy.animation import Animation
from kivy.lang import Builder
from kivy.properties import BooleanProperty, ColorProperty, StringProperty
from kivy.uix.behaviors import ButtonBehavior

from components.boxlayout import PBoxLayout
from core.theming import ThemableBehavior

Builder.load_string(
    """
<ListItem>
    spacing: dp(15)
    padding: dp(10)
    adaptive_height: True

    canvas.before:
        Color:
            rgba: root.bg_color
        RoundedRectangle:
            radius: [dp(18),]
            size: self.size
            pos: self.pos

    PBoxLayout:
        adaptive_size: True
        pos_hint: {"center_y": .5}

        PIcon:
            icon: root.icon
            adaptive_size: True
            font_size: sp(30)

    PBoxLayout:
        orientation: 'vertical'
        spacing: dp(7)
        adaptive_height: True
        pos_hint: {"center_y": .5}

        PLabel:
            text: root.text
            adaptive_height: True
            shorten: True
            shorten_from: 'right'
            text_size: self.width, None

        PLabel:
            text: root.secondary_text
            font_name: 'LexendLight'
            text_color: 0.5, 0.5, 0.5, 0.5
            adaptive_height: True
            shorten: True
            shorten_from: 'right'
            text_size: self.width, None


<-ChatListItem>
    padding: [dp(10), dp(15)]
    spacing: dp(10)
    adaptive_height: True

    canvas.before:
        Color:
            rgba: root.bg_color
        RoundedRectangle:
            radius: [dp(18),]
            size: self.size
            pos: self.pos

    PBoxLayout:
        adaptive_size: True
        pos_hint: {"center_y": .5}

        FitImage:
            source: root.image
            size_hint: None, None
            size: dp(50), dp(50)
            radius: [dp(18),]

    PBoxLayout:
        orientation: 'vertical'
        spacing: dp(7)
        adaptive_height: True
        pos_hint: {"center_y": .5}

        PLabel:
            text: root.text
            adaptive_height: True
            shorten: True
            shorten_from: 'right'
            text_size: self.width, None

        PLabel:
            text: root.secondary_text
            font_name: 'LexendLight'
            text_color: 0.5, 0.5, 0.5, 0.5
            adaptive_height: True
            shorten: True
            shorten_from: 'right'
            text_size: self.width, None

    PBoxLayout:
        orientation: 'vertical'
        spacing: dp(7)
        adaptive_size: True
        pos_hint: {"center_y": .5}

        PLabel:
            text: root.time
            font_name: 'LexendThin'
            adaptive_size: True

        Widget:
            size_hint: None, None
            size: dp(10), dp(10)

            canvas.before:
                Color:
                    rgba:
                        root.theme_cls.primary_color if root.unread_messages \
                        else (0, 0, 0, 0)
                Ellipse:
                    size: self.size
                    pos: self.pos

    """
)


class ListItem(ButtonBehavior, ThemableBehavior, PBoxLayout):

    bg_color = ColorProperty([0, 0, 0, 0])

    text = StringProperty()

    secondary_text = StringProperty()

    icon = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bg_color = self.theme_cls.bg_normal
        self.theme_cls.bind(theme_style=self._update_bg_color)

    def _update_bg_color(self, *args):
        self.bg_color = self.theme_cls.bg_normal

    def on_state(self, instance, value):
        Animation(
            bg_color=self.theme_cls.bg_dark
            if value == "down"
            else self.theme_cls.bg_normal,
            d=0.1,
            t="in_out_cubic",
        ).start(self)


class ChatListItem(ListItem):
    image = StringProperty()

    time = StringProperty()

    unread_messages = BooleanProperty()
