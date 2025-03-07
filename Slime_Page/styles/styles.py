import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font

#Constants
MAX_WIDTH = "600px"

#temporal
FLEX_DIRECTION = "row"

#sizes
class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    DEFAULT = "1em"
    BIG = "2em"

# Style
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "background_color": Color.BACKGROUND.value,
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "color": TextColor.HEADER.value,
        "border_radius": Size.DEFAULT.value,
        "background_color": Color.CONTENT.value
    }
}

title_style = dict(
    width = "100%",
    padding_top = Size.DEFAULT.value,
    font_family = Font.TITLE.value
)