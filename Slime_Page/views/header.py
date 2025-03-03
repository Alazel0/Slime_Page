import reflex as rx
from Slime_Page.styles.styles import Size

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="SP", size="9"),
            rx.vstack(
                rx.text("Slime Links", weight="bold", size="4"),
                rx.text("@slime_links", color_scheme="gray"),
            )
        ),
        rx.text("aqui podria ir un texto de ser necesario ya vere si lo quito o lo cambio"),
        padding_top= Size.DEFAULT.value
    )