/* ***********************************
 * CSCI205 - Software Engineering and Design
 * Spring 2017AD
 *
 * Names: CJ Blasi, Christina Caruso, Katherine Lordi, Leo Orozco
 * Date: Apr 12, 2017
 * Time: 9:59:09 AM
 * Project csci205_The_Slackers
 * Package: mainPackage
 * File: LevelOne
 * Descripion: Introduction to the game.
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
import org.newdawn.slick.Sound;
import org.newdawn.slick.state.BasicGameState;
import org.newdawn.slick.state.StateBasedGame;

/**
 * Class that encapsulates the very first level of the game.
 *
 * @author CJ Blasi, Leonard Orozco, Katherine Lordi, Christina Caruso
 */
public class LevelOne extends BasicGameState {

    // Define scrolling
    public float tx;
    public float ty;

    // Contains the character image
    public Image charImage;
    public Image charImage2;
    public Image barrierImage;

    // Contains the portal's image
    public Image portalImage;
    public Image barrierSide;
    public Image barrierCorner;
    public Image barrierVert;
    public Image portalImg;

    // Contains the main player
    public Character player;
    public Character player2;
    public static ArrayList<Character> players;

    // Encoder for the active player
    public int activePlayer;

    // Contains the background object
    public Background background;

    // Make a narrators array
    public ArrayList<NarratorBlock> narrators;
    // Make the image and sound arrays for the narrators
    public ArrayList<Image> narratorImages;
    public ArrayList<Sound> narratorSounds;
    public Image narImgOne;
    public Sound narSndOne;
    public Image narImgTwo;
    public Sound narSndTwo;
    public Image narImgThree;
    public Sound narSndThree;

    // Contains the potential obstacles the player could encounter
    private ArrayList<Sprite> obstacles;

    // Contains the music for the level
    public Music music;

    // Tile width of the associated background
    public final float tileWidth = 40;

    // Room this level will read
    private final int[][] room = new int[][]{{-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, 8, 2, -1, 8, 1, 2, -1, 8, 1, 2, -1, 8, 1, 2, -1, 8, 1, 2, -1, 8, 1, 2, 5, 8, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, 7, 17, 1, 17, 17, 17, 1, 17, 17, 17, 1, 17, 17, 17, 1, 17, 17, 17, 1, 17, 17, 17, -1, 17, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, 7, -1, 5, 5, 5, 17, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 17, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, 7, 3, -1, -1, -1, 9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 6, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, 7, 3, -1, -1, -1, 13, -1, -1, 23, -1, -1, 16, -1, 21, 22, -1, -1, -1, -1, -1, -1, 16, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, 7, 3, -1, -1, -1, -1, -1, -1, 15, 21, -1, 11, -1, 15, 15, -1, 15, 15, -1, 22, 22, 11, 23, -1, -1, -1, -1, -1, 21, 16, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, 7, 3, -1, -1, -1, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, 7, 17, 2, -1, -1, 6, 5, 5, 5, 5, 5, 5, 5, 5, 17, 5, 5, 5, 5, 5, 5, 5, 5, 17, 17, 17, 17, 17, 5, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, 7, 17, 5, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 9, 22, -1, -1, -1, -1, -1, -1, -1, 7, 17, 17, 5, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, 7, 3, -1, 6, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, 6, 12, -1, -1, -1, -1, -1, -1, -1, 7, 17, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, 7, 3, -1, -1, 6, 2, -1, -1, -1, 8, 2, 21, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 23, 7, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, 7, 3, -1, -1, -1, 6, 2, -1, -1, 6, 4, 8, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, 8, 17, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, 7, 3, -1, -1, -1, -1, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 12, -1, -1, 8, 5, 17, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, 7, 3, -1, -1, -1, -1, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, -1, -1, 8, 4, -1, 7, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, 7, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 8, 4, -1, -1, 7, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, 7, 3, -1, 8, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 8, 4, -1, -1, -1, 7, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, 7, 3, -1, 7, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 8, 4, -1, -1, -1, -1, 7, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, 7, 3, -1, 7, 3, 20, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 14, 4, -1, -1, -1, -1, -1, 7, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, 7, 3, -1, 6, 5, 12, -1, 19, -1, 18, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 7, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, 7, 17, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, -1, -1, -1, 7, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, 7, 17, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, -1, -1, 8, 17, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, 7, 3, -1, -1, -1, -1, -1, -1, -1, 6, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 8, 5, 17, 3, -1, 8, 2, -1, 8, 2, -1, 8, 2, -1, 8, 2, -1, -1},
                                             {-1, 7, 3, -1, -1, -1, -1, -1, -1, 6, 4, 6, 4, -1, -1, -1, -1, -1, -1, -1, -1, 8, 4, -1, 7, 17, 1, 17, 17, 1, 17, 17, 1, 17, 17, 1, 17, 3, -1, -1},
                                             {-1, 7, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 8, 4, -1, -1, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, -1, -1},
                                             {-1, 6, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 14, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1},
                                             {-1, -1, -1, 18, -1, -1, 11, -1, 14, 15, 15, 15, 15, 12, -1, 11, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 18, -1, -1, -1, -1, -1, -1, -1, 0, 16},
                                             {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
                                             {5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5}};

// List the contains all of the level rendering
    ArrayList<Integer> levelData = new ArrayList<>(
            Arrays.asList());

    /**
     * Create a LevelOne object.
     *
     * @param state State given from the Game class.
     * @throws SlickException
     */
    public LevelOne(int state) throws SlickException {

    }

// Slick2D init method that allows for continued looping for the game.
    @Override
    public void init(GameContainer gc, StateBasedGame sbg) throws SlickException {

        // Initializes the scrolling variables (where the game viewport starts) to 0,0
        this.tx = 0;
        this.ty = 0;

        // Set up the background with an image from the resources
        // Notice the coordinates are starting at 0.0
        // background hardcoded to width 1600 by height 1200.
        background = new Background(new Image(
                "resources/bg_Lvl_1.png"),
                                    0, 0, 1600, 1200, room);

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

        // Set up the narrators
        setUpNarrator();

        // Initialize the music and start looping the music at 10f volume
        music = new Music("resources/lvlOneMusic.ogg");
        music.setVolume(10f);
        music.loop();

        // Initialize the player and obstacle arrays
        players = new ArrayList<>();
        obstacles = new ArrayList<>();

        // Initialize both players and add them to the array of players
        player = new Character(charImage, 50, 1120, charImage.getWidth(),
                               charImage.getHeight(), 0.12);

        // Add the player to the level.
        players.add(player);

    }

    /**
     * Create the narrators associated with this particular room. This cycles
     * through the room associated with the level to find the appropriate
     * coordinates for each narrator. Each narrator is then its appropriate text
     * string and sound file.
     *
     * @throws SlickException
     * @author Leonard Orozco
     */
    public void setUpNarrator() throws SlickException {
        // Initialize the narrators list
        narrators = new ArrayList<>();
        // TODO - Declare the narration sound associated with each narrator
        narSndOne = new Sound("resources/Lord.ogg");
        narSndTwo = new Sound("resources/Anticipation.ogg");
        narSndThree = new Sound("resources/Checkpoint.ogg");
        // Count the narrator appropriately
        int narCount = 0;
        // For loop for each row in the room
        for (int row = 0; row < room.length; row++) {
            // For loop for each tile in the room
            for (int tile = 0; tile < room[row].length; tile++) {
                // Create these coordinates based on the Background coordinate.
                float xpos = background.x + tile * this.tileWidth;
                float ypos = background.y + row * this.tileWidth;
                // 18 Encodes the the narrator image
                if (room[row][tile] == 18) {
                    // Set up the narrators in this room according to the appropriate counts
                    switch (narCount) {
                        case 1:
                            // Declare the narrator, and its position
                            NarratorBlock newNarrator = new NarratorBlock(xpos,
                                                                          ypos);
                            //Give narrator its stuff
                            newNarrator.stringMessage = "Flatley took in the surroundings with weary anticipation and excitement. 'Adventure is my life's calling,\n"
                                                        + "and I can smell it in the air,' thought Flatley.\n"
                                                        + "Flatley however, would come to realize that that smell was actually just the developer's bad code.";
                            newNarrator.setAudioMessage(narSndTwo);
                            narrators.add(newNarrator);
                            break;
                        case 0:
                            // Declare the narrator, and its position
                            NarratorBlock newNarratorOne = new NarratorBlock(
                                    xpos,
                                    ypos);
                            //Give narrator its stuff
                            newNarratorOne.stringMessage = "Like another King of repute, Lord Monochromatic swore like a sailor,\n"
                                                           + "and wore a constant scowl he bestowed upon all the other\n"
                                                           + "plebeian polygons of flatland.";
                            newNarratorOne.setAudioMessage(narSndOne);
                            narrators.add(newNarratorOne);
                            break;
                        case 2:
                            // Declare the narrator, and its position
                            NarratorBlock newNarratorThree = new NarratorBlock(
                                    xpos,
                                    ypos);
                            //Give narrator its stuff
                            newNarratorThree.stringMessage = "Flatley had reached the first of\n"
                                                             + "many meaningful checkpoints.";
                            newNarratorThree.setAudioMessage(narSndThree);
                            narrators.add(newNarratorThree);
                            break;
                    }
                    // Update the narrator count
                    narCount += 1;
                }
            }
        }
    }

    @Override // Slick2D method that renders objects
    public void render(GameContainer gc, StateBasedGame sbg, Graphics grphcs) throws SlickException {
        // Moves the viewport so that the player stays in view
        grphcs.translate(-tx, -ty);

        // Draw the background
        background.render(gc, sbg, grphcs);

        // Render the narrators
        for (NarratorBlock narrator : narrators) {
            narrator.render(gc, sbg, grphcs);
        }
        // Render the players
        for (Character c : players) {
            c.render(gc, sbg, grphcs);
        }
    }

    @Override // Slick2D update method.
    public void update(GameContainer gc, StateBasedGame sbg, int i) throws SlickException {
        // Check the input passed in
        Input input = gc.getInput();

        // Add the narrators to the objects the player will interact with
        for (NarratorBlock theNarrator : narrators) {
            background.roomObjects.add(theNarrator);
        }

        // Update the players interactions with the background
        players.get(activePlayer).update(gc, sbg, i,
                                         background.roomObjects);

        // Change level if the player is touching a portal
        if (players.get(activePlayer).isTouchingPortal) {
            changeLevel(players, sbg);
        }

        // Call the conditions for scrolling
        sideScrolling(players.get(activePlayer));

        // Call the shadow by pressing Q.
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
        if (player.x + player.width >= (2 * Game.WIDTH / 3) + this.tx) { // Player is scrolling right
            if (this.tx + 3 <= (background.height - Game.HEIGHT)) {
                this.tx += 3;
            }
        }
        if (player.y <= (Game.HEIGHT / 3) + this.ty) { // Player is scrolling to the top
            if (this.ty - 3 >= 0) {
                this.ty -= 3;
            }
        }
        if (player.y + player.height >= (2 * Game.HEIGHT / 3) + this.ty) { // Player is scrolling to the bottom
            if (this.ty + 3 <= (background.height - Game.HEIGHT)) {
                this.ty += 3;
            }
        }
        if (player.x <= (Game.WIDTH / 3) + this.tx) { // Player is scrolling to the left
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
     * @author CJ Blasi
     */
    private void changeLevel(ArrayList<Character> players, StateBasedGame sbg) {
        // Reset the player's position
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
        // Enter level two
        sbg.enterState(103);
    }

    // Get the state ID for this level.
    @Override
    public int getID() {
        return 1;
    }
}
