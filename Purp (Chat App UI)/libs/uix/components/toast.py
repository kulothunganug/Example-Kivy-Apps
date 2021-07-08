from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ListProperty, NumericProperty
from kivy.utils import platform

from components.dialog import BaseDialog
from components.label import PLabel

Builder.load_string(
    """
<Toast>
    size_hint: None, None
    pos_hint: {"center_x": 0.5, "center_y": 0.1}
    opacity: 0
    auto_dismiss: True
    overlay_color: 0, 0, 0, 0

    canvas:
        Color:
            rgba: root.bg_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [7, 7, 7, 7]
"""
)


class Toast(BaseDialog):
    duration = NumericProperty(2.5)
    bg_color = ListProperty([0.2, 0.2, 0.2, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label_toast = PLabel(
            text_color=(1, 1, 1, 1),
            size_hint=(None, None),
            opacity=0,
            halign="center",
        )
        self.label_toast.bind(texture_size=self.label_check_texture_size)
        self.add_widget(self.label_toast)

    def label_check_texture_size(self, instance, texture_size):
        texture_width, texture_height = texture_size
        if texture_width > Window.width:
            instance.text_size = (Window.width - dp(10), None)
            instance.texture_update()
            texture_width, texture_height = instance.texture_size
        self.size = (texture_width + 25, texture_height + 25)

    def toast(self, text_toast):
        self.label_toast.text = text_toast
        self.open()

    def on_open(self):
        self.fade_in()
        Clock.schedule_once(self.fade_out, self.duration)

    def fade_in(self):
        anim = Animation(opacity=1, duration=0.4)
        anim.start(self.label_toast)
        anim.start(self)

    def fade_out(self, *args):
        anim = Animation(opacity=0, duration=0.4)
        anim.bind(on_complete=lambda *x: self.dismiss())
        anim.start(self.label_toast)
        anim.start(self)

    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            if self.auto_dismiss:
                self.fade_out()
                return False
        super().on_touch_down(touch)
        return True


if platform != "android":

    def toast(text):
        Toast().toast(text)


else:
    from android.runnable import run_on_ui_thread
    from jnius import autoclass

    activity = autoclass("org.kivy.android.PythonActivity").mActivity
    AndroidToast = autoclass("android.widget.Toast")
    String = autoclass("java.lang.String")

    @run_on_ui_thread
    def toast(text):
        duration = AndroidToast.LENGTH_LONG
        t = AndroidToast.makeText(activity, String(text), duration)
        t.show()
