import reflex as rx
import Slime_Page.styles.styles as styles
from Slime_Page.pages.index import index

app = rx.App(
    style = styles.BASE_STYLE
)

app.add_page(index)