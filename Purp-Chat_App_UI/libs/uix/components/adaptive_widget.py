from kivy.properties import BooleanProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class AdaptiveWidget:
    adaptive_height = BooleanProperty(False)

    adaptive_width = BooleanProperty(False)

    adaptive_size = BooleanProperty(False)

    def on_adaptive_height(self, instance, value):
        self.size_hint_y = None
        if issubclass(self.__class__, Label):
            self.bind(
                texture_size=lambda *x: self.setter("height")(
                    self, self.texture_size[1]
                )
            )
        else:
            if not isinstance(self, (FloatLayout, Screen)):
                self.bind(minimum_height=self.setter("height"))

    def on_adaptive_width(self, instance, value):
        self.size_hint_x = None
        if issubclass(self.__class__, Label):
            self.bind(
                texture_size=lambda *x: self.setter("width")(
                    self, self.texture_size[0]
                )
            )
        else:
            if not isinstance(self, (FloatLayout, Screen)):
                self.bind(minimum_width=self.setter("width"))

    def on_adaptive_size(self, instance, value):
        self.size_hint = (None, None)
        if issubclass(self.__class__, Label):
            self.text_size = (None, None)
            self.bind(
                texture_size=lambda *x: self.setter("size")(
                    self, self.texture_size
                )
            )
        else:
            if not isinstance(self, (FloatLayout, Screen)):
                self.bind(minimum_size=self.setter("size"))
