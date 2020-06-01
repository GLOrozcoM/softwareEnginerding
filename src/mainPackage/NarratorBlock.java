/* ***********************************
 * CSCI205 - Software Engineering and Design
 * Spring 2017AD
 * Names: CJ Blasi, Christina Caruso, Katherine Lordi, Leo Orozco
 * Date: Apr 18, 2017
 * Time: 8:08:10 PM
 * Project csci205_The_Slackers
 * Package: mainPackage
 * File: NarratorBlock
 * Descripion: Class that controls the workings for the Narrator Block.
 * ***********************************
 */
package mainPackage;

import org.newdawn.slick.GameContainer;
import org.newdawn.slick.Graphics;
import org.newdawn.slick.Image;
import org.newdawn.slick.SlickException;
import org.newdawn.slick.Sound;
import org.newdawn.slick.state.StateBasedGame;

/**
 *
 * Constructor for the Narrator Block.
 *
 * @author CJ Blasi, Leonard Orozco
 */
public class NarratorBlock extends Sprite {

    // Object coordinates
    public float x;
    public float y;
    // Object dimensions. Must be preset by the developer in terms of the
    // room object dimensions.
    private final int width = 40;
    private final int height = 40;
    // List of audio messages the Narrator can play.
    public Sound audioMessage;
    // Toggle the narration in the block
    public boolean narrate;
    // Boolean that determines the narrator block's status as a portal
    private final boolean isPortal = false;
    // Image to narrate
    public Image narrationImg;
    // String message
    public String stringMessage;

    /**
     *
     * Construct a NarratorBlock object. Notice that you will need to take in a
     * sound object.
     *
     * @param x_cor Object's x Position
     * @param y_cor Object's Y Position
     * @author CJ Blasi, Leonard Orozco
     */
    public NarratorBlock(float x_cor, float y_cor) {
        // Set up coordinates of the object
        this.x = x_cor;
        this.y = y_cor;
        // Initialize its narration to be false so as to not display the message yet
        this.narrate = false;
    }

    /**
     * Method that turns the sound on for the narrator if the message isn't
     * already playing
     *
     * @author Leonard Orozco
     */
    public void turnSoundOn() {
        // Only allow the sound to turn on if the audio message isn't
        // already playing.
        if (!this.audioMessage.playing()) {
            this.audioMessage.play();
        }
    }

    /**
     * Method based on Slick2D's render. Check the API for more information.
     *
     * @param container
     * @param sbg
     * @param g
     * @throws SlickException
     */
    @Override
    public void render(GameContainer container, StateBasedGame sbg, Graphics g) throws SlickException {
        // Only render if the audio message is playing.
        if (this.narrate) {
            g.drawString(this.stringMessage,
                         x + 50,
                         y + 50);

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
        return this.x;
    }

    @Override
    public float getY() {
        return this.y;
    }

    /**
     * Method that checks to see if the narrator is playing right now.
     */
    public boolean checkPlaying() {
        return this.audioMessage.playing();
    }

    /**
     * Method that toggles the narration to true or false
     *
     * @author CJ Blasi
     */
    public void toggleNarate() {
        if (this.narrate) {
            this.narrate = false;
        }
        else {
            this.narrate = true;
        }
    }

    public void setNarrate(boolean narrate) {
        this.narrate = narrate;
    }

    /**
     * Method that toggles the narration to true or false
     *
     * @author CJ Blasi
     */
    public void toggleNarrate() {
        if (this.narrate) {
            this.narrate = false;
        }
        else {
            this.narrate = true;
        }
    }

    public Sound getAudioMessage() {
        return audioMessage;
    }

    public void setAudioMessage(Sound audioMessage) {
        this.audioMessage = audioMessage;
    }

    public Image getNarrationImg() {
        return narrationImg;
    }

    @Override
    public boolean isPortal() {
        return this.isPortal;
    }

    public boolean isNarrate() {
        return narrate;
    }

    @Override
    public boolean canPassThrough() {
        return false;
    }

    @Override
    public void setX(float x) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public void setY(float y) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

}
