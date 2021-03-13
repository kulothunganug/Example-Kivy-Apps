from kivy.core.text import LabelBase

fonts_path = "assets/fonts/"

fonts = [
    {
        "name": "Exo2",
        "fn_regular": fonts_path + "Exo2-Regular.ttf",
        "fn_bold": fonts_path + "Exo2-Bold.ttf",
        "fn_italic": fonts_path + "Exo2-Italic.ttf",
        "fn_bolditalic": fonts_path + "Exo2-BoldItalic.ttf",
    },
    {
        "name": "Exo2Thin",
        "fn_regular": fonts_path + "Exo2-Thin.ttf",
        "fn_italic": fonts_path + "Exo2-ThinItalic.ttf",
    },
    {
        "name": "Exo2Light",
        "fn_regular": fonts_path + "Exo2-Light.ttf",
        "fn_italic": fonts_path + "Exo2-LightItalic.ttf",
    },
    {
        "name": "Exo2Medium",
        "fn_regular": fonts_path + "Exo2-Medium.ttf",
        "fn_italic": fonts_path + "Exo2-MediumItalic.ttf",
    },
    {
        "name": "Exo2Black",
        "fn_regular": fonts_path + "Exo2-Black.ttf",
        "fn_italic": fonts_path + "Exo2-BlackItalic.ttf",
    },
]

for font in fonts:
    LabelBase.register(**font)

font_styles = {
    "H1": ["Exo2Light", 96, False, -1.5],
    "H2": ["Exo2Light", 60, False, -0.5],
    "H3": ["Exo2", 48, False, 0],
    "H4": ["Exo2", 34, False, 0.25],
    "H5": ["Exo2", 24, False, 0],
    "H6": ["Exo2Medium", 20, False, 0.15],
    "Subtitle1": ["Exo2", 16, False, 0.15],
    "Subtitle2": ["Exo2Medium", 14, False, 0.1],
    "Body1": ["Exo2", 16, False, 0.5],
    "Body2": ["Exo2", 14, False, 0.25],
    "Button": ["Exo2Medium", 14, True, 1.25],
    "Caption": ["Exo2", 12, False, 0.4],
    "Overline": ["Exo2", 10, True, 1.5],
}
