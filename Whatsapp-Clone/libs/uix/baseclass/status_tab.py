import utils
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase

utils.load_kv("status_tab.kv")


class StatusTab(FloatLayout, MDTabsBase):
    pass
