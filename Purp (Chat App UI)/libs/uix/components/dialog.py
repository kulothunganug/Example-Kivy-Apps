from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.modalview import ModalView

from core.theming import ThemableBehavior

Builder.load_string(
    """
<BaseDialog>
    background: 'assets/images/transparent.png'
    size_hint_y: .5  # small hack to fix touch not responding


<PDialog>

    PBoxLayout:
        id: container
        orientation: 'vertical'
        adaptive_height: True
        size_hint_x: .9

        canvas.before:
            Color:
                rgba: root.theme_cls.bg_normal
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: root.radius

"""
)


class BaseDialog(ModalView):
    radius = ListProperty([dp(7), dp(7), dp(7), dp(7)])


class PDialog(ThemableBehavior, BaseDialog):
    content = ObjectProperty()

    def on_content(self, instance, value):
        Clock.schedule_once(self.add_content_cls)

    def add_content_cls(self, i):
        self.ids.container.add_widget(self.content)
