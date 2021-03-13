import base64
import json
import os

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen

import utils

utils.load_kv("home_screen.kv")


class HomeScreen(MDScreen):

    data = None

    def on_pre_enter(self):
        self.set_list_items()

    def read_data(self):
        if not os.path.exists(self.manager.user_data_file):
            self.data = {"data": []}
        else:
            with open(self.manager.user_data_file, "r") as f:
                self.data = json.load(f)

    def set_list_items(self, text="", search=False):
        def add_list_item(data):
            self.ids.rv.data.append(
                {
                    "viewclass": "TwoLineListItem",
                    "text": data["media"],
                    "secondary_text": data["id"],
                    "on_release": lambda: self.open_dialog(
                        data["media"], data["id"], data["password"]
                    ),
                }
            )

        self.read_data()

        if not self.data["data"]:
            self.ids.rv.data = [
                {
                    "viewclass": "MDLabel",
                    "text": "No Passwords Saved!",
                    "halign": "center",
                    "font_style": "H5",
                }
            ]
            return

        self.ids.rv.data = []

        for i in self.data["data"]:
            if search:
                if text.strip().lower() in i["media"].lower():
                    add_list_item(i)
            else:
                add_list_item(i)

    def open_dialog(self, *args):

        self.temp_data = list(args)

        self.dialog = MDDialog(
            title=args[0],
            text=f"ID: {args[1]}\nPassword: {self.decode_str(args[2])}",
            buttons=[
                MDIconButton(
                    icon="trash-can-outline",
                    theme_text_color="Error",
                    on_release=self.delete_password,
                ),
                MDFlatButton(text="Close", on_release=self.close_dialog),
            ],
        )

        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

    def delete_password(self, *args):

        self.read_data()

        self.data["data"].remove(
            {
                "media": self.temp_data[0],
                "id": self.temp_data[1],
                "password": self.temp_data[2],
            }
        )
        _data = self.data

        with open(self.manager.user_data_file, "w") as f:
            f.write(json.dumps(_data, indent=4))

        self.set_list_items()
        self.dialog.dismiss()

    def open_settings(self):
        self.settings = MDDialog(
            content_cls=SettingsContent(),
            type="custom",
        )
        self.settings.open()

    def delete_all_password(self, *args):
        if os.path.exists(self.manager.user_data_file):
            os.remove(self.manager.user_data_file)
        self.dispatch("on_pre_enter")
        self.settings.dismiss()

    def decode_str(self, text):
        return str(
            base64.b64decode(bytes(text, encoding="ascii").decode("ascii"))
        )[2:-1]


class SettingsContent(MDBoxLayout):
    pass
