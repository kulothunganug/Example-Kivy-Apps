import threading

import wikipedia
from kivy.clock import mainthread
from kivymd.app import MDApp


class MainApp(MDApp):
    url = ""

    def build(self):
        self.title = "Wikipedia-App"

    @mainthread
    def search(self, text):
        t1 = threading.Thread(target=self.get_wiki, args=(text,), daemon=True)
        t1.start()

    def get_wiki(self, text):
        self.root.ids.rc_spin.active = True
        self.root.ids.summary.text = ""
        self.root.ids.title.text = ""

        wikipedia.set_lang("en")
        try:
            summary = wikipedia.page(text.strip())
            self.root.ids.title.text = summary.title
            self.root.ids.summary.text = f"\n{summary.summary}"
        except Exception as e:
            print(e)
            self.root.ids.title.text = (
                "[color=#EE4B2B]"
                + "Sorry unable to find "
                + self.root.ids.fld.text
                + "[/color]"
            )
        self.root.ids.rc_spin.active = False


if __name__ == "__main__":
    MainApp().run()
