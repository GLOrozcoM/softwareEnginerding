/* ***********************************
 * CSCI205 - Software Engineering and Design
 * Spring 2017AD
 *
 * Names: CJ Blasi, Christina Caruso, Katherine Lordi, Leo Orozco
 * Date: Apr 29, 2017
 * Time: 11:07:38 PM
 * Project csci205_The_Slackers
 * Package: mainPackage
 * File: PreLevelTwo
 * Descripion:
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
 * Pre-level slides
 *
 * @author Leonard Orozco
 */
public class PreLevelTwo extends BasicGameState {

    /**
     * Constructor for the transition screen
     *
     * @param state An integer encoding the state of the transition.
     */
    public PreLevelTwo(int state) {
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
        graphics.drawString(
                "Flatley sighed with relief at leaving the King’s castle.\n"
                + "Afterall, one never knew when the King would hand out a quiz, and at times,\n"
                + "the King was known to bring out a guitar and play Billy Jean *gross*.\n"
                + "Luckily for Flatley, the King had been asleep dreaming about hair. \n\n\n"
                + "Flatley continued his journey through Flatland in search of this 'disturbance in the plane'.\n"
                + "Lord Monochrome had been somewhat vague describing this 'disturbance'.\n"
                + "Flatley decided to postpone imaginative musings about the 'disturbance'\n"
                + "until further information had been gathered.\n\n\n"
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
        // If space is pressed go to level two
        if (input.isKeyPressed(Input.KEY_SPACE)) {
            game.enterState(2);
        }
    }

    @Override // Returns the state ID
    public int getID() {
        return 103;
    }

}
