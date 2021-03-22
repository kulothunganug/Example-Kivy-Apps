import base64
import json

from kivymd.toast import toast
from kivymd.uix.screen import MDScreen

import utils

utils.load_kv("pass_screen.kv")


class PassScreen(MDScreen):
    def write(self):

        for i in self.ids:
            if not self.ids[i].text:
                toast("Please fill all the fields")
                return

        try:
            with open(self.manager.user_data_file, "r") as f:
                data = json.load(f)
        except Exception:
            data = {"data": []}

        data["data"].append(
            {
                "media": (self.ids.media_fld.text).strip(),
                "id": (self.ids.id_fld.text).strip(),
                "password": self.encode_str((self.ids.pass_fld.text).strip()),
            }
        )

        with open(self.manager.user_data_file, "w") as f:
            f.write(json.dumps(data, indent=4))

        self.clear_fields()
        self.goto_home()

    def clear_fields(self):
        for i in self.ids:
            self.ids[i].text = ""

    def encode_str(self, text):
        return str(base64.b64encode(text.encode("ascii")))[2:-1]

    def goto_home(self):
        self.manager.transition.direction = "right"
        self.manager.current = "home"
