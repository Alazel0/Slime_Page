import reflex as rx
from Slime_Page.components.link_button import link_button
from Slime_Page.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            link_button("Twitter", "http:/www.ggg.com"),
            rx.spacer(),
            link_button("Discord", "http:/www.ggg.com")
        )
    )