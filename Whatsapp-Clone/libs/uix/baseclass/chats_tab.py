import json

import utils
from kivy.properties import ListProperty
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase

utils.load_kv("chats_tab.kv")


class ChatsTab(FloatLayout, MDTabsBase):

    users_data = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open("assets/users.json") as f:
            data = json.load(f)

        for i in data:
            user_data = {
                "text": i,
                "secondary_text": data[i]["message"],
                "time": data[i]["time"],
                "image": data[i]["image"],
            }
            self.users_data.append(user_data)
