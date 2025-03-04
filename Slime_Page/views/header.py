import reflex as rx
from Slime_Page.styles.styles import Size
from Slime_Page.components.title import title
from Slime_Page.components.link_icon import link_icon

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="SP", size="9"),
            rx.vstack(
                rx.text("Slime Links", weight="bold", size="4"),
                rx.text("@slime_links", color_scheme="gray"),
            ),
            link_icon("https://x.com")
        ),
        rx.text("aqui podria ir un texto de ser necesario ya vere si lo quito o lo cambio"),
        rx.center(
            title("Enlazar Redes"),
        ),
        padding_top= Size.DEFAULT.value,
    )