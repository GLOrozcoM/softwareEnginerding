/* ***********************************
 * CSCI205 - Software Engineering and Design
 * Spring 2017AD
 *
 * Names: CJ Blasi, Christina Caruso, Katherine Lordi, Leo Orozco
 * Date: Apr 12, 2017
 * Time: 3:38:00 PM
 * Project csci205_The_Slackers
 * Package: mainPackage
 * File: Barrier
 * Descripion:
 * ***********************************
 */
package mainPackage;

import org.newdawn.slick.GameContainer;
import org.newdawn.slick.Graphics;
import org.newdawn.slick.Image;
import org.newdawn.slick.SlickException;
import org.newdawn.slick.state.StateBasedGame;

/**
 *
 * @author cjb030
 */
public class Barrier extends Sprite {

    // Cardinal coordinates
    public float x;
    public float y;

    // Dimensions of object
    private int width;
    private int height;
    private boolean notSolid = false;

    // Image associated with the object
    private Image barImage;

    // Boolean determining whether this is a portal or not.
    private boolean isPortal = false;

    /**
     *
     * @param image
     * @param x
     * @param y
     */
    public Barrier(Image image, float x, float y) {
        this.x = x;
        this.y = y;
        this.barImage = image;
        this.width = barImage.getWidth();
        this.height = barImage.getHeight();
    }

    @Override
    public void render(GameContainer container, StateBasedGame sbg, Graphics g) throws SlickException {
        g.drawImage(barImage, x, y);

    }

    // Setters
    @Override
    public void setX(float x) {
        this.x = x;
    }

    public void setPassThrough() {
        notSolid = true;
    }

    @Override
    public void setY(float y) {
        this.y = y;
    }

    @Override
    public int getWidth() {
        return width;
    }

    @Override
    public int getHeight() {
        return height;
    }

    Image getImage() {
        return barImage;
    }

    @Override
    public float getX() {
        return this.x;
    }

    @Override
    public float getY() {
        return this.y;
    }

    @Override
    public boolean isPortal() {
        return isPortal;
    }

    @Override
    public boolean canPassThrough() {
        return notSolid;
    }

}
