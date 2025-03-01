import reflex as rx
import Slime_Page.styles.styles as styles

def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        style= styles.title_style
    )