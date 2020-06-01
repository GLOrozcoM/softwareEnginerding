/* ***********************************
 * CSCI205 - Software Engineering and Design
 * Spring 2017AD
 *
 * Names: CJ Blasi, Christina Caruso, Katherine Lordi, Leo Orozco
 * Date: Apr 30, 2017
 * Time: 10:50:19 AM
 * Project csci205_The_Slackers
 * Package: mainPackage
 * File: PostLevelFour
 * Descripion: Flatley's thoughts towards the end of the game
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
 * End of the game transition
 *
 * @author Leonard Orozco
 */
public class Epilogue extends BasicGameState {

    /**
     * Constructor for the transition screen
     *
     * @param state An integer encoding the state of the transition.
     */
    public Epilogue(int state) {
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
                "At the moment of contact the anomaly noticed dear Flatley. A bellowing voice echoed across the plane,\n"
                + "vibrating the land, seas, and Flatley.\n"
                + "'Sup.'\n"
                + "Flatley was unsure of how to respond. Eventually he managed to stammer out a response.\n"
                + "'W-why are you doing this?'\n"
                + "“Doing what?”\n"
                + "'The disturbances everywhere!' Exclaimed Flatley 'Everything is getting messed up!'\n"
                + "'Oh, it isn’t always like this?'\n"
                + "At that moment, Flatley realized this was more of a misunderstanding than an intentional act of malice.\n"
                + "Flatley explained his mission, and how the anomaly’s presence was causing a disturbance in the world.\n"
                + "The anomaly ruminated on this for a moment, before apologizing.\n"
                + "It was quite a scene to see such a vast being apologize to one so small.\n"
                + "After gathering itself up the Anomaly bid Flatley a farewell and promised that if it were to return,\n"
                + "it would try to do so less destructively. And with that, Flatley was alone.\n\n\n"
                + "Press space to begin anew or press 'E' to exit the game",
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
        // If space is pressed go to the pre-menu
        if (input.isKeyPressed(Input.KEY_SPACE)) {
            game.enterState(101);
        }
        else if (input.isKeyPressed(Input.KEY_E)) {
            // If key E is pressed, exit the game
            gameContainer.exit();
        }
    }

    @Override // Returns the state ID
    public int getID() {
        return 107;
    }

}
