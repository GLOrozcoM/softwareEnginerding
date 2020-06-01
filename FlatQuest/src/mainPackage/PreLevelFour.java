/* ***********************************
 * CSCI205 - Software Engineering and Design
 * Spring 2017AD
 *
 * Names: CJ Blasi, Christina Caruso, Katherine Lordi, Leo Orozco
 * Date: Apr 30, 2017
 * Time: 10:43:20 AM
 * Project csci205_The_Slackers
 * Package: mainPackage
 * File: PreLevelFour
 * Descripion: Flatley's thoughts and description between levels three and four
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
 * Transition between levels three and four
 *
 * @author Leonard Orozco
 */
public class PreLevelFour extends BasicGameState {

    /**
     * Constructor for the transition screen
     *
     * @param state An integer encoding the state of the transition.
     */
    public PreLevelFour(int state) {
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
        graphics.drawString("Flatley felt its diodes creak and croak in pain.\n"
                            + "Apparently, shadow hopping is about as strenuous (and maybe even as undignified)\n"
                            + "as a 1980’s aerobic session with middle aged wannabe’s.\n"
                            + "Flatley just hoped it didn’t get worse. \n\n\n"
                            + "'It got worse,' thought Flatley.\n\n\n"
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
        // If space is pressed go to level four
        if (input.isKeyPressed(Input.KEY_SPACE)) {
            game.enterState(4);
        }
    }

    @Override // Returns the state ID
    public int getID() {
        return 105;
    }

}
