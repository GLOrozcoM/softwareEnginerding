/* ***********************************
 * CSCI205 - Software Engineering and Design
 * Spring 2017AD
 *
 * Names: CJ Blasi, Christina Caruso, Katherine Lordi, Leo Orozco
 * Date: Apr 24, 2017
 * Time: 10:06:23 AM
 * Project csci205_The_Slackers
 * Package: mainPackage
 * File: LevelTwo
 * Descripion:
 * ***********************************
 */
package mainPackage;

import java.util.ArrayList;
import java.util.Arrays;
import org.newdawn.slick.GameContainer;
import org.newdawn.slick.Graphics;
import org.newdawn.slick.Image;
import org.newdawn.slick.Input;
import org.newdawn.slick.Music;
import org.newdawn.slick.SlickException;
import org.newdawn.slick.state.BasicGameState;
import org.newdawn.slick.state.StateBasedGame;

/**
 * Class that encapsulates behavior for level three
 *
 * @author CJ Blasi, Leonard Orozco, Katherine Lordi
 */
public class LevelFive extends BasicGameState {

    // Define scrolling
    public float tx;
    public float ty;

    // Contains the character image
    public Image charImage;
    public Image charImage2;

    // Contains the barrier image
    public Image barrierImage;
    public Image portalImage;
    public Character player;
    public Character player2;
    public static ArrayList<Character> players;
    public int activePlayer;

    // Contains the background object
    public Background background;
    public Image barrierSide;
    public Image barrierCorner;
    public Image barrierVert;
    public Image portalImg;

    public final float tileWidth = 40;

// Contains the potential obstacles the player could encounter
    private ArrayList<Sprite> obstacles;

// Contains the music for the level
    Music music;

    private final int[][] room = new int[][]{{-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 23, -1, -1, -1},
                                             {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 24, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, -1, -1, -1, 30, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, -1, -1, -1, -1, -1, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 24, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, -1, -1, -1, -1, 2, -1, -1, -1, -1, -1, -1, -1, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, -1, -1, -1, 6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, 2, -1, -1, -1, -1, -1, -1, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, -1, -1, -1, -1, -1, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, -1, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, -1, -1, -1, 6, -1, -1, -1, -1, -1, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, -1, -1, 2, -1, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, 8, -1, -1, -1, 6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, -1, -1, -1, -1, -1, -1, -1, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1},
                                             {-1, -1, -1, -1, -1, -1, -1, -1, -1, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5, 1, -1, -1},
                                             {-1, -1, -1, 25, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 5, 1, -1},
                                             {-1, -1, -1, 26, -1, 1, 1, 5, 5, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 5, -1, -1, -1, -1, 1, -1, 5, -1, -1, 5, -1},
                                             {1, 1, 1, 1, 1, 5, 5, -1, -1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, -1, 1, 1, 1, 1, 5, 1, -1, -1, -1, -1, 1},
                                             {5, 5, 5, 5, 5, -1, -1, -1, -1, 5, 5, 5, 5, -1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, -1, 5, 5, -1, 5, 5, 5, 5, -1, 5, -1, -1, -1, -1, 5}};

    // List the contains all of the level rendering
    ArrayList<Integer> levelData = new ArrayList<>(
            Arrays.asList());

    /**
     * Create a LevelOne object.
     *
     * @param state State given from the Game class.
     * @throws SlickException
     */
    public LevelFive(int state) throws SlickException {

    }
// Slick2D init method that allows for continued looping for the game.

    @Override
    public void init(GameContainer gc, StateBasedGame sbg) throws SlickException {

        // Initializes the scrolling variables (where the game viewport starts) to 0,0
        this.tx = 0;
        this.ty = 0;

        // Set up the background with an image from the resources
        // Notice the coordinates are starting at 0.0
        // background hardcoded to width 1600 by height 1200. I
        background = new Background(new Image(
                "resources/bg_Lvl_5.png"),
                                    0, 0, 1600, 1200, room);

        // Initialize the music
        music = new Music("resources/lvlOneMusic.ogg");
        //music.play();

        players = LevelFour.players;
        player = players.get(0);
        // Create an empty list to hold all the obstacles
        obstacles = new ArrayList<>();

        // Declare all images for this level
        charImage = new Image("resources/character.png");
        charImage2 = new Image("resources/Advisor_Maxel.png");
        barrierImage = new Image("resources/barrier.png");
        barrierSide = new Image("resources/BarrierSide.png");
        barrierCorner = new Image("resources/BarrierCorner.png");
        barrierVert = new Image("resources/BarrierVert.png");
        portalImg = new Image("resources/portal.png");
        charImage2 = new Image("resources/Shadow.png");
        portalImage = new Image("resources/portal.png");
        barrierVert = new Image("resources/BarrierVert.png");

    }

    /**
     * Create the narrators associated with this particular room. This cycles
     * through the room associated with the level to find the appropriate
     * coordinates for each narrator.
     *
     * @throws SlickException
     * @author Leonard Orozco
     */
    public void setUpNarrator() throws SlickException {
        // Unused for this level
    }

    @Override // Slick2D method that renders objects
    public void render(GameContainer gc, StateBasedGame sbg, Graphics grphcs) throws SlickException {
        // Moves the viewport so that the player stays in view
        grphcs.translate(-tx, -ty);
        // Draw the background

        background.render(gc, sbg, grphcs);
        for (Character c : players) {
            c.render(gc, sbg, grphcs);
        }
    }

    @Override // Slick2D update method.
    public void update(GameContainer gc, StateBasedGame sbg, int i) throws SlickException {
        // Check the input passed in
        Input input = gc.getInput();

        players.get(activePlayer).update(gc, sbg, i,
                                         background.roomObjects);

        // Change level if the player is touching a portal
        if (players.get(activePlayer).isTouchingPortal) {
            changeLevel(players, sbg);
        }

        // Call the conditions for scrolling
        sideScrolling(players.get(activePlayer));

        // CODE USED FOR TESTING
        if (input.isKeyPressed(Input.KEY_SPACE)) {

        }
        if (input.isKeyPressed(Input.KEY_Q)) {
            if (players.size() <= 1) {
                player2 = new Character(charImage2, player.x, player.y,
                                        charImage2.getWidth(),
                                        charImage2.getHeight(), 0.12);
                players.add(player2);
            }
            else if (players.size() > 1) {
                players.set(0, players.get(activePlayer));
                player = players.get(0);
                activePlayer = 0;
                players.remove(1);
                player2 = null;

            }
        }
        // Switch between characters
        if (input.isKeyPressed(Input.KEY_LSHIFT) || input.isKeyPressed(
                Input.KEY_RSHIFT)) {
            if (players.size() > 1) {
                switch (this.activePlayer) {
                    case 0:
                        players.get(0).setCharImage(charImage2);
                        players.get(1).setCharImage(charImage);
                        this.activePlayer = 1;
                        break;
                    case 1:
                        players.get(1).setCharImage(charImage2);
                        players.get(0).setCharImage(charImage);
                        this.activePlayer = 0;
                        break;
                    default:
                        System.out.println("Unexpected Error Encountered");
                        break;
                }
            }
        }
    }

    /**
     * Method that checks for all the conditions to allow for side scrolling.
     * This includes scrolling in the +-x and +-y directions.
     *
     * In general, the players x and y will change inversely with respect to the
     * direction the players wishes to move in. Also note that after making
     * contact with 2/3 of the window view, an additional condition based on
     * basic geometry is necessary.
     *
     * @author Leonard Orozco, Katherine Lordi
     */
    public void sideScrolling(Character player) {
        // The player wishes to scroll to the right
        if (player.x + player.width >= (2 * Game.WIDTH / 3) + this.tx) {
            if (this.tx + 3 <= (background.height - Game.HEIGHT)) {
                this.tx += 3;
            }
        }
        // The player wishes to scroll to the top
        if (player.y <= (Game.HEIGHT / 3) + this.ty) {
            if (this.ty - 3 >= 0) {
                this.ty -= 3;
            }
        }
        // The player wishes to scroll to the bottom
        if (player.y + player.height >= (2 * Game.HEIGHT / 3) + this.ty) {
            if (this.ty + 3 <= (background.height - Game.HEIGHT)) {
                this.ty += 3;
            }
        }
        // The player wishes to scroll to the left
        if (player.x <= (Game.WIDTH / 3) + this.tx) {
            if (this.tx - 3 >= 0) {
                this.tx -= 3;
            }
        }
    }

    /**
     * Resets the players and changes the level to the next one. This method
     * gets called whenever a player comes in contact with a portal. It resets
     * both players i the game back to their starting point ad the changes the
     * state of the game.
     *
     * @param players
     * @param sbg
     */
    private void changeLevel(ArrayList<Character> players, StateBasedGame sbg) {
        this.activePlayer = 0;
        players.get(0).setX(50);
        players.get(0).setY(1100);
        if (players.size() > 1) {
            players.remove(1);
        }
        for (Character c : players) {
            c.isTouchingPortal = false;
        }
        players.get(0).setCharImage(charImage);
        sbg.enterState(107);
    }

    @Override
    public int getID() {
        return 5;
    }
}
