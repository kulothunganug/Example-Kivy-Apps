from kivy.animation import Animation
from kivy.properties import DictProperty, ListProperty, StringProperty

from components.boxlayout import PBoxLayout
from components.dialog import PDialog
from components.screen import PScreen
from components.toast import toast


class ChatScreen(PScreen):
    user = DictProperty()
    title = StringProperty()
    chat_logs = ListProperty()

    def send(self, text):
        if not text:
            toast("Please enter any text!")
            return

        self.chat_logs.append(
            {"text": text, "send_by_user": True, "pos_hint": {"right": 1}}
        )

        self.chat_logs.append(
            {
                "text": "Okay!",
                "send_by_user": False,
            }
        )
        self.scroll_to_bottom()
        self.ids.field.text = ""

    def receive(self, text):
        self.chat_logs.append(
            {
                "text": text,
                "send_by_user": False,
            }
        )

    def show_user_info(self):
        PDialog(
            content=UserInfoDialogContent(
                title=self.user["name"],
                image=self.user["image"],
                about=self.user["about"],
            )
        ).open()

    def scroll_to_bottom(self):
        rv = self.ids.chat_rv
        box = self.ids.box
        if rv.height < box.height:
            Animation.cancel_all(rv, "scroll_y")
            Animation(scroll_y=0, t="out_quad", d=0.5).start(rv)


class UserInfoDialogContent(PBoxLayout):
    title = StringProperty()
    image = StringProperty()
    about = StringProperty()
