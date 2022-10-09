import utils
from kivy.animation import Animation
from kivy.metrics import dp
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen

utils.load_kv("home_screen.kv")


class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        items = [
            "New group",
            "New broadcasts",
            "WhatsApp Web",
            "Starred messages",
            "Payments",
            "Settings",
        ]
        menu_items = [
            {
                "text": item,
                "viewclass": "OneLineListItem",
                "height": dp(54),
                "divider": None,
                "on_release": self.menu_callback
                if item == "Settings"
                else lambda *args: None,
            }
            for item in items
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=3,
            radius=[
                dp(2),
            ],
        )

    def open_menu(self, button):
        self.menu.caller = button
        self.menu.open()

    def menu_callback(self):
        self.manager.set_screen("settings")
        self.menu.dismiss()

    def on_tab_switch(self, *args):
        if args[3] == "[b]CHATS[/b]":
            self.ids.float_btn.icon = "message"
        elif args[3] == "[b]STATUS[/b]":
            self.ids.float_btn.icon = "camera"
        elif args[3] == "[b]CALLS[/b]":
            self.ids.float_btn.icon = "phone-plus"

        self.toggle_pencil_btn(args[3])

    def toggle_pencil_btn(self, current_tab):
        if current_tab == "[b]STATUS[/b]":
            anim = Animation(
                d=0.1, y=self.ids.float_btn.y + (self.ids.float_btn.height + dp(10))
            )
            self.ids.pencil_btn.disabled = False
        else:
            anim = Animation(d=0.1, y=self.ids.float_btn.y)
            self.ids.pencil_btn.disabled = True

        anim.start(self.ids.pencil_btn)


class CustomFloatingActionButton(MDFloatingActionButton):
    def set_size(self, interval):
        self.width = "40dp"
        self.height = "40dp"
