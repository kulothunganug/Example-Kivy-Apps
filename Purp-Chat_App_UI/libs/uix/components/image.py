from kivy.clock import Clock
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.widget import Widget

Builder.load_string(
    """
<FitImage>
    canvas.before:
        StencilPush
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: root.radius
        StencilUse

    canvas.after:
        StencilUnUse
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: root.radius
        StencilPop
"""
)


class FitImage(BoxLayout):
    source = ObjectProperty()
    container = ObjectProperty()
    radius = ListProperty([0, 0, 0, 0])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self._late_init)

    def _late_init(self, *args):
        self.container = Container(self.source)
        self.bind(source=self.container.setter("source"))
        self.add_widget(self.container)


class Container(Widget):
    source = ObjectProperty()
    image = ObjectProperty()

    def __init__(self, source, **kwargs):
        super().__init__(**kwargs)
        self.image = AsyncImage()
        self.image.bind(on_load=self.adjust_size)
        self.source = source
        self.bind(size=self.adjust_size, pos=self.adjust_size)

    def on_source(self, instance, value):
        if isinstance(value, str):
            self.image.source = value
        else:
            self.image.texture = value
        self.adjust_size()

    def adjust_size(self, *args):
        if not self.parent or not self.image.texture:
            return

        (par_x, par_y) = self.parent.size

        if par_x == 0 or par_y == 0:
            with self.canvas:
                self.canvas.clear()
            return

        par_scale = par_x / par_y
        (img_x, img_y) = self.image.texture.size
        img_scale = img_x / img_y

        if par_scale > img_scale:
            (img_x_new, img_y_new) = (img_x, img_x / par_scale)
        else:
            (img_x_new, img_y_new) = (img_y * par_scale, img_y)

        crop_pos_x = (img_x - img_x_new) / 2
        crop_pos_y = (img_y - img_y_new) / 2

        subtexture = self.image.texture.get_region(
            crop_pos_x, crop_pos_y, img_x_new, img_y_new
        )

        with self.canvas:
            self.canvas.clear()
            Color(1, 1, 1)
            Rectangle(texture=subtexture, pos=self.pos, size=(par_x, par_y))
