/* ***********************************
 * CSCI205 - Software Engineering and Design
 * Spring 2017AD
 *
 * Names: CJ Blasi, Christina Caruso, Katherine Lordi, Leo Orozco
 * Date: Apr 12, 2017
 * Time: 3:38:00 PM
 * Project csci205_The_Slackers
 * Package: mainPackage
 * File: Portal
 * Descripion: Class containing the wonders of the portal object.
 * ***********************************
 */
package mainPackage;

import org.newdawn.slick.GameContainer;
import org.newdawn.slick.Graphics;
import org.newdawn.slick.Image;
import org.newdawn.slick.SlickException;
import org.newdawn.slick.state.StateBasedGame;

/**
 * Class designed to handle the portal objects found in each level.
 *
 * @author Leonard Orozco
 */
public class Portal extends Sprite {

    // Portal coordinates
    public float x;
    public float y;

    // Portal dimensions
    private int width = 20;
    private int height = 20;

    // Image associated with the portal.
    private Image portalImg;

    // Boolean that checks if this is a portal.
    private boolean isPortal = true;

    /**
     * Construct a portal object based on desired coordinates.
     *
     * @param image Image associated with the portal object
     * @param x_cor X coordinate
     * @param y_cor Y coordinate
     * @author Leonard Orozco
     */
    public Portal(Image image, float x_cor, float y_cor) {

        // Set up coordinates
        this.x = x_cor;
        this.y = y_cor;

        // Set up the associated image
        this.portalImg = image;

    }

    /**
     * Method based on Slick2D's render. Check the API for more information.
     *
     * @param container
     * @param sbg
     * @param g
     * @throws SlickException
     * @author Leonard Orozco
     */
    @Override
    public void render(GameContainer container, StateBasedGame sbg, Graphics g) throws SlickException {
        // Draw the image of the portal (note this is not a regular rectangle call)
        g.drawImage(portalImg, x, y);
    }

    // Getters and setters
    @Override
    public int getWidth() {
        return width;
    }

    @Override
    public int getHeight() {
        return height;
    }

    Image getImage() {
        return portalImg;
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
    public void setX(float x) {
        this.x = x;
    }

    @Override
    public void setY(float y) {
        this.y = y;
    }

    @Override
    public boolean canPassThrough() {
        return false;
    }

    public void setWidth(int width) {
        this.width = width;
    }

    public void setHeight(int height) {
        this.height = height;
    }

}
