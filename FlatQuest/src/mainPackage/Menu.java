/* ***********************************
 * CSCI205 - Software Engineering and Design - Spring 2017AD
 *
 * Names: CJ Blasi, Christina Caruso, Katherine Lordi, Leo Orozco
 * Date: Apr 11, 2017
 * Time: 5:32:49 PM
 * Project csci205_The_Slackers
 * Package: mainPackage
 * File: Menu
 * Descripion:
 * ***********************************
 */
package mainPackage;

import org.newdawn.slick.GameContainer;
import org.newdawn.slick.Graphics;
import org.newdawn.slick.Image;
import org.newdawn.slick.Input;
import org.newdawn.slick.SlickException;
import org.newdawn.slick.state.BasicGameState;
import org.newdawn.slick.state.StateBasedGame;

/**
 * Sets up the Menu State. Currently contains only overridden methods.
 *
 * @author cjb030
 */
public class Menu extends BasicGameState {

    Image TitleBanner;
    String welcomeMessage = "Press Space to Play!";

    // Currently unused constructor
    public Menu(int state) {
    }

    @Override // Mandatory Override
    public void init(GameContainer container, StateBasedGame sbg)
            throws SlickException {
        TitleBanner = new Image("resources/TitleBanner.png");

    }

    @Override
    public void render(GameContainer container, StateBasedGame sbg, Graphics g)
            throws SlickException {
        // Place the welcome message in the center of the window.
        g.drawString(welcomeMessage,
                     (Game.WIDTH / 2 - welcomeMessage.length() * 5),
                     (2 * Game.HEIGHT / 3));
        g.drawString(
                "'WASD' to Move \n'Q' To Summon Shadow \n'Shift' to switch bodies",
                (Game.WIDTH / 2) - 90, (2 * Game.HEIGHT / 3) + 40);

        g.drawImage(TitleBanner, (Game.WIDTH / 2 - (TitleBanner.getWidth() / 2)),
                    (Game.HEIGHT / 2 - TitleBanner.getHeight()));
    }

    @Override
    public void update(GameContainer container, StateBasedGame sbg, int delta)
            throws SlickException {
        Input input = container.getInput();
        if (input.isKeyPressed(Input.KEY_SPACE)) {
            sbg.enterState(101);
        }
    }

    @Override // Return's the state's number (0 for menu).
    public int getID() {
        return 0;
    }
}
