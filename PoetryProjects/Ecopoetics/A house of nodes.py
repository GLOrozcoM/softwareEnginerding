### Never lose your will to why. That time will come.
### You will feel the tempting tug to not wish to see inside the black box.
### You will feel thirsty for the soda of ease and superficial understanding.
### But not today...

# Import statements.
# --There is nothing new under the moon.
from tkinter import *
from tkinter.ttk import *
from Somnium import *


# Overarching master window structure is declared.
# --On this house of leaves do I grow my trees.
master = Tk()

# Create title for master window.
# -- "You see Watson, the mind is like an attic. If you fill up the attic in a precise
# --  and organized manner, you will be able to access each part without any trouble at all."
# --  But what about the rest of the house? What kind of holy crawler lives outside of the attic?
master.title("The house in the mind.")


# Set the image to display as a label in the GUI.
# --The moon also falls.
photo = PhotoImage(file="spiraldesign.gif")

label = Label(master, image=photo).place(x=0, y=0, relwidth=1.0, relheight=1.0, anchor="nw", bordermode="outside")

# Declare new text label.
# --So tall was he. And so skinny as well.
anzo = Label(master, text="He firmly believed the truth was not as it appeared to him. ").grid(row= 0, column = 1)

# Creating an input prompt for the user.
# -- Why must you remain so passive while I must be active?
e1 = Entry(master)

# Set the user entry in the correct position.
# -- Grids are only as fun as they are nuf.
e1.grid(row=1, column=1)

# General text reading function.
# -- Neurons have words for breakfast, sentences for lunch, and a language for dinner.
# -- Then they die.
def read_poem_replace(poem_title):
    """Maintains the previous master window and opens up a new window with the new text."""

    # Call the random text extractor.
    # -- SUMMON THE DEAMON!
    daemon_full_tower()

    # Create title.
    # -- I am not ready to grudge.
    title = poem_title.replace('txt', '')

    # Create new window and title.
    # -- Yakuza no tamago.
    new_master = Toplevel()
    new_master.title(title)

    # Display the new poem to the window.
    # -- La matriz donde nacen las lineas virgines.
    p1 = open(poem_title, 'r')
    p1_lines = p1.readlines()
    p1_string = ''.join(p1_lines)
    Label(new_master, text=p1_string).grid(row=0)
    p1.close()

# General image reading function.
# -- Experiment with blindness #24301.
def read_image(img):
    """Function that shows an image in a new window of the program."""

    # TIME SEQUENCES

    # Create a new window, and set its geometry and title.
    # -- Black onyx shapes move...
    new_master = Toplevel()
    new_master.geometry("1000x750")
    new_master.resizable(0, 0)
    new_title = img.replace('.gif', '')
    new_master.title(new_title)

    # Create the new photo.
    # -- ...into my dreams...
    photo1 = PhotoImage(file=img)

    # Show the new photo as a label
    # -- ...and into your mares.
    new_label = Label(new_master, image=photo1)
    new_label.image = photo1
    new_label.place(x=0, y=0, relwidth=1.0, relheight=1.0, anchor="nw",
                    bordermode="outside")

# Sequentially produce the original poem sections in chronological order.
# -- If you wait, you can find the answer.
# -- If you don't wait, you can also find the answer.
def fukai():
    """fukai is a procedural function so no parameters or returns statements are found in it. """

    # The original texts.
    read_image("OriginalEntries/01.gif")
    read_image("OriginalEntries/02.gif")
    read_image("OriginalEntries/03.gif")
    read_image("OriginalEntries/04.gif")
    read_image("OriginalEntries/05.gif")
    read_image("OriginalEntries/06.gif")
    read_image("OriginalEntries/07.gif")
    read_image("OriginalEntries/08.gif")
    read_image("OriginalEntries/09.gif")
    read_image("OriginalEntries/10.gif")
    read_image("OriginalEntries/11.gif")
    read_image("OriginalEntries/12.gif")
    read_image("OriginalEntries/13.gif")
    read_image("OriginalEntries/14.gif")
    read_image("OriginalEntries/15.gif")
    read_image("OriginalEntries/16.gif")
    read_image("OriginalEntries/17.gif")
    read_image("OriginalEntries/18.gif")
    read_image("OriginalEntries/19.gif")
    read_image("OriginalEntries/20.gif")
    read_image("OriginalEntries/21.gif")
    read_image("OriginalEntries/22.gif")
    read_image("OriginalEntries/23.gif")
    read_image("OriginalEntries/24.gif")
    read_image("OriginalEntries/25.gif")
    read_image("OriginalEntries/26.gif")
    read_image("OriginalEntries/27.gif")
    read_image("OriginalEntries/28.gif")
    read_image("OriginalEntries/29.gif")
    read_image("OriginalEntries/30.gif")
    read_image("OriginalEntries/31.gif")
    read_image("OriginalEntries/32.gif")
    read_image("OriginalEntries/33.gif")
    read_image("OriginalEntries/34.gif")


# Room of words.
# -- Minotaurs.
def learn():

    master = Toplevel()
    b1 = Button(master, command=false_path_entry)
    b1.grid(row=10, column=0, sticky='W',pady=4)
    b2 = Button(master, text='Shoot.', command=false_path_entry)
    b2.grid(row=9, column=0, sticky='W', pady=4)
    b3 = Button(master, text='Yelps.', command=false_path_entry)
    b3.grid(row=8, column=0, sticky='W', pady=4)
    b4 = Button(master, text='Sweet land of liberty.', command=false_path_entry)
    b4.grid(row=7, column=0, sticky='W', pady=4)
    b5 = Button(master, text='To thee I pray a fervent prayer.', command=false_path_entry)
    b5.grid(row=6, column=0, sticky='W', pady=4)
    b6 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b6.grid(row=5, column=0, sticky='W', pady=4)
    b7 = Button(master, command=false_path_entry)
    b7.grid(row=4, column=0, sticky='W', pady=4)
    b8 = Button(master, text='Spiral.', command=false_path_entry)
    b8.grid(row=3, column=0, sticky='W', pady=4)
    b9 = Button(master, command=false_path_entry)
    b9.grid(row=2, column=0, sticky='W', pady=4)
    b10 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b10.grid(row=1, column=0, sticky='W', pady=4)
    b11 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b11.grid(row=0, column=0, sticky='W', pady=4)
    b12 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b12.grid(row=10, column=1, sticky='W', pady=4)
    b13 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b13.grid(row=9, column=1, sticky='W', pady=4)
    b14 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b14.grid(row=8, column=1, sticky='W', pady=4)
    b15 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b15.grid(row=7, column=1, sticky='W', pady=4)
    b16 = Button(master, text='Jimmy up.', command=false_path_entry)
    b16.grid(row=6, column=1, sticky='W', pady=4)
    b17 = Button(master, text='Transfer phosphates.', command=false_path_entry)
    b17.grid(row=5, column=1, sticky='W', pady=4)
    b18 = Button(master, text='Polygraphy.', command=false_path_entry)
    b18.grid(row=4, column=1, sticky='W', pady=4)
    b19 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b19.grid(row=3, column=1, sticky='W', pady=4)
    b20 = Button(master, text='Chasing Vermeer and another less savory ice cap.', command=false_path_entry)
    b20.grid(row=2, column=1, sticky='W', pady=4)
    b21 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b21.grid(row=1, column=1, sticky='W', pady=4)
    b22 = Button(master, text='Look a hot air ballon!', command=fukai)
    b22.grid(row=0, column=1, sticky='W', pady=4)
    b23 = Button(master, command=false_path_entry)
    b23.grid(row=10, column=2, sticky='W', pady=4)
    b24 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b24.grid(row=9, column=2, sticky='W', pady=4)
    b25 = Button(master, text='Too bad...', command=false_path_entry)
    b25.grid(row=8, column=2, sticky='W', pady=4)
    b26 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b26.grid(row=7, column=2, sticky='W', pady=4)
    b27 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b27.grid(row=6, column=2, sticky='W', pady=4)
    b28 = Button(master, text='Veritas', command=false_path_entry)
    b28.grid(row=5, column=2, sticky='W', pady=4)
    b29 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b29.grid(row=4, column=2, sticky='W', pady=4)
    b30 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b30.grid(row=3, column=2, sticky='W', pady=4)
    b31 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b31.grid(row=2, column=2, sticky='W', pady=4)
    b32 = Button(master, command=false_path_entry)
    b32.grid(row=1, column=2, sticky='W', pady=4)
    b33 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b33.grid(row=0, column=2, sticky='W', pady=4)
    b35 = Button(master, command=false_path_entry)
    b35.grid(row=10, column=3, sticky='W', pady=4)
    b36 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b36.grid(row=9, column=3, sticky='W', pady=4)
    b37 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b37.grid(row=8, column=3, sticky='W', pady=4)
    b38 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b38.grid(row=7, column=3, sticky='W', pady=4)
    b39 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b39.grid(row=6, column=3, sticky='W', pady=4)
    b40 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b40.grid(row=5, column=3, sticky='W', pady=4)
    b41 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b41.grid(row=4, column=3, sticky='W', pady=4)
    b42 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b42.grid(row=3, column=3, sticky='W', pady=4)
    b43 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b43.grid(row=2, column=3, sticky='W', pady=4)
    b44 = Button(master, text='The tower of words goes further.', command=false_path_entry)
    b44.grid(row=1, column=3, sticky='W', pady=4)
    b45 = Button(master, command=false_path_entry)
    b45.grid(row=0, column=3, sticky='W', pady=4)

# AI's that will write in background.
# -- How do you know that you didn't know?
def daemon_full_tower():
    """Upon this house do I spiral my continuous tower of language."""

    # Declare the file objects.
    # -- Upon and from this clay...
    file_1 = open("Crawler_text.txt", "a")
    file_2 = open("Full_Text.txt", "r")

    # Read in lines from the full text.
    # --...do I form a mold...
    lines_to_read = file_2.readlines()

    # Access a random line.
    # -- Randomness is very hard to achieve.
    index = randint(0, len(lines_to_read) - 1)

    print("The circuitrypen says: ", lines_to_read[index])

    # Write out the line chosen.
    # -- and etch out some Sumerians.
    file_1.write(lines_to_read[index])

    # Close all files.
    # -- Like a book.
    file_1.close()
    file_2.close()

# -- I'm so tired. LIfe is a tiring project. My dreams may lend me a sabbath.
# -- Eso espero.
def dreamer():
    """Function uses to call the cascade and space randomizer deamon."""

    # Sequentially call each part of the text manipulator.
    # -- AHA! --
    cuyo = Somnium()
    cuyo.maleficus()
    cuyo.genesis()
    cuyo.exodus()
    cuyo.cataracta()

# Main function that conditions to other poems in the text.
# -- The itsy bitsy spider...
def path_entry():

    # Entire list of conditions to each new text.
    # -- Mr. Nobody does not know which path to take.
    # -- Tell him to take any!

    if e1.get() == "accipio":
        learn()

    if e1.get() == "I":
        read_poem_replace("TypedEntries/Sonder's_eyes.txt")

    if e1.get() == "will":
        read_poem_replace("TypedEntries/Maybe_Cycles.txt")

    if e1.get() == "love":
        read_poem_replace("TypedEntries/Prometheus.txt")

    if e1.get() == "you":
        read_poem_replace("TypedEntries/Octopi_rain.txt")

    if e1.get() == "if":
        read_poem_replace("TypedEntries/Ifs.txt")

    if e1.get() == "wEvBm7":
        read_poem_replace("TypedEntries/The_4_0.txt")

    if e1.get() == "never":
        read_poem_replace("TypedEntries/The_bind.txt")

    if e1.get() == "see":
        read_poem_replace("TypedEntries/Cricket_leg.txt")

    if e1.get() == "e8DwMR":
        read_poem_replace("TypedEntries/Blithe_trash.txt")

    if e1.get() == "Dt2xzm":
        read_poem_replace("TypedEntries/Child_bird.txt")

    if e1.get() == ",":
        read_poem_replace("TypedEntries/Move_appropriately.txt")

    if e1.get() == "and":
        read_poem_replace("TypedEntries/No_digas.txt")

    if e1.get() == "VSFGAv":
        read_poem_replace("TypedEntries/Rain_remember.txt")

    if e1.get() == "x6UbBB":
        read_poem_replace("TypedEntries/Theatre.txt")

    if e1.get() == "ShGBuV":
        read_poem_replace("TypedEntries/Cabeza.txt")

    if e1.get() == "4MsVfG":
        read_poem_replace("TypedEntries/Jungle.txt")

    if e1.get() == "L6UjcF":
        read_poem_replace("TypedEntries/Liquor_apple.txt")

    if e1.get() == "z9Rqux":
        read_poem_replace("TypedEntries/Words_house.txt")

    if e1.get() == "rGpVBU":
        read_poem_replace("TypedEntries/Aztec.txt")

    if e1.get() == "g6zCvu":
        read_poem_replace("TypedEntries/Endgame.txt")

    if e1.get() == "every":
        read_poem_replace("TypedEntries/Outerness.txt")

    if e1.get() == "Tuesday":
        read_poem_replace("TypedEntries/Raining.txt")

    if e1.get() == "reading":
        read_poem_replace("TypedEntries/Ifs.txt")

    if e1.get() == "this":
        read_poem_replace("TypedEntries/Maps.txt")

    if e1.get() == "not":
        read_poem_replace("TypedEntries/My_mind_similar.txt")

    if e1.get() == "wearing":
        read_poem_replace("TypedEntries/Couple_smoked.txt")

    if e1.get() == "a":
        read_poem_replace("TypedEntries/Listen_to_the_clouds.txt")

    if e1.get() == "blindfold":
        read_poem_replace("TypedEntries/The_function_playground.txt")

    if e1.get() == "mientras":
        read_poem_replace("TypedEntries/The_poop_proof.txt")

    if e1.get() == "hay":
        read_poem_replace("TypedEntries/Sir.txt")

    if e1.get() == "esperanza":
        read_poem_replace("TypedEntries/Set_ignorance.txt")

    if e1.get() == "UK38mz":
        read_poem_replace("TypedEntries/Bloody_pen.txt")

    if e1.get() == "vida":
        read_poem_replace("TypedEntries/The_function_playground.txt")

# False path taken if the user presses the wrong button.
# -- There is only data and flow of information in a poem.
# -- "Well then fuck off because my data doesn't give a damn about
# --  your definition of poetry and my fist shall flow swiftly to your
# --  intellectual face."
def false_path_entry():
    """Any button other than true button will call this function."""

    # Call the crawler.
    # -- Demasiadas tormentas unden demasiados soldados.
    daemon_full_tower()

    # Call the dreamer.
    # -- Mr. Sandman....
    dreamer()

    # Create title.
    # -- Ahora o nunca mi chico.
    title = 'Where did you take me?'

    # Create new window.
    # -- Puertas nuevas para mundos nuevos.
    new_master = Tk()
    new_master.title(title)

    # Display the new poem to the window.
    # -- Not too late to learn something new.
    p1 = open("TypedEntries/Effendi.txt", 'r')
    p1_lines = p1.readlines()
    p1_string = ''.join(p1_lines)
    Label(new_master, text=p1_string).grid(row=0)
    p1.close()

# Button calls for next action.
# -- We are the sum of the buttons our friends push on us.

# Button events.
# -- P(E) = 1 - P(E^c)
def enterB0(event):
    b0.configure(text='Alas, we are stuck in heaven!')
def leaveB0(event):
    b0.configure(text='Look! A golden ratio.')
def enterB1(event):
    b1.configure(text='Je sui perdiu.')
def leaveB1(event):
    b1.configure(text='Quam?')
def enterB2(event):
    b2.configure(text='Alas, the Lord of hosts cries.')
def leaveB2(event):
    b2.configure(text='She said I was an asshole, but she did not explain why.')
def enterB3(event):
    b3.configure(text='Alas, the marble statues pray.')
def leaveB3(event):
    b3.configure(text='What is left for thee but do well in the sight of they Lord?')
def enterB4(event):
    b4.configure(text='Alas, the merchant of venice sings.')
def leaveB4(event):
    b4.configure(text='Locke responds with his lies.')
def enterB5(event):
    b5.configure(text='Alas, my friend tells me.')
def leaveB5(event):
    b5.configure(text='You are but an abortion of time.')
def enterB6(event):
    b6.configure(text='Alas, ring the bells of my neurons.')
def leaveB6(event):
    b6.configure(text='Timbre of thought.')
def enterB7(event):
    b7.configure(text='Alas, rivers of mercy upon thy head.')
def leaveB7(event):
    b7.configure(text='Oh.')
def enterB8(event):
    b8.configure(text='Alas, how green was my valley then!')
def leaveB8(event):
    b8.configure(text='A mechanism of strong thoughts.')
def enterB9(event):
    b9.configure(text='Alas, eloi eloi lama sabactani?')
def leaveB9(event):
    b9.configure(text='Though shalt know that I am but human.')
def enterB10(event):
    b10.configure(text='Alas, the room of branches doth grow a sprog.')
def leaveB10(event):
    b10.configure(text='LOOK NOT AT THE SPECIFIC BUT AT THE PATTERN.')
def enterB11(event):
    b11.configure(text='Alas, pray for me.')
def leaveB11(event):
    b11.configure(text='May he keep the czar far away from us!')
def enterB12(event):
    b12.configure(text='Alas, the tree of the righteouss must be watered.')
def leaveB12(event):
    b12.configure(text='The leftouss tree will water itself.')
def enterB13(event):
    b13.configure(text='Alas, como un aguila.')
def leaveB13(event):
    b13.configure(text='Vuela mi pajaro, vuela.')
def enterB14(event):
    b14.configure(text='Alas, the valley descends on my shadow.')
def leaveB14(event):
    b14.configure(text='The hyperion cantos.')
def enterB15(event):
    b15.configure(text='Alas, the rebels make this river run red.')
def leaveB15(event):
    b15.configure(text='How is it that a river runs like a color?')

# False buttons and true button declared.
# -- No woman can serve two masters. Maybe three?
b0 = Button(master, command=false_path_entry)
b0.grid(row=3, column=0, sticky='W', pady=4)
b0.bind('<Enter>', enterB0)
b0.bind('<Leave>', leaveB0)
b1 = Button(master, command=false_path_entry)
b1.grid(row=5, column=0, sticky='W', pady=4)
b1.bind('<Enter>', enterB1)
b1.bind('<Leave>', leaveB1)
b2 = Button(master, command=false_path_entry)
b2.grid(row=7, column=0, sticky='W', pady=4)
b2.bind('<Enter>', enterB2)
b2.bind('<Leave>', leaveB2)
b3 = Button(master, command=false_path_entry)
b3.grid(row=9, column=0, sticky='W', pady=4)
b3.bind('<Enter>', enterB3)
b3.bind('<Leave>', leaveB3)
b4 = Button(master, command=false_path_entry)
b4.grid(row=11, column=0, sticky='W', pady=4)
b4.bind('<Enter>', enterB4)
b4.bind('<Leave>', leaveB4)
b5 = Button(master, command=false_path_entry)
b5.grid(row=13, column=0, sticky='W', pady=4)
b5.bind('<Enter>', enterB5)
b5.bind('<Leave>', leaveB5)
# True button.
# -- The nail that stands out gets hammered in.
b6 = Button(master, command=path_entry)
b6.grid(row=15, column=0, sticky='W', pady=4)
b6.bind('<Enter>', enterB6)
b6.bind('<Leave>', leaveB6)
b7 = Button(master, command=false_path_entry)
b7.grid(row=17, column=0, sticky='W', pady=4)
b7.bind('<Enter>', enterB7)
b7.bind('<Leave>', leaveB7)
b8 = Button(master, command=false_path_entry)
b8.grid(row=4, column=2, sticky='W', pady=4)
b8.bind('<Enter>', enterB8)
b8.bind('<Leave>', leaveB8)
b9 = Button(master, command=false_path_entry)
b9.grid(row=6, column=2, sticky='W', pady=4)
b9.bind('<Enter>', enterB9)
b9.bind('<Leave>', leaveB9)
b10 = Button(master, command=false_path_entry)
b10.grid(row=8, column=2, sticky='W', pady=4)
b10.bind('<Enter>', enterB10)
b10.bind('<Leave>', leaveB10)
b11 = Button(master, command=false_path_entry)
b11.grid(row=10, column=2, sticky='W', pady=4)
b11.bind('<Enter>', enterB11)
b11.bind('<Leave>', leaveB11)
b12 = Button(master, command=false_path_entry)
b12.grid(row=12, column=2, sticky='W', pady=4)
b12.bind('<Enter>', enterB12)
b12.bind('<Leave>', leaveB12)
b13 = Button(master, command=false_path_entry)
b13.grid(row=14, column=2, sticky='W', pady=4)
b13.bind('<Enter>', enterB13)
b13.bind('<Leave>', leaveB13)
b14 = Button(master, command=false_path_entry)
b14.grid(row=16, column=2, sticky='W', pady=4)
b14.bind('<Enter>', enterB14)
b14.bind('<Leave>', leaveB14)
b15 = Button(master, command=false_path_entry)
b15.grid(row=18, column=2, sticky='W', pady=4)
b15.bind('<Enter>', enterB15)
b15.bind('<Leave>', leaveB15)

# Continue showing the window.
# -- We are happy in the loops we are not willing to leave.
mainloop( )