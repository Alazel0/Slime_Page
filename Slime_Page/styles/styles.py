import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TextColor

#Constants
MAX_WIDTH = "600px"

#temporal
FLEX_DIRECTION = "row"

#sizes
class Size(Enum):
    SMALL = "0.5em"
    DEFAULT = "1em"
    BIG = "2em"

# Style
BASE_STYLE = {
    "backgraund_color": Color.BACKGRAUND.value,
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "color": TextColor.HEADER,
        "border_radius": Size.DEFAULT.value
    }
}

title_style = dict(
    width = "100%",
    padding_top = Size.DEFAULT.value
)