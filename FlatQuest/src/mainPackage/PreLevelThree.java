/* ***********************************
 * CSCI205 - Software Engineering and Design
 * Spring 2017AD
 *
 * Names: CJ Blasi, Christina Caruso, Katherine Lordi, Leo Orozco
 * Date: Apr 30, 2017
 * Time: 10:30:17 AM
 * Project csci205_The_Slackers
 * Package: mainPackage
 * File: PreLevelThree
 * Descripion: Transition between levels two and three
 * ***********************************
 */
package mainPackage;

import org.newdawn.slick.GameContainer;
import org.newdawn.slick.Graphics;
import org.newdawn.slick.Input;
import org.newdawn.slick.SlickException;
import org.newdawn.slick.state.BasicGameState;
import org.newdawn.slick.state.StateBasedGame;

/**
 * Class that renders the transition between levels two and three
 *
 * @author Leonard Orozco
 */
public class PreLevelThree extends BasicGameState {

    /**
     * Constructor for the transition screen
     *
     * @param state An integer encoding the state of the transition.
     */
    public PreLevelThree(int state) {
    }

    @Override // Maindatory override to fullfill abstractions for 'state'
    public void init(GameContainer gameContainer, StateBasedGame game)
            throws SlickException {
    }

    /**
     * Render method using Slick 2D's capabilities to display the transition's
     * text.
     *
     * @param gameContainer
     * @param game
     * @param graphics
     * @throws SlickException
     * @author Leonard Orozco
     */
    @Override
    public void render(GameContainer gameContainer, StateBasedGame game,
                       Graphics graphics)
            throws SlickException {
        // Display the funky text
        graphics.drawString("Flatley had found a friend in darkness.\n"
                            + "Flatley also realized an important fact: Flatley was not alone.\n\n\n"
                            + "'Goodwill Hunting' highlighted the plight of an intelligent individual who was never challenged.\n"
                            + "Luckily for Flatley, challenge was just around the corner."
                            + "Press space bar to continue ",
                            Game.WIDTH / 6, Game.HEIGHT / 4);
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
        // If space is pressed go to level three
        if (input.isKeyPressed(Input.KEY_SPACE)) {
            game.enterState(3);
        }
    }

    @Override // Returns the state ID
    public int getID() {
        return 104;
    }

}
