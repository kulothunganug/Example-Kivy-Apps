from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ColorProperty, ListProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout

from components.button import PIconButton
from core.theming import ThemableBehavior

Builder.load_string(
    """
<PToolbar>
    size_hint_y: None
    height: dp(56)
    padding: [dp(15), dp(25), dp(15), dp(10)]

    PBoxLayout:
        id: left_actions
        orientation: "horizontal"
        size_hint_x: None
        padding: [0, (self.height - dp(48)) / 2]

    PBoxLayout:
        padding: [dp(10), 0]

        PLabel:
            text: root.title
            font_size: sp(25)
            size_hint_x: None
            width: self.texture_size[0]
            text_size: None, None
            markup: True
            on_touch_down:
                if self.collide_point(*args[1].pos): \
                root.dispatch('on_title_press')

    PBoxLayout:
        id: right_actions
        orientation: "horizontal"
        size_hint_x: None
        padding: [0, (self.height - dp(48)) / 2]

"""
)


class PToolbar(BoxLayout, ThemableBehavior):
    title = StringProperty()
    text_color = ColorProperty(None)
    left_action_items = ListProperty()
    right_action_items = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_title_press")

    def on_left_action_items(self, instance, value):
        self.update_action_bar(self.ids["left_actions"], value)

    def on_right_action_items(self, instance, value):
        self.update_action_bar(self.ids["right_actions"], value)

    def update_action_bar(self, action_bar, action_bar_items):
        action_bar.clear_widgets()
        new_width = 0
        for item in action_bar_items:
            new_width += dp(48)
            action_bar.add_widget(
                PIconButton(
                    icon=item[0],
                    mode="unstyled",
                    font_size="23sp",
                    pos_hint={"center_y": 0.5},
                    on_release=item[1],
                )
            )
        action_bar.width = new_width

    def on_title_press(self):
        pass
