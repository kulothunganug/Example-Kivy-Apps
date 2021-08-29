from kivy.lang import Builder
from kivy.properties import BooleanProperty

from components.label import PLabel

Builder.load_string(
    """
<ChatBubble>
    adaptive_height: True
    padding: [dp(8), dp(8)]
    text_color: 1, 1, 1, 1
    text_size: self.width, None

    canvas.before:
        Color:
            rgba:
                self.theme_cls.primary_dark if self.send_by_user \
                else self.theme_cls.primary_color
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius:
                [dp(8), dp(8), (dp(-5), dp(5)), dp(8)] if self.send_by_user \
                else [(dp(-5), dp(5)), dp(8), dp(8), dp(8)]
"""
)


class ChatBubble(PLabel):
    send_by_user = BooleanProperty()
