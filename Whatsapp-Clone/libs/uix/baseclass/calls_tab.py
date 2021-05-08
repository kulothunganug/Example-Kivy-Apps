import utils
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase

utils.load_kv("calls_tab.kv")


class CallsTab(FloatLayout, MDTabsBase):
    pass
