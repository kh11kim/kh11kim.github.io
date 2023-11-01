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
        rx.text("Contents will be uploaded soon..! \
            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, \
        when an unknown printer took a galley of type and scrambled it to make a type specimen book."),
        rx.text("It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. \
        It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
    )

def aboutme():
    return rx.hstack(
        rx.vstack(
            name(),
            h_spacing(30),
            intro(),
            max_width="500px"
        ),
        rx.center(
            rx.image(
                src="/image/20231002_145255.jpg",
                border_radius="50%"
            ),
            max_width="30%",
        ),
        spacing="1em",
    )

def link_buttons():
    def divider():
        return rx.text("|", font_size="20px", color="lightgray")
    return rx.center(rx.button_group(
        rx.button("CV"),
        divider(),
        rx.button("Google Scholar"),
        divider(),
        rx.button("Github"),
        divider(),
        rx.button("LinkedIn"),
        variant="ghost",
        #font_family="courier new",
        #font_size="0.85em"
        size="100px"
        #spacing=8
    ))

def research():
    return rx.card(
        rx.box("It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. \
         It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        ),
        header=rx.heading("Research", size="md"),
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
    return rx.center(
            rx.vstack(
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
                font_family="Nunito Sans",
                font_size="0.9em",
                max_width="95%",
            ),
            spacing="2em",
        )

STYLESHEETS = [
    "https://fonts.googleapis.com/css?family=Nunito+Sans",
]

app = rx.App(stylesheets=STYLESHEETS)
app.add_page(index, route="/", title="Kanghyun Kim")
app.compile()
