# Program designed to revise 304 poems randomly
# - I wonder what Atticus carries in the briefcase.

#  Import statements
# - I still wish there were more new things under this sun
import os
from random import randint
from random import sample
from random import choices

# Method definitions
# -- skyscrapers
def dig_root():
    # Acquire the current working directory
    # - The journey of a thousand cliche's starts with the first one
    foundation = os.getcwd()
    # Acquire the files within the current directory
    # - Humpty's pieces
    humpty = [f for f in os.listdir(foundation) if os.path.isfile(f)]
    # Remove the DS store file
    # - Lollipops and sticky like the sun
    humpty.pop(0)
    return humpty

def cast_members(files):
    # Populate lists to include the files associated with revisions, comments, and originals
    # - Warehouses of future explosive comments
    bang_set = list()
    boom_set = list()
    crash_set = list()
    for file in files:
        # Originals
        if (".txt" in file and "R" not in file and "C" not in file):
            bang_set.append(file)
        # Revisions
        elif (".txt" in file and "R" == file[0]):
            boom_set.append(file)
        # Comments
        elif (".txt" in file and "C" == file[0]):
            crash_set.append(file)

    return bang_set, boom_set, crash_set

def charged_field(rev_choice):
    # Sample how many to revise from the original poetry
    bang_N = randint(1, len(bang_set))
    # Sample to pick from in the revisions
    boom_N = randint(1, len(boom_set))
    # Sample to pick from in the comments section
    crash_N = randint(1, len(crash_set))

    # Randomly create a list that will contain the text we want to revise
    # -- Choice 1
    tortoise = randint(1, len(bang_set))
    i = tortoise
    bang_rev = list()
    while i < bang_N:
        bang_rev.append(bang_set[i % bang_N])  # Populate the container for the true originals
        i += 1  # Today, we avoid the infinite loop

    # Establish the revision choice
    rev_choice = rev_choice

    # Randomly pick what text you want to use to revise from
    # Note that we MUST have the exact same number as bang_rev
    boom_rev = list()
    hare = len(bang_rev)
    j = 0
    while j < hare:
        # Want to revise from revision text
        if rev_choice == 1:
            boom_rev.append(boom_set[j % boom_N])
        elif rev_choice == 2:
            boom_rev.append(crash_set[j % crash_N])
        j += 1

    return bang_rev, boom_rev

def fields(bull, ox_lines, eco_lines):
    # Revise each file in the bang_rev
    # -- make certain we are not working empty handed
    if len(bang_rev) != 0:
        # - Store all the wonderful lines to revise
        # --- Note that this will become a 2 dimensional list
        these_lines = list()
        for file in bang_rev:
            # Read the lines in
            with open(file) as og_file:
                these_lines.append(og_file.readlines())
        # - Store all the wonderful lines we will use as revisions
        those_lines = list()
        for file in boom_rev:
            # Read them in!
            with open(file) as rev_file:
                those_lines.append(rev_file.readlines())

        # Allow for pulling from oxford and ecopoetics
        if bull == 2:
            those_lines = ox_lines
        elif bull == 3:
            those_lines = eco_lines

        # We made it thus far.
        # Now, consider choosing which line to modify
        # Looping through each file
        for index in range(0, len(these_lines)):

            # Now in a separate file
            # -- Want to determine how many lines to revise
            n_sample = randint(0, len(these_lines[index]))
            # -- Want to determine which lines to revise
            og_sample = sample(range(0, len(these_lines[index])), n_sample)
            rev_sample = choices(range(0, len(those_lines[index])), k=n_sample)

            # Revise the lines we chosen
            for interior in range(0, n_sample):
                og_index = og_sample[interior]
                rev_index = rev_sample[interior]
                these_lines[index][og_index] = those_lines[index][rev_index]

        # Write out the revised lines in a new file according to its experimented file
        # Write out the new revised lines
        for i in range(len(bang_rev)):
            name = "Investigate" + bang_rev[i]
            outF = open(name, "w")
            outF.writelines(these_lines[i])
            outF.close()




            # Print out sampled sets

# Script in action
# -- an insect launch

# Get the current directory files and clean theme
humpty = dig_root()

# Populate the sets that will contain all text
bang_set, boom_set, crash_set = cast_members(humpty)

# Randomly pick the source for revisions
rev_choice = randint(1, 2)

# Extract two sets that will revise each other
bang_rev, boom_rev = charged_field(rev_choice)

# Obtain the Oxford lines
ox_lines = list()
with open("Oxford_English_Dictionary.txt") as ox_file:
    ox_lines.append(ox_file.readlines())

# Obtain the Ecological lines
eco_lines = list()
with open("Full_Text.txt") as eco_file:
    eco_lines.append(eco_file.readlines())

# Perform, now.
my_bull = randint(1, 3)
fields(my_bull, ox_lines, eco_lines)
