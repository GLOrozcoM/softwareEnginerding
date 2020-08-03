# softwareEnginerding

This repository contains projects I contributed to or personally completed in software engineering.

## Table of contents
* [General info](#general-info)
* [FlatQuest](#FlatQuest)
* [Conquer the Chess Board](#Cover-Chess-Board)

## General Info

[FlatQuest](#FlatQuest) (2017)
was a culminating project for a software engineering course designed
to teach fundamental development practices. I GitHubbed and Scrummed for this project in a team with three other undergraduate
students. [Conquer the Chess Board](#Cover-Chess-Board) (2020) came about after wondering how 
I could solve the knight's tour, and realizing a computer would make it all easier.
I implemented a backtracking algorithm and designed a GUI to visualize the solution.

## FlatQuest

Inspired by exacting professors and the desire to build a beautiful game, I collaborated in a
team of four undergraduate students to produce a quirky side scrolling platforming game.

![Level one](Images/LevelOne.png)

The game follows Flatley, a square, as it progresses through various levels in FlatLand.
I won't spoil the story line here, but we drew a small bit of inspiration from Edwin Abbott's
book - Flatland, and Thomas Was Alone's narration style.

![Level two](Images/LevelTwo.png)

## Gameplay

![Residential](Images/Residential.png)

● Use ‘WASD’ or the arrow keys to move Flatly around the screen to explore new territory

● Press ‘Q’ to spawn and despawn Flatly’s shadow to assist with high jumps

● ‘SHIFT’ to to switch between controlling Flatly or his shadow

● ‘SPACE’ to pause the game

● Explore the level until Flatly finds a portal in order to proceed to the next level (5 total
levels)

Tips:

● Read the text to fully immerse yourself in Flatly’s story and world (*** and also get a few
hints of how to succeed in the game along the way ***)

● Button trick for a high jump: ‘W’ -> ‘Q’ -> ‘W’ -> ‘SHIFT’

● Explore the level to find hidden narration

#### How to access

Navigate to the FlatQuest/dist folder and click on the FlatQuest.jar file. The file has been configured to run
as an executable so no need for programming IDE's!

#### Musical notes

The music used for the game is by Dexter Britain and is under a cc license (check him out at www.dexterbritain.com).

#### Packages used

We used Slick2D as the base for the game development.

## Conquer the Chess Board

A classic chess problem is the knight's tour. The player must use a knight to cover
every square on the chess board. The only constraint is the knight must pass through 
each square only once. Since the knight has a tricky movement scheme in chess, figuring
out a path for covering each square in an 8 by 8 board (64 squares total) is not easy.

I designed a GUI to explore this problem. The user can  


#### How to run

Navigate to CoverChessBoard, src, GUI, and run main.py.

#### Packages used

* kivy
* collections
