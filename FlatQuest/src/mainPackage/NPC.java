/* ***********************************
 * CSCI205 - Software Engineering and Design
 * Spring 2017AD
 *
 * Names: CJ Blasi, Christina Caruso, Katherine Lordi, Leo Orozco
 * Date: Apr 25, 2017
 * Time: 3:21:59 PM
 * Project csci205_The_Slackers
 * Package: mainPackage
 * File: NPC
 * Descripion:
 * ***********************************
 */
package mainPackage;

import org.newdawn.slick.Animation;
import org.newdawn.slick.GameContainer;
import org.newdawn.slick.Graphics;
import org.newdawn.slick.SlickException;
import org.newdawn.slick.SpriteSheet;
import org.newdawn.slick.state.StateBasedGame;

/**
 *
 * @author cjb030
 */
public class NPC extends Sprite {

    private float x;
    private float y;
    private int width;
    private int height;
    private SpriteSheet sSheet;
    public Animation sAnimation;

    public NPC(SpriteSheet sSheet, float x, float y, int width, int height) {
        this.x = x;
        this.y = y;
        this.height = height;
        this.width = width;
        this.sSheet = sSheet;
        this.sAnimation = new Animation(sSheet, 100);
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

    @Override
    public void setX(float x) {
        this.x = x;
    }

    @Override
    public void setY(float y) {
        this.y = y;
    }

    @Override
    public boolean isPortal() {
        return false;
    }

    @Override
    public void render(GameContainer container, StateBasedGame sbg, Graphics g) throws SlickException {
        sAnimation.setCurrentFrame(23);
        sAnimation.draw(x, y);

    }

    @Override
    public boolean canPassThrough() {
        return false;
    }

}
