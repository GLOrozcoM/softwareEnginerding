/* ***********************************
 * CSCI205 - Software Engineering and Design
 * Spring 2017AD
 *
 * Names: CJ Blasi, Christina Caruso, Katherine Lordi, Leo Orozco
 * Date: Apr 27, 2017
 * Time: 6:40:49 PM
 * Project csci205_The_Slackers
 * Package: mainPackage
 * File: PreMenu
 * Descripion: The first transition before game play.
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
 * Displays the first transition screen
 *
 * @author Leonard Orozco
 */
public class PreMenu extends BasicGameState {

    /**
     * Constructor for the transition screen
     *
     * @param state An integer encoding the state of the transition.
     */
    public PreMenu(int state) {
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
                "A number one New York Times bestseller three weeks in a row.\n"
                + "Like a series of unfortunate events, only this time, fortunate. - Daniel Handler\n"
                + "Winner of the 2017 Grammy and Oscar award. -The Academy\n"
                + "The only project in Bucknell CSCI 205 that was so original it made the English Department jealous. - J. Joyce\n"
                + "“A true delight. Reminiscent of a shot of kahlua.” - Antonio Banderas. \n"
                + "“A radical cross section of one square’s painful existence.”  - Dostoevsky \n"
                + "Like the Polar Plunge. Without all that awful coldness. - Kirsten Dunst \n"
                + "A shameless parody of life on the edge of 90 degrees. - Terrence Tao \n"
                + "Flatley is the real slim shady. -Eminem \n \n \n"
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
            game.enterState(102);
        }
    }

    @Override // Returns the PreMenu's state
    public int getID() {
        return 101;
    }
}
