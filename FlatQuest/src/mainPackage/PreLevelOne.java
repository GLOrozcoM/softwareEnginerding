/* ***********************************
 * CSCI205 - Software Engineering and Design
 * Spring 2017AD
 *
 * Names: CJ Blasi, Christina Caruso, Katherine Lordi, Leo Orozco
 * Date: Apr 29, 2017
 * Time: 10:47:05 PM
 * Project csci205_The_Slackers
 * Package: mainPackage
 * File: PreLevelOne
 * Descripion: Displays the text before the first level.
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
 * Displays the second transition screen
 *
 * @author Leonard Orozco
 */
public class PreLevelOne extends BasicGameState {

    /**
     * Constructor for the transition screen
     *
     * @param state An integer encoding the state of the transition.
     */
    public PreLevelOne(int state) {
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
                "Flatland - A geometric plane of two dimensional figures.\n"
                + "In it, a young charming flatlander by the name of Flatley,\n"
                + "has been chosen by the king of Flatland, Lord Monochromatic, to steal away in the depths of night and\n"
                + "discover the source of a 'disturbance in the plane.' Flatley responded quite flatly to this summon\n"
                + "with a very submissive, 'Only if I have to.'\n"
                + "Armed with a firm undestanding of Euclid's fifth postulate, Flatley would take on anything.\n"
                + "Hopefully, this included the anomaly.\n\n\n"
                + "Press space to continue.",
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
        // If space is pressed return to the menu screen
        if (input.isKeyPressed(Input.KEY_SPACE)) {
            game.enterState(1);
        }
    }

    @Override // Returns the state ID
    public int getID() {
        return 102;
    }
}
