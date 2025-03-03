import reflex as rx
from Slime_Page.components.navbar import navbar
from Slime_Page.components.footer import footer
from Slime_Page.views.header import header
from Slime_Page.views.links import links
import Slime_Page.styles.styles as styles

@rx.page(
        
)

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                rx.vstack(
                    rx.flex(
                        rx.stack(
                            rx.box(
                                links()
                            )
                        )
                    ),
                    flex_direction = styles.FLEX_DIRECTION,
                    max_width = styles.MAX_WIDTH,
                    margin_y= styles.Size.DEFAULT.value
                ),
            ),
        ),
        footer()
    )