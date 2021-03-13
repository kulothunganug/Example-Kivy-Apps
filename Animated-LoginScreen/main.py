import os
import sys

root_dir = os.path.split(os.path.abspath(sys.argv[0]))[0]
sys.path.insert(0, os.path.join(root_dir, "libs", "applibs"))
import platform

from kivy.core.window import Window
from kivymd.app import MDApp
from libs.uix.baseclass.root import Root

# This is needed for supporting Windows 10 with OpenGL < v2.0
if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"


class LoginScreenApp(MDApp):
    def __init__(self, **kwargs):
        super(LoginScreenApp, self).__init__(**kwargs)
        Window.soft_input_mode = "below_target"
        self.title = "Animated-LoginScreen"

    def build(self):
        return Root()


LoginScreenApp().run()
