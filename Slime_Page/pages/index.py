import reflex as rx
import Slime_Page.utils as utils
from Slime_Page.routes import Route
from Slime_Page.components.navbar import navbar
from Slime_Page.components.footer import footer
from Slime_Page.views.header import header
from Slime_Page.views.links import links
import Slime_Page.styles.styles as styles

@rx.page(
    route= Route.INDEX.value,
    title= utils.index_title,
    description= utils.index_description,
    # image= utils.preview,
    meta= utils.index_meta
)

def index() -> rx.Component:
    return rx.box(
        # utils.lang(),
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