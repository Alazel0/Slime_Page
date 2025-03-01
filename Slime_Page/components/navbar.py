import reflex as rx
from Slime_Page.styles.styles import Size

def navbar() -> rx.Component:
    return rx.hstack(
        rx.center(
            rx.box(
                rx.heading(
                    rx.text(
                        "Slime Page"
                    )
                )
            )
        ),
        bg = "green",
        z_index = "5",
        border_radius = Size.SMALL.value,
        size = Size.DEFAULT.value,
        padding_x = Size.DEFAULT.value,
        padding_y = Size.SMALL.value,
        top = "0"
    )
