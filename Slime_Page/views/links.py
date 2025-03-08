import reflex as rx
from Slime_Page.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            link_button("Login with Discord", "/auth/discord"),
            rx.spacer(),
            link_button("Login with Twitter", "/auth/twitter")
        )
    )