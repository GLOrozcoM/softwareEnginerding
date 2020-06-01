/* ***********************************
 * CSCI205 - Software Engineering and Design
 * Spring 2017AD
 *
 * Names: CJ Blasi, Christina Caruso, Katherine Lordi, Leo Orozco
 * Date: Apr 12, 2017
 * Time: 10:22:39 AM
 * Project csci205_The_Slackers
 * Package: mainPackage
 * File: Character
 * Descripion:
 * @author CJ Blasi
 * ***********************************

 */
package mainPackage;

import java.util.ArrayList;
import org.newdawn.slick.GameContainer;
import org.newdawn.slick.Graphics;
import org.newdawn.slick.Image;
import org.newdawn.slick.Input;
import org.newdawn.slick.SlickException;
import org.newdawn.slick.geom.Rectangle;
import org.newdawn.slick.state.StateBasedGame;

/**
 *
 *
 */
public class Character extends Sprite {

    public float x; // Character's x position
    public float y; // Character's y position
    public Image charImage; // Character's Image
    public Image eastCharImg; // Image facing East
    public Image westCharImg; // Image facing West
    protected float xAccel; // Char's acceleration in the x direction
    protected float yAcceleration; // Char's acceleration in the y direction
    protected int width; // Char's width
    protected int height; // Char's height
    public float xVel; // char's velocity in the x direction
    public float maxXVel; // char's max velocity for the x direction
    public float yVel; // Char's velocity in the y direction
    final protected double GRAVITY = 2.3; // Weight of the character
    protected double jumpStrength; // Strength of Character's jumps
    public boolean northTouch, southTouch, eastTouch, westTouch = false; // Boolean toggles for movement checking
    public boolean isTouchingPortal = false; // Boolean toggles for movement checking
    private final boolean isPortal = false; // Checks if the object is a portal
    public ArrayList<Sprite> obstacles;

    public Character(Image charImage, float x, float y, int width, int height,
                     double jumpStrength) throws SlickException {
        this.charImage = charImage;
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.xVel = 0;
        this.maxXVel = 10;
        this.yVel = 0;
        this.xAccel = 0;
        this.jumpStrength = jumpStrength;
        this.eastCharImg = this.charImage;
        if (charImage != null) {
            this.westCharImg = this.charImage.getFlippedCopy(true, false);
        }
    }

    @Override
    public void render(GameContainer container, StateBasedGame sbg, Graphics g) throws SlickException {
        g.drawImage(charImage, x, y);
    }

    public void update(GameContainer container, StateBasedGame sbg, int delta,
                       ArrayList<Sprite> obstacles) throws SlickException {

        Input input = container.getInput();

        this.obstacles = obstacles;

        float moveDist = 1.5f;

        collisionCheck();

        checkObjectCollision(obstacles, sbg, 1);

        if (northTouch == true) {
            this.yVel = 1;
        }
        if (eastTouch == true || westTouch == true) {
            this.xVel = 0;
            this.xAccel = 0;
        }

        // Not touching so movement is as usual.
        if (southTouch == false) {

            this.yAcceleration = (this.yAcceleration / (float) GRAVITY) + (float) jumpStrength;

            this.yVel += this.yAcceleration;
            if (this.yVel < 0) {
                this.y += checkMoveNorth(this.yVel, sbg);
            }
            if (this.yVel > 0) {
                this.y += checkMoveSouth(this.yVel, sbg);
            }
        }
        if (input.isKeyDown(Input.KEY_W) || input.isKeyDown(Input.KEY_UP)) {
            if (northTouch == false) {
                if (southTouch == true) {
                    this.yAcceleration = -2;
                    this.yVel = -5;
                    this.y += checkMoveNorth(this.yVel, sbg);
                }
            }
        }

        if (input.isKeyDown(Input.KEY_S)) {
            if (southTouch == false) {
                y += +1;
            }
        }

        if (input.isKeyDown(Input.KEY_D) || input.isKeyDown(Input.KEY_RIGHT)) {
            this.charImage = this.eastCharImg;
            if (eastTouch == false) {
                this.x += checkMoveEast(moveDist, sbg);
            }
        }

        if (input.isKeyDown(Input.KEY_A) || input.isKeyDown(Input.KEY_LEFT)) {
            this.charImage = this.westCharImg;
            if (westTouch == false) {
                moveDist *= -1;
                this.x += checkMoveWest(moveDist, sbg);
            }
        }
    }

    /**
     * Checks for collisions between objects in the room. Must pass in objects
     * to check as an array of sprites. Creates a series of 'sensors' on the
     * corners and center of the character one pixel from the character's edges
     * and checks to see if they encounter any barrier type objects.
     *
     * @param sprites The array of sprites to check collisions for.
     * @author CJ Blasi, Leonard Orozco, Katherine Lordi
     * @param sbg
     */
    public void checkObjectCollision(ArrayList<Sprite> sprites,
                                     StateBasedGame sbg, float moveDist) {

        // Address each sprite in the array and toggle the touching
        // flag in the original character class
        // Create a hitbox of the player
        turnOffTouches();

        // Check each sprite.
        checkMoveNorth(moveDist, sbg);

        checkMoveSouth(moveDist, sbg);

        checkMoveEast(moveDist, sbg);

        checkMoveWest(moveDist, sbg);

    }

    /**
     * Method to check if any of the narrators in the room are currently playing
     * their audio messages. Used to ensure that no narrator talks over the
     * other.
     *
     * @author Leonard Orozco
     */
    private boolean narratorsPlaying() {
        // Create an array of booleans to check whether a narrator is playing
        ArrayList<Boolean> playingList = new ArrayList<>();
        // Loop through every sprite in the room
        boolean result;
        for (Sprite sprite : obstacles) {
            // Make sure the sprite is of type narrator block
            if (sprite instanceof NarratorBlock) {
                // Check whether the narrator is playing any audio right now
                result = ((NarratorBlock) sprite).checkPlaying();
                // If so, add true to the final playing
                playingList.add(result);
            }
        }
        // We found a narrator talking so return true
        if (playingList.contains(true)) {
            return true;
        }
        // No narrators were talking so return false
        return false;
    }

    /**
     * Method that checks movement for the west
     *
     * @param moveDist
     * @param sbg
     * @return The maximum allowed movement
     * @author CJ Blasi, Katherine Lordi
     */
    public float checkMoveWest(float moveDist, StateBasedGame sbg) {
        float maxMove = moveDist;
        for (Sprite sprite : obstacles) {
            // Create a hitbox for the other objects.

            if (sprite.getClass() == this.getClass() && this == sprite) {
                continue;
            }
            if (sprite.canPassThrough() == false) {

                Rectangle otherHitBox = new Rectangle(sprite.getX(),
                                                      sprite.getY(),
                                                      sprite.getWidth(),
                                                      sprite.getHeight());
                // Check to see if the movement of the character will place the character
                // within the hitbox's radius
                if (otherHitBox.contains(x - moveDist, y)
                    || otherHitBox.contains(x - moveDist, y + height)
                    || otherHitBox.contains(x - moveDist, y + (height / 2))) {
                    // Check to see if this is a narrator block
                    if (sprite instanceof NarratorBlock) {

                        // Show the string message in the narrator
                        ((NarratorBlock) sprite).setNarrate(
                                true);
                        // No narrators are playing so we may turn on the narrator's audio
                        if (!narratorsPlaying()) {
                            // Play the narrator audio
                            ((NarratorBlock) sprite).turnSoundOn();
                        }

                    }
                    else {
                        // Turn all narrator renderings off
                        turnNarratorsOff();
                        westTouch = true;
                        this.x = otherHitBox.getX() + otherHitBox.getWidth();
                        maxMove = 0;
                        // Handle the case that we are encountering a portal
                        if (sprite.isPortal()) {
                            this.isTouchingPortal = true;
                        }
                    }
                }
            }
        }
        return maxMove;
    }

    public float checkMoveEast(float moveDist, StateBasedGame sbg) {
        float maxMove = moveDist;
        for (Sprite sprite : obstacles) {
            // Create a hitbox for the other objects.

            if (sprite.getClass() == this.getClass() && this == sprite) {
                continue;
            }
            if (sprite.canPassThrough() == false) {

                Rectangle otherHitBox = new Rectangle(sprite.getX(),
                                                      sprite.getY(),
                                                      sprite.getWidth(),
                                                      sprite.getHeight());
                if (otherHitBox.contains(x + width + moveDist, y)
                    || otherHitBox.contains(x + width + moveDist, y + height)
                    || otherHitBox.contains(x + width + moveDist,
                                            y + (height / 2))) {

                    if (sprite instanceof NarratorBlock) {
                        // Show the string message in the narrator
                        ((NarratorBlock) sprite).setNarrate(
                                true);
                        // No narrators are playing so we may turn on the narrator's audio
                        if (!narratorsPlaying()) {
                            // Play the narrator audio
                            ((NarratorBlock) sprite).turnSoundOn();
                        }
                    }
                    else {
                        // Turn all narrator renderings off
                        turnNarratorsOff();
                        eastTouch = true;
                        this.x = (otherHitBox.getX() - width);
                        maxMove = 1;
                        // Handle the case that we are encountering a portal
                        if (sprite.isPortal()) {
                            this.isTouchingPortal = true;
                        }
                    }
                }

            }
        }
        return maxMove;
    }

    private float checkMoveSouth(float moveDist, StateBasedGame sbg) {
        float maxMove = moveDist;
        for (Sprite sprite : obstacles) {
            // Create a hitbox for the other objects.

            if (sprite.getClass() == this.getClass() && this == sprite) {
                continue;
            }
            if (sprite.canPassThrough() == false) {

                Rectangle otherHitBox = new Rectangle(sprite.getX(),
                                                      sprite.getY(),
                                                      sprite.getWidth(),
                                                      sprite.getHeight());
                if (otherHitBox.contains(x, y + height + moveDist)
                    || otherHitBox.contains(x + width, y + height + moveDist)
                    || otherHitBox.contains(x + (width / 2),
                                            y + height + moveDist)) {

                    if (sprite instanceof NarratorBlock) {
                        // Show the string message in the narrator
                        ((NarratorBlock) sprite).setNarrate(
                                true);
                        // No narrators are playing so we may turn on the narrator's audio
                        if (!narratorsPlaying()) {
                            // Play the narrator audio
                            ((NarratorBlock) sprite).turnSoundOn();
                        }
                    }
                    else {
                        // Turn all narrator renderings off
                        turnNarratorsOff();
                        southTouch = true;
                        this.yAcceleration = 0;
                        this.yVel = 0;
                        this.y = otherHitBox.getY() - (height);
                        maxMove = 0;
                        // Handle the case that we are encountering a portal
                        if (sprite.isPortal()) {
                            this.isTouchingPortal = true;
                        }
                    }
                }

            }
        }
        return maxMove;
    }

    private float checkMoveNorth(float moveDist, StateBasedGame sbg) {
        float maxMove = moveDist;
        for (Sprite sprite : obstacles) {
            // Create a hitbox for the other objects.

            if (sprite.getClass() == this.getClass() && this == sprite) {
                continue;
            }
            if (sprite.canPassThrough() == false) {

                Rectangle otherHitBox = new Rectangle(sprite.getX(),
                                                      sprite.getY(),
                                                      sprite.getWidth(),
                                                      sprite.getHeight());
                if (otherHitBox.contains(x, y - moveDist)
                    || otherHitBox.contains(x + width, y - moveDist)
                    || otherHitBox.contains(x + (width / 2), y - moveDist)) {

                    if (sprite instanceof NarratorBlock) {
                        // Show the string message in the narrator
                        ((NarratorBlock) sprite).setNarrate(
                                true);
                        // No narrators are playing so we may turn on the narrator's audio
                        if (!narratorsPlaying()) {
                            // Play the narrator audio
                            ((NarratorBlock) sprite).turnSoundOn();
                        }
                    }
                    else {
                        // Turn all narrator renderings off
                        turnNarratorsOff();
                        northTouch = true;
                        this.y = otherHitBox.getY() + otherHitBox.getHeight();
                        maxMove = 0;
                        // Handle the case that we are encountering a portal
                        if (sprite.isPortal()) {
                            this.isTouchingPortal = true;
                        }
                    }

                }
            }
        }
        return maxMove;
    }

    /**
     * Method that will set all narrator renderings in the room obstacles to off
     *
     * @author Leonard Orozco
     */
    private void turnNarratorsOff() {
        // Loop through each obstacle in the room
        for (Sprite sprite : this.obstacles) {
            // Check if the sprite is of type narrator block
            if (sprite instanceof NarratorBlock) {
                // Turn off the narrator's rendering
                ((NarratorBlock) sprite).setNarrate(false);
            }
        }
    }

    @Override

    public int getWidth() {
        return width;
    }

    @Override

    public int getHeight() {
        return height;
    }

    @Override
    public float getX() {
        return x;
    }

    @Override
    public float getY() {
        return y;
    }

// NOT OUR METHOD
    public void collisionCheck() {

        if (this.x > 1600 - this.width) {
            this.x = 1600 - this.width;
        }

        else if (this.x < 0) {
            this.x = 0;
        }

        if (this.y > 1200 - this.height) {
            this.y = 1200 - this.height;
        }

        else if (this.y < 0) {
            this.y = 0;
        }

    }

    @Override
    public boolean isPortal() {
        return isPortal;
    }

    void turnOffTouches() {
        southTouch = false;
        northTouch = false;
        eastTouch = false;
        westTouch = false;
    }

    @Override
    public void setX(float x) {
        this.x = x;
    }

    @Override
    public void setY(float y) {
        this.y = y;
    }

    public void setCharImage(Image charImage) {
        if (this.charImage.equals(eastCharImg)) {
            this.charImage = charImage;
            this.eastCharImg = charImage;
            if (charImage != null) {
                this.westCharImg = charImage.getFlippedCopy(true, false);
            }
        }
        else {
            if (charImage != null) {
                this.charImage = charImage.getFlippedCopy(true, false);
            }
            this.eastCharImg = charImage;
            if (charImage != null) {
                this.westCharImg = charImage.getFlippedCopy(true, false);
            }

        }

    }

    @Override
    public boolean canPassThrough() {
        return false;
    }

}
