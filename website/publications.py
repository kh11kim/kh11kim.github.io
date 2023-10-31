import reflex as rx
from .base import h_spacing

def publication_card():
    return rx.box(rx.grid(
            rx.grid_item(
                "figure",
                row_span=3, col_span=2, bg="lightgreen"
            ),
            rx.grid_item(
                rx.heading("Title of the paper", size="sm"),
                rx.text("author list"),
                rx.text("Name of the conference/journal", as_="i"),
                rx.text("some useful links"),
                h_spacing(10),
                rx.text("Very brief summary of the paper. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged."),
                row_span=3, col_span=6
            ),
            template_rows="repeat(3, 1fr)",
            template_columns="repeat(8, 1fr)",
            h="170px",
            gap=4,
        ),
        h_spacing(15),
    )

def publications():
    return rx.box(
        rx.heading("Publications", size="md"),
        h_spacing(15),
        publication_card(),
        publication_card(),
        publication_card(),
        publication_card()
    )