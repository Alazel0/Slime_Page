import reflex as rx
from Slime_Page.styles.styles import Size

def link_button(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(tag="album"),
                rx.vstack(
                    rx.text(text),
                    margin=Size.ZERO.value
                )
            )
        ),
        href=url,
        is_external=True,
        width="100%"
    )

def login_page() -> rx.Component:
    return rx.vstack(
        link_button("Login with Discord", "/auth/discord"),
        link_button("Login with Twitter", "/auth/twitter"),
        spacing="1rem",
    )
