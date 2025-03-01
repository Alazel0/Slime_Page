import reflex as rx
from Slime_Page.components.link_button import link_button
from Slime_Page.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("Enlazar Redes"),
        rx.center(
            link_button("Twitter", "http:/www.ggg.com"),
            link_button("Discord", "http:/www.ggg.com")
        )
    )