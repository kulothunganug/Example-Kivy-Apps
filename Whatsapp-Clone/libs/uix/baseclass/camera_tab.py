import utils
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase

utils.load_kv("camera_tab.kv")


class CameraTab(FloatLayout, MDTabsBase):
    pass
