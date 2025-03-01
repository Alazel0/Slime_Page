import reflex as rx
from Slime_Page.components.navbar import navbar
from Slime_Page.components.footer import footer
from Slime_Page.views.header.header import header
from Slime_Page.views.links.links import links
import Slime_Page.styles.styles as styles

@rx.page(route="/", title="Slime page")
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
app = rx.App(
    style = styles.BASE_STYLE
)
app.add_page(index)