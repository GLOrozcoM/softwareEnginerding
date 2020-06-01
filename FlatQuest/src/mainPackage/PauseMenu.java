/* ***********************************
 * CSCI205 - Software Engineering and Design - Spring 2017AD
 *
 * Names: CJ Blasi, Christina Caruso, Katherine Lordi, Leo Orozco
 * Date: Apr 11, 2017
 * Time: 5:49:12 PM
 * Project csci205_The_Slackers
 * Package: mainPackage
 * File: PauseMenu
 * Descripion:
 * ***********************************
 */
package mainPackage;

import org.newdawn.slick.Color;
import org.newdawn.slick.GameContainer;
import org.newdawn.slick.Graphics;
import org.newdawn.slick.Input;
import org.newdawn.slick.SlickException;
import org.newdawn.slick.state.BasicGameState;
import org.newdawn.slick.state.StateBasedGame;

/**
 * The Pause Menu is a simple state that allows you to briefly step out of the
 * game (without letting you see the current game.)
 *
 * @author cjb030
 */
public class PauseMenu extends BasicGameState {

    /**
     * Constructor for the Menu
     *
     * @param state
     */
    public PauseMenu(int state) {
    }

    @Override // Maindatory override to fullfill abstractions for 'state'
    public void init(GameContainer gameContainer, StateBasedGame game)
            throws SlickException {
    }

    /**
     *
     * @param gameContainer
     * @param game
     * @param graphics
     * @throws SlickException
     */
    @Override
    public void render(GameContainer gameContainer, StateBasedGame game,
                       Graphics graphics)
            throws SlickException {
        // Set the background to the classic black screen
        //graphics.drawImage(new Image("src/resources/bg_Lvl_3.png"), 0, 0);
        graphics.setBackground(Color.gray);
        graphics.drawString("GAME PAUSED", Game.WIDTH / 2, Game.HEIGHT / 2);
    }

    /**
     *
     * @param gameContainer
     * @param game
     * @param delta Mandatory Parameter; Unused.
     * @throws SlickException
     */
    @Override
    public void update(GameContainer gameContainer, StateBasedGame game,
                       int delta)
            throws SlickException {
        Input input = gameContainer.getInput();
        if (input.isKeyPressed(Input.KEY_SPACE)) { // If pressed again, return to game.
            game.enterState(1);
        }
    }

    @Override // Returns the Pause Menu's state ID (2).
    public int getID() {
        return 10;
    }
}
