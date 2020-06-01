/* ***********************************
 * CSCI205 - Software Engineering and Design
 * Spring 2017AD
 *
 * Names: CJ Blasi, Christina Caruso, Katherine Lordi, Leo Orozco
 * Date: Apr 30, 2017
 * Time: 2:10:42 PM
 * Project csci205_The_Slackers
 * Package: mainPackage
 * File: PreLevelFive
 * Descripion: Flatley's thoughts before level five
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
 * Transition between levels four and five
 *
 * @author Leonard Orozco
 */
public class PreLevelFive extends BasicGameState {

    /**
     * Constructor for the transition screen
     *
     * @param state An integer encoding the state of the transition.
     */
    public PreLevelFive(int state) {
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
                "Having experienced something sublime (a word which here means 'terrible and beautiful at once'),\n"
                + "Flatley knew it wanted to get to the bottom (or to the top and sides) of this anomaly.\n"
                + "That part of the world hadn't been half bad afterall. It had only been one fourth bad. \n\n\n"
                + "In everyone's life, there is 'this is it, the defining point of my life' moment.\n"
                + "For the Russian authors, it was the Tolstoy's Anna Karennina that did it.\n"
                + "For Flatley, it was the next thing it saw...\n\n\n"
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
        // If space is pressed go to level 5
        if (input.isKeyPressed(Input.KEY_SPACE)) {
            game.enterState(5); // Change to go directly to level 5
        }
    }

    @Override // Returns the state ID
    public int getID() {
        return 106;
    }

}
