from random import *

class Somnium:
    """Class which takes in a text file and outputs a randomly spaced text
    using randomly chosen words from the text."""

    def __init__(self, file = "Full_text.txt"):
        """Specify from which file to take in the words."""
        self.file = file
        self.lines = None
        self.blocks = []

    def maleficus(self):
        """Reads in lines from file to the class attribute."""
        assert self.file != None, "Why dost thou not pass in a file?"
        file = open(self.file, "r")
        self.lines = file.readlines()

    def genesis(self):
        """Splits lines into discrete blocks. Each block is however, picked randomly."""
        assert self.lines is not None, "Why dost thou have no lines?"

        # Specify a sample size.
        sample_size = randint(1, 20)

        # Declare the randomly chosen numbers to pick from the lines.
        numbers = sample(range(0, len(self.lines) - 1), sample_size)

        # Loop over each number and assign it to the block attribute.
        for num in numbers:
            split_list = self.lines[num].split()
            self.blocks += split_list

    def exodus(self):
        """Draws out a random output of space conscious words."""
        assert self.blocks != [], "Why dost thou not have blocks?"

        # Prepare the file to write out to.
        file = open("Exodus.txt", "a")

        # Create an empty string to store in the final block.
        etchings = ''

        for block in self.blocks:

            # Randomly pick the number of spaces and new lines.
            num_spaces1 = randint(0,5)
            num_lines = randint(0,3)
            num_spaces2 = randint(0, 10)

            # Store in the string.
            # To understand the parsing, notice the order: spaces, then the block of text, then spaces, then
            # the new lines. Spaces and new lines are chosen randomly from the integers above.
            etchings += num_spaces1 * " " + block + num_spaces2 * " " + num_lines * '\n'

        # Write to the file and close it.
        file.write(etchings)
        file.close()

        # Return in case the it needs to be printed to the console
        return etchings

    def cataracta(self):
        """Outputs text randomly in a "waterfall" like spacing. """
        assert self.blocks != [], "Why dost thou not have blocks?"

        # Prepare file to write out.
        file = open("Caracta.txt", 'a')

        # Declare string to store the waterfall in.
        waterfall = ''

        # Declare the number of spaces variable.
        spaces = 3

        # Loop that creates the text waterfall.
        for block in self.blocks:

            # Spaces first, then text, then a new line.
            waterfall += spaces * " " + block + "\n"

            # Increment the number of spaces for the next block of text.
            spaces += 2

        # Write and close to the file.
        file.write(waterfall)
        file.close()

        # Return the string in case printing to the console is necessary.
        return waterfall





