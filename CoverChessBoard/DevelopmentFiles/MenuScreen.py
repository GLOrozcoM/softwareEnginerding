"""

Menu screen to navigate app.

"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.colorpicker import Color
from kivy.graphics import Rectangle

def create_computer_button():
    computer_btn = Button(text="Have the computer conquer for you",
                          pos=(325, 110),
                          size_hint=(0.2, 0.2),
                          background_normal='',
                          background_down='',
                          background_color=(0, 0, 0.14, 1),
                          color=(1, 1, 1, 0.7))
    return computer_btn

def create_conquer_button():
    conquer_btn = Button(text="Try to conquer the board yourself",
                         pos=(325, 210),
                         size_hint=(0.2, 0.2),
                         background_normal='',
                         background_down='',
                         background_color=(0, 0, 0.14, 1),
                         color=(1, 1, 1, 0.7))
    return conquer_btn

def create_concept_button():
    concept_btn = Button(text="Get the process explained",
                         pos=(325, 310),
                         size_hint=(0.2, 0.2),
                         background_normal='',
                         background_down='',
                         background_color=(0, 0, 0.14, 1),
                         color=(1, 1, 1, 0.7))
    return concept_btn

def create_title():
    title_lbl = Label(text="What would you like to do?",
                      pos=(0, 250),
                      font_size='40sp',
                      color=(1, 1, 1, 0.7))
    return title_lbl

def generate_layout():
    layout = RelativeLayout()
    # Give background image to layout
    with layout.canvas.before:
        Color(0, 0, 0.14, 1)
        rect = Rectangle(size=(1000, 1000),
                         pos=layout.pos)
    return layout

def create_menu_layout():
    layout = generate_layout()

    title_lbl = create_title()
    concept_btn = create_concept_button()
    conquer_btn = create_conquer_button()
    computer_btn = create_computer_button()

    layout.add_widget(title_lbl)
    layout.add_widget(concept_btn)
    layout.add_widget(conquer_btn)
    layout.add_widget(computer_btn)
    return layout

