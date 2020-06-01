/* ***********************************
 * CSCI205 - Software Engineering and Design - Spring 2017AD
 *
 * Names: CJ Blasi, Christina Caruso, Katherine Lordi, Leo Orozco
 * Date: Apr 11, 2017
 * Time: 5:00:10 PM
 * Project csci205_The_Slackersawd
 * Package: mainPackage
 * File: Game
 * Descripion: The Big Mac Daddy of Heimlich County. This class
 * places all states and games together in one cohesive whole.
 * ***********************************
 */
package mainPackage;

import org.newdawn.slick.AppGameContainer;
import org.newdawn.slick.GameContainer;
import org.newdawn.slick.SlickException;
import org.newdawn.slick.state.StateBasedGame;

/**
 * Class that brings all the game together and manages the current state of the
 * game
 *
 * @author CJ Blasi, Leonard Orozco
 */
public class Game extends StateBasedGame {

    // The Main Game container
    public static AppGameContainer TheGame;

    // Declare all states and their respective ID's
    public static final int MENU = 0;
    public static final int LEVEL_1 = 1;
    public static final int LEVEL_2 = 2;
    public static final int LEVEL_3 = 3;
    public static final int LEVEL_4 = 4;
    public static final int LEVEL_5 = 5;
    public static final int PAUSEMENU = 10;
    public static final int PRE_MENU = 101;
    public static final int PRE_LEVEL_ONE = 102;
    public static final int PRE_LEVEL_TWO = 103;
    public static final int PRE_LEVEL_THREE = 104;
    public static final int PRE_LEVEL_FOUR = 105;
    public static final int PRE_LEVEL_FIVE = 106;
    public static final int EPILOGUE = 107;

    // Sets the game's viewing dimensions
    public static int WIDTH = 1200;
    public static int HEIGHT = 800;

    /**
     * Constructor for the game class. Sets up all the states.
     *
     * @param name Name identifier for the game instance. Is always "Game"
     * @throws org.newdawn.slick.SlickException
     * @author CJ Blasi, Leonard Orozco
     */
    public Game(String name) throws SlickException {
        super(name);
        // Add all states the game may work with.
        this.addState(new PreMenu(PRE_MENU));
        this.addState(new Menu(MENU));
        this.addState(new PauseMenu(PAUSEMENU));
        this.addState(new PreLevelOne(PRE_LEVEL_ONE));
        this.addState(new LevelOne(LEVEL_1));
        this.addState(new PreLevelTwo(PRE_LEVEL_TWO));
        this.addState(new LevelTwo(LEVEL_2));
        this.addState(new PreLevelThree(PRE_LEVEL_THREE));
        this.addState(new LevelThree(LEVEL_3));
        this.addState(new PreLevelFour(PRE_LEVEL_FOUR));
        this.addState(new LevelFour(LEVEL_4));
        this.addState(new PreLevelFive(PRE_LEVEL_FIVE));
        this.addState(new LevelFive(LEVEL_5));
        this.addState(new Epilogue(EPILOGUE));
    }

    /**
     * Initializes the different states of the game.
     *
     * @param container The Game Container object
     * @throws SlickException
     * @author CJ Blasi, Leonard Orozco
     */
    @Override
    public void initStatesList(GameContainer container) throws SlickException {

        // Acquire all the states the game will work with.
        this.getState(PRE_MENU).init(container, this);
        this.getState(MENU).init(container, this);
        this.getState(PAUSEMENU).init(container, this);
        this.getState(PRE_LEVEL_ONE).init(container, this);
        this.getState(LEVEL_1).init(container, this);
        this.getState(PRE_LEVEL_TWO).init(container, this);
        this.getState(LEVEL_2).init(container, this);
        this.getState(PRE_LEVEL_THREE).init(container, this);
        this.getState(LEVEL_3).init(container, this);
        this.getState(PRE_LEVEL_FOUR).init(container, this);
        this.getState(LEVEL_4).init(container, this);
        this.getState(PRE_LEVEL_FIVE).init(container, this);
        this.getState(LEVEL_5).init(container, this);
        // Access level five here
        this.getState(EPILOGUE).init(container, this);
        // This is where the game begins
        this.enterState(MENU);
    }

    /**
     * Main method that calls the game into being.
     *
     * @param args
     * @throws SlickException
     * @author CJ Blasi, Leonard Orozco
     */
    public static void main(String[] args) throws SlickException {
        // Initialize a new game.
        TheGame = new AppGameContainer(new Game("Game"), Game.WIDTH,
                                       Game.HEIGHT, false);

        // Set frame rate and do not display it.
        TheGame.setTargetFrameRate(120);
        TheGame.setShowFPS(false);

        // Get the party underway
        TheGame.start();

    }
}
