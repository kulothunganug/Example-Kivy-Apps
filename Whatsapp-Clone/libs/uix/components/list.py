from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from libs.uix.components.profile_preview_dialog import ProfilePreview

Builder.load_string(
    """
<ChatListItem>
    adaptive_height: True
    padding: dp(15)
    spacing: dp(10)

    FitImage:
        id: img
        source: root.image
        size_hint: None, None
        size: dp(50), dp(50)
        radius: [self.width/2,]
        pos_hint: {'center_y': .5}
        on_touch_down:
            if self.collide_point(*args[1].pos): root.open_dialog()

    MDBoxLayout:
        orientation: 'vertical'
        pos_hint: {'center_y': .5}
        spacing: dp(5)
        adaptive_height: True

        MDLabel:
            text: root.text
            font_style: 'Subtitle1'
            adaptive_height: True

        MDLabel:
            text: root.secondary_text
            font_style: 'Body2'
            theme_text_color: 'Secondary'
            adaptive_height: True

    MDLabel:
        text: root.time
        font_style: 'Caption'
        theme_text_color: 'Secondary'
        adaptive_size: True
        pos_hint: {'center_y': .75}
"""
)


class ChatListItem(RectangularRippleBehavior, MDBoxLayout):

    text = StringProperty()

    secondary_text = StringProperty()

    image = StringProperty()

    time = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def open_dialog(self):
        ProfilePreview().fire(title=self.text, image=self.image)
