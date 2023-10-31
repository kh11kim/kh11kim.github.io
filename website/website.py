import os

import reflex as rx

from .states import State

def index():
    return rx.center(
        rx.box("hello world")
    )

app = rx.App()
app.add_page(index, route="/")
app.compile()
