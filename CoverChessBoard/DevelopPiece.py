"""
Make a piece object that will interact with the board.

Ideas:
-> Make a child class of Button, that willl have a click status attribute.
As the attribute changes, so will its ability to interact with the rest of the board.
Let the board be "aware" of a piece by having a piece attribute and seeing if it has
been clicked.
-> Explore bindings.

"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout
from CoverChessBoard.ChessObjects import ChessBoard

"""
Right at press: on_press
Right after release: on_release
Abled or disabled (state): state
"""

# I want to change the color of the button after pressing it.
# Until pressed again.
# Toggle ultimately...
def after_color(instance):
    after_press_color = [1, 0.25, 0.58, 0.58]
    print("Changing color of button")
    instance.background_color = after_press_color

def before_color(instance):
    before_press_color = [1, 0.25, 0.58, 0.58]

class PieceButton(Button):

    def __init__(self, text, color):
        super().__init__(text = text)
        self.pressed = 0

        self.before_press_color = color
        self.background_color = self.before_press_color

        # Set pressed down color to original color
        self.background_down = str(self.background_color)

        # Purplish hue
        self.after_press_color = [1, 0.25, 0.58, 0.58]

    # TODO simplify with bitwise operations
    # TODO get background to not jump to disable background at all, blue between before and after colors
    def toggle_press(instance):
        if instance.pressed == 0:
            # Going from unpressed to pressed

            # Button has been pressed, after release, so change its color
            instance.background_color = instance.after_press_color
            instance.pressed = 1
            print("Toggled on")
            return
        # Going from pressed to unpressed
        instance.background_disabled_down = instance.after_press_color
        instance.background_color = instance.before_press_color
        instance.pressed = 0
        print("Toggled off")
        return


def toggle_press(instance):
    if instance.pressed == 0:
        # Going from unpressed to pressed
        # Button has been pressed, after release, so change its color
        instance.background_color = instance.after_press_color
        instance.pressed = 1
        print("Toggled on")
        return
    # Going from pressed to unpressed
    instance.background_color = instance.before_press_color
    instance.pressed = 0
    print("Toggled off")
    return

class Piece(ToggleButton):

    def __init__(self, piece_name):
        super().__init__()
        self.text = piece_name

    def print_state(self, instance, state_value):
        if state_value == 'normal':
            print("the state value is normal")
        else:
            print("the state value is down")

class Test(App):

    def build(self):

        btn = Piece('Piece')
        btn.bind(state = btn.print_state)

        return btn

the_piece = Test()
the_piece.run()