
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.list import OneLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.core.clipboard import Clipboard

import wikipedia
import threading


class MainApp(MDApp):
    url = ''

    def build(self):
        self.title = 'Wikipedia-App'

    def search(self, text):
        t1 = threading.Thread(target=self.get_wiki, args=(text,))
        t1.start()

    def get_wiki(self, text):
        self.root.ids.rc_spin.active = True
        self.root.ids.summary.text = ''
        self.root.ids.title.text = ''
        self.root.ids.error.text = ''

        wikipedia.set_lang("en") # to use specific lanuage
        try:
            summary = wikipedia.page(text.strip())
            self.root.ids.title.text = summary.title
            self.root.ids.summary.text = f'\n{summary.summary}'
            self.root.ids.rc_spin.active = False
        except Exception as e:
            print(e)
            self.root.ids.summary.text = 'Sorry unable to find ' + self.root.ids.fld.text
            self.root.ids.rc_spin.active = False


if __name__ == '__main__':
    MainApp().run()
