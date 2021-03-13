import json

from kivy.app import App
from kivy.clock import Clock
from kivy.factory import Factory  # NOQA: F401
from kivy.uix.screenmanager import ScreenManager


class Root(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_data_file = (
            App.get_running_app().user_data_dir + "/pass.json"
        )
        Clock.schedule_once(self.add_screens)

    def add_screens(self, interval):
        with open("screens.json") as f:
            screens = json.load(f)
            for import_screen, screen_details in screens.items():
                exec(import_screen)
                screen_object = eval(screen_details["factory"])
                screen_object.name = screen_details["screen_name"]
                self.add_widget(screen_object)
