"""
This module was built to encapsulate the bottom buttons that may help a user to go back.
"""
from kivy.uix.button import Button
from functools import partial

def back_btn_callback(*args, screen_manager):
    screen_manager.current = "menu_screen"

def create_back_button(screen_manager):
    back_btn = Button(text="Go back",
                      background_normal='',
                      background_down='',
                      background_color=(0, 0, 0.14, 1),
                      color=(1, 1, 1, 0.7))
    back_btn.bind(on_release=partial(back_btn_callback, screen_manager=screen_manager))
    return back_btn