"""

First screen to welcome user.

"""
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.colorpicker import Color
from kivy.graphics import Rectangle
from functools import partial

def navigate_menu(screen_manager, *args):
    screen_manager.current = "menu_screen"

def continue_button(screen_manager):
    continue_btn = Button(text="Press here to start",
                          pos=(325, 250),
                          size_hint=(0.2, 0.2),
                          background_normal='',
                          background_down='',
                          background_color=(0, 0, 0.14, 1),
                          color=(1, 1, 1, 0.7))
    continue_btn.bind(on_release=partial(navigate_menu, screen_manager))
    return continue_btn

def create_version():
    version = Label(text="Version 1.0",
                    pos=(650, 10),
                    size_hint=(0.10, 0.10),
                    color=(1, 1, 1, 0.7))
    return version

def create_subtitle():
    subtitle = Label(text="Use chess pieces judiciously to visit every square on the board or "
                          "have a computer do it for you.",
                     pos=(0, 180),
                     color=(1, 1, 1, 0.7))
    return subtitle

def create_title():
    title = Label(text="Conquer the chess board!",
                  pos=(0, 250),
                  font_size='50sp',
                  color=(1, 1, 1, 0.7))
    return title

def create_author():
    author = Label(text="G.L.Orozco-Mulfinger",
                   pos=(80, 10),
                   size_hint=(0.1, 0.1),
                   color=(1, 1, 1, 0.7))
    return author

def generate_layout():
    layout = RelativeLayout()
    # Give background image to layout
    with layout.canvas.before:
        Color(0, 0, 0.14, 1)
        rect = Rectangle(size=(1000, 1000),
                         pos=layout.pos)
    return layout

def create_welcome_layout(screen_manager):

    layout = generate_layout()

    continue_btn = continue_button(screen_manager)
    author = create_author()
    title = create_title()
    subtitle = create_subtitle()
    version = create_version()

    layout.add_widget(continue_btn)
    layout.add_widget(author)
    layout.add_widget(title)
    layout.add_widget(subtitle)
    layout.add_widget(version)

    return layout