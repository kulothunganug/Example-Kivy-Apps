from kivy.config import ConfigParser


class Config:
    config = ConfigParser()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config.read("config.ini")
        # Theme config
        self.config.adddefaultsection("theme")
        self.config.setdefault("theme", "theme_style", "Light")

        self.config.write()

    def get_theme_style(self):
        return self.config.get("theme", "theme_style")

    def set_theme_style(self, theme_style):
        self.config.set("theme", "theme_style", theme_style)
        self.config.write()


config = Config()
