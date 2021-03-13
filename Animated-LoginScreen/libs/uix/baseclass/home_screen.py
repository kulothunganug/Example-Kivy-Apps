import utils
from kivy.animation import Animation
from kivy.clock import mainthread
from kivy.metrics import dp
from kivy.properties import BooleanProperty
from kivymd.uix.screen import MDScreen

utils.load_kv("home_screen.kv")


class HomeScreen(MDScreen):
    """
    Example Screen.
    """

    on_section = BooleanProperty(False)

    @mainthread
    def goto_section(self, section):
        if self.on_section:
            return
        self.current_section = section
        self.on_section = True

        # header text
        self.ids.header_text.text = (
            "Welcome!" if section == "sign_up" else "Welcome Back!"
        )

        # header icon
        self.ids.header_icon.pos_hint = {
            "center_x": -1 if section == "sign_up" else 1.2
        }

        self.ids.header_icon.disabled = False
        Animation(pos_hint={"center_x": 0.5}, t="in_out_circ").start(
            self.ids.header_icon
        )

        # labels in selected card
        for lbl in self.ids["welcome_" + section].children:
            if not lbl.text.startswith("Sign"):
                Animation(opacity=0, t="in_out_circ").start(lbl)
        self.ids[section].radius = [
            dp(30),
        ]

        # selected card
        Animation(
            pos_hint={"center_x": 0.5}, size_hint_x=0.8, t="in_out_circ"
        ).start(self.ids[section])

        # forms in main card
        Animation(opacity=1, t="in_out_circ").start(
            self.ids[section + "_form"]
        )
        self.ids[section + "_form"].disabled = False

        # another card
        Animation(opacity=0, d=0.2).start(
            self.ids["sign_in" if section == "sign_up" else "sign_up"]
        )

    @mainthread
    def back_section(self):
        if not self.on_section:
            return
        self.on_section = False

        def restore_radius(*args):
            self.ids[self.current_section].radius = (
                [0, dp(30), dp(30), 0]
                if self.current_section == "sign_up"
                else [dp(30), 0, 0, dp(30)]
            )

        # header text
        self.ids.header_text.text = "Hello!"

        # header icon
        Animation(
            pos_hint={
                "center_x": -1 if self.current_section == "sign_up" else 1.2
            },
            t="in_out_circ",
        ).start(self.ids.header_icon)

        # labels in selected card
        for lbl in self.ids["welcome_" + self.current_section].children:
            if not lbl.text.startswith("Sign"):
                Animation(opacity=1, t="in_out_circ").start(lbl)

        # selected card
        anim = Animation(
            pos_hint={
                "center_x": 0.2 if self.current_section == "sign_up" else 0.8
            },
            size_hint_x=0.45,
            t="in_out_circ",
        )
        anim.bind(on_complete=restore_radius)
        anim.start(self.ids[self.current_section])
        Animation(opacity=0, t="in_out_circ").start(
            self.ids[self.current_section + "_form"]
        )
        self.ids[self.current_section + "_form"].disabled = True

        # another card
        Animation(opacity=1).start(
            self.ids[
                "sign_in" if self.current_section == "sign_up" else "sign_up"
            ]
        )
