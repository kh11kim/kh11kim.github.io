import reflex as rx
from .base import h_spacing

def publication_card():
    return rx.card(
        rx.hstack(
            rx.image(
                src="/image/panda.jpg",
                ratio=1/1,
                height="10em",
            ),
            rx.box(
                rx.heading("Title of the paper", size="sm"),
                rx.text("author list"),
                rx.text("Name of the conference/journal", as_="i"),
                rx.text("some useful links"),
                h_spacing(10),
                rx.text("Very brief summary of the paper. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged."),
            ),
            gap=4,
        ),
    )

def publications():
    return rx.card(
        rx.vstack(
        publication_card(),
        publication_card(),
        publication_card(),
        publication_card()),
        header=rx.heading("Publications", size="md")
    )