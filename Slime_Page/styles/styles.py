import reflex as rx
from enum import Enum

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
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value
    }
}

title_style = dict(
    width = "100%",
    padding_top = Size.DEFAULT.value
)