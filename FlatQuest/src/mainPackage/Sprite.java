/* ***********************************
 * CSCI205 - Software Engineering and Design - Spring 2017AD
 *
 * Names: CJ Blasi, Christina Caruso, Katherine Lordi, Leo Orozco
 * Date: Apr 11, 2017
 * Time: 6:20:43 PM
 * Project csci205_The_Slackers
 * Package: mainPackage
 * File: Sprite
 * Descripion:
 * ***********************************
 */
package mainPackage;

import org.newdawn.slick.GameContainer;
import org.newdawn.slick.Graphics;
import org.newdawn.slick.SlickException;
import org.newdawn.slick.state.StateBasedGame;

/**
 *
 * @author cjb030
 */
public abstract class Sprite {

    public abstract int getWidth(); // Abstract method returns the sprite's width.

    public abstract int getHeight(); // Abstract method returns the sprite's height.

    public abstract float getX(); // Abstract method returns sprite's x position.

    public abstract float getY(); // Abstract method returns sprite's y position.

    // Setters
    public abstract void setX(float x);

    public abstract void setY(float y);

    public abstract boolean isPortal(); // Abstract method returns true if the object is a portal.

    public abstract boolean canPassThrough();

    public abstract void render(GameContainer container, StateBasedGame sbg,
                                Graphics g) throws SlickException;

    /**
     * Checks to see if two sprites are touching by seeing whether their x & y
     * values exist in the other's width and height.
     *
     * @param other The other sprite being tested for contact.
     * @return
     */
    public boolean touching(Sprite other) {
        return this.getX() < other.getX() + other.getWidth() && this.getX() + getWidth() > other.getX() && this.getY() < other.getY() + other.getHeight() && this.getY() + getHeight() > other.getY();
    }

}
