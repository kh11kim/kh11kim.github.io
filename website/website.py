import os

import reflex as rx

from .states import State
from .base import h_spacing
from .publications import *

def name():
    return rx.vstack(
        rx.heading(
            "Kanghyun Kim", font_size="2em"
        ),
        rx.text(
            "kh11kim at kaist.ac.kr",
            font_family="courier new",
            font_size="0.9em",
            color="gray"
        )
    )

def intro():
    return rx.vstack(
        rx.text(
            "Contents will be uploaded soon..! \
             Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, \
            when an unknown printer took a galley of type and scrambled it to make a type specimen book."),
        rx.text(
            "It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. \
            It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
    )

def aboutme():
    return rx.grid(
        rx.grid_item(
            name(),
            h_spacing(20),
            intro(),
            row_span=3, col_span=5
        ),
        rx.grid_item(
            "picture",
            row_span=3, col_span=2, bg="lightgreen"
        ),
        template_rows="repeat(3, 1fr)",
        template_columns="repeat(7, 1fr)",
        h="260px",
        gap=4,
    )

def link_buttons():
    return rx.center(rx.button_group(
        rx.button("CV", size="sm"),
        rx.text("/", font_size="20px", color="lightgray"),
        rx.button("Google Scholar", size="sm"),
        rx.text("/", font_size="20px", color="lightgray"),
        rx.button("Github", size="sm"),
        rx.text("/", font_size="20px", color="lightgray"),
        rx.button("LinkedIn", size="sm"),
        variant="ghost",
        font_family="courier new",
        spacing=8
    ))

def research():
    return rx.box(
        rx.heading("Research", size="md"),
        h_spacing(15),
        "It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. \
        It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
    )


def license():
    return rx.vstack(
        rx.box(h="10px"),
        rx.box(
            "Kanghyun Kim ⓒ 2023",
            font_family="courier new",
            font_size="0.85em",
            color="gray"
        ),
        rx.box(h="10px"),
)

def index():
    return rx.center(rx.box(
        h_spacing(100),
        aboutme(),
        h_spacing(20),
        link_buttons(),
        h_spacing(80),
        research(),
        h_spacing(50),
        publications(),
        h_spacing(50),
        license(),
        width="70%",
    ))

style = {
    "font_family": "Comic Sans MS",
    "font_size": "15px",
}

app = rx.App(style=style)
app.add_page(index, route="/", title="Kanghyun Kim")
app.compile()
