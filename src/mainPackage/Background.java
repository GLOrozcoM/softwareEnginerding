/* ***********************************
 * CSCI205 - Software Engineering and Design - Spring 2017AD
 *
 * Names: CJ Blasi, Christina Caruso, Katherine Lordi, Leo Orozco
 * Date: Apr 11, 2017
 * Time: 5:00:10 PM
 * Project csci205_The_Slackers
 * Package: mainPackage
 * File: Background
 * Descripion: A class that encapsulates a background object. The background
 * interacts heavily with the level classes. Take care to understand how each level
 * class interacts with the background.
 * ***********************************
 */
package mainPackage;

import java.util.ArrayList;
import java.util.Random;
import org.newdawn.slick.GameContainer;
import org.newdawn.slick.Graphics;
import org.newdawn.slick.Image;
import org.newdawn.slick.SlickException;
import org.newdawn.slick.Sound;
import org.newdawn.slick.SpriteSheet;
import org.newdawn.slick.state.StateBasedGame;

/**
 * Class that creates a background for the player to move around in.
 *
 * @author Leonard Orozco & CJ Blasi
 */
public class Background {

    // Cordinates in the plane
    public float x;
    public float y;
    public ArrayList<Character> players;
    public int activePlayer;

    // Give the height and width
    public float width;
    public float height;

    // Image associated with this object
    public Image backgroundImg;

    // Array list that will hold the necessary numbers
    // that encode an object and its rendering
    public int[][] roomObjectsEncoded;
    public Image barrierSide;
    public Image barrierCorner;
    public Image barrierVert;
    public Image barrierThin;
    public Image barrierthinSide;
    public Image barrierEdge;
    public Image barrierEdgeRight;
    public Image barrierX;
    public Image barrierBlack;
    public Image portalImg;
    public Sound narratorSound;
    public Image charImage2;
    public Image charImage;
    public Image mushroomImg;
    public Image fFlower;
    public Image sleepCitizen;
    public Image sleepCitizenL;
    public Image AnomalyImg;
    public Image citizenWorriedImg;
    // ArrayList that will hold the actual objects
    public ArrayList<Sprite> roomObjects = new ArrayList<>();
    public ArrayList<NarratorBlock> narrators = new ArrayList<>();
    // Each "tile" or populator of the room
    // should have a width associated with it.
    public int tileWidth = 40;

    private final SpriteSheet lmSheet;
    private final SpriteSheet amSheet;

    /**
     * Construct a background object for a room. Particular care must be taken
     * when assigning an image and dimensions. Make sure the image passed in as
     * the background has the same dimensions as the width and height passed in.
     *
     * @param img Image associated with the object.
     * @param x X coordinate
     * @param y Y coordinate
     * @param width
     * @param height
     * @author Leonard Orozco & CJ Blasi
     * @param room
     * @throws org.newdawn.slick.SlickException
     */
    public Background(Image img, float x, float y, float width, float height,
                      int[][] room) throws SlickException {
        this.barrierCorner = new Image("resources/BarrierCorner.png");
        this.barrierVert = new Image("resources/BarrierVert.png");
        this.portalImg = new Image("resources/portal.png");
        this.charImage = new Image("resources/character.png");
        this.charImage2 = new Image("resources/Lord_Monochromatic.png");
        this.barrierSide = new Image("resources/BarrierSide.png");
        this.barrierThin = new Image("resources/thinBarrier.png");
        this.barrierthinSide = new Image("resources/thinBarrierSide.png");
        this.barrierEdge = new Image("resources/BarrierEdge.png");
        this.barrierEdgeRight = new Image("resources/BarrierEdgeRight.png");
        this.barrierX = new Image("resources/x-block.png");
        this.barrierBlack = new Image("resources/BarrierBlack.png");
        this.mushroomImg = new Image("resources/Mushroom.png");
        this.sleepCitizen = new Image("resources/SleepingCitizen.png");
        this.sleepCitizenL = new Image("resources/SleepingCitizenL.png");
        this.lmSheet = new SpriteSheet(
                "resources/Lord_MonochromaticGif.png", 20,
                20);
        this.amSheet = new SpriteSheet("resources/Advisor_Maxel.png", 20,
                                       30);
        this.fFlower = mushroomImg.getFlippedCopy(false, false);
        this.AnomalyImg = new Image("resources/Anomaly.png");
        this.citizenWorriedImg = new Image("resources/CitizenWorried.png");

        // Pass in the required coordinates
        this.x = x;
        this.y = y;
        // Set up the image
        this.backgroundImg = img;
        // Set the height and width of the entire background
        this.width = width;
        this.height = height;
        // Initialize the encoding array for each type of room component
        roomObjectsEncoded = room;
    }

    /**
     * Method built off of Slick 2D's rendering method. See the Slick 2D API for
     * details with the parameters.
     *
     * This method ensures that the background and its associated objects are
     * rendered correctly.
     *
     * @param gc
     * @param sbg
     * @param g
     * @throws SlickException
     */
    public void render(GameContainer gc, StateBasedGame sbg, Graphics g) throws SlickException {
        // Make sure the objects were actualy created.
        createRoomObjects();
        // Notice this is draw image instead of a shape
        g.drawImage(backgroundImg, x, y);
        // Render each object.
        for (Sprite s : roomObjects) {
            s.render(gc, sbg, g);
        }
    }

    /**
     * Method that declares the room objects to the level. Simply recreate the
     * room every time the background coordinates are changed!
     *
     * @author CJ Blasi & Leonard Orozco
     */
    public void createRoomObjects() throws SlickException {
        // Recreate the objects in the room from scratch
        roomObjects.clear();
        narrators.clear();
        Random rand = new Random();

        // For loop for the first row
        for (int row = 0; row < roomObjectsEncoded.length; row++) {
            // For loop for each tile in the room
            for (int tile = 0; tile < roomObjectsEncoded[row].length; tile++) {
                // TODO - Set up the possible room objects above as
                // final constants, then when comparing, we will only
                // call their names.
                // Create these coordinates based on the Background coordinate.
                float xpos = this.x + tile * this.tileWidth;
                float ypos = this.y + row * this.tileWidth;

                // Floats for generating random color 'distortion' flashes
                float r = rand.nextFloat() * 0.99f; // Random red value
                float g = rand.nextFloat() * 0.99f; // Random green value
                float b = rand.nextFloat() * 0.99f; // Random blue value

                switch (roomObjectsEncoded[row][tile]) {
                    case 0: // Creates a Portal Block
                        Portal port = new Portal(portalImg, xpos, ypos);
                        roomObjects.add(port);
                        break;
                    case 1: // Create barrier w/top side image
                        Barrier topBar = new Barrier(barrierSide, xpos, ypos);
                        roomObjects.add(topBar); // Add object to obstacles list.
                        break;
                    case 2: // Create barrier w/top corner side image
                        Barrier topCornerBar = new Barrier(barrierCorner, xpos,
                                                           ypos);
                        roomObjects.add(topCornerBar); // Add object to obstacles list.
                        break;
                    case 3:  // Create barrier w/right side image
                        Barrier rightBar = new Barrier(barrierVert, xpos, ypos);
                        roomObjects.add(rightBar); // Add object to obstacles list.
                        break;
                    case 4:  // Create barrier w/bottom right corner side image
                        Barrier bottomRightCorner = new Barrier(
                                barrierCorner.getFlippedCopy(false, true), xpos,
                                ypos);
                        roomObjects.add(bottomRightCorner); // Add object to obstacles list.
                        break;
                    case 5: // Create barrier w/bottom side image
                        Barrier bottomBar = new Barrier(
                                barrierSide.getFlippedCopy(false, true), xpos,
                                ypos);
                        roomObjects.add(bottomBar); // Add object to obstacles list.
                        break;
                    case 6:  // Create barrier w/bottom left corner side image
                        Barrier bottomLeftCorner = new Barrier(
                                barrierCorner.getFlippedCopy(true, true), xpos,
                                ypos);
                        roomObjects.add(bottomLeftCorner); // Add object to obstacles list.
                        break;
                    case 7: // Create barrier w/left side image
                        Barrier leftBar = new Barrier(
                                barrierVert.getFlippedCopy(true, false), xpos,
                                ypos);
                        roomObjects.add(leftBar); // Add object to obstacles list.
                        break;
                    case 8:  // Create barrier w/top corner side image
                        Barrier topLeftCorner = new Barrier(
                                barrierCorner.getFlippedCopy(true, false), xpos,
                                ypos);
                        roomObjects.add(topLeftCorner); // Add object to obstacles list.
                        break;
                    case 9:
                        Barrier thinBar = new Barrier(barrierThin, xpos, ypos);
                        roomObjects.add(thinBar);
                        break;
                    case 10:
                        Barrier thinSideBar = new Barrier(barrierthinSide, xpos,
                                                          ypos);
                        roomObjects.add(thinSideBar);
                        break;
                    case 11:
                        Barrier edgeBar = new Barrier(barrierEdge, xpos, ypos);
                        roomObjects.add(edgeBar);
                        break;
                    case 12:
                        Barrier edgeRBar = new Barrier(barrierEdgeRight, xpos,
                                                       ypos);
                        roomObjects.add(edgeRBar);
                        break;
                    case 13:
                        Barrier edgeBBar = new Barrier(
                                barrierEdge.getFlippedCopy(false, true), xpos,
                                ypos);
                        roomObjects.add(edgeBBar);
                        break;
                    case 14:
                        Barrier edgeLBar = new Barrier(
                                barrierEdgeRight.getFlippedCopy(true, false),
                                xpos,
                                ypos);
                        roomObjects.add(edgeLBar);
                        break;
                    case 15:
                        Barrier xBar = new Barrier(barrierX, xpos, ypos);
                        roomObjects.add(xBar);
                        break;
                    case 16:
                        Barrier mushBar = new Barrier(mushroomImg, xpos,
                                                      ypos + (tileWidth - mushroomImg.getHeight()));
                        roomObjects.add(mushBar);
                        break;
                    case 17:
                        Barrier blackBar = new Barrier(barrierBlack, xpos, ypos);
                        roomObjects.add(blackBar);
                        break;
                    case 18:
                        // This is the narrator check.
                        break;
                    case 19: // Creates the NPC Advisor Maxel
                        NPC advisorM = new NPC(amSheet, xpos,
                                               ypos + (tileWidth - 30), 20, 20);
                        roomObjects.add(advisorM);
                        break;
                    case 20: //Creates NPC Lord Monochromatic
                        NPC lordM = new NPC(lmSheet, xpos + 10,
                                            ypos + (tileWidth - 20), 20, 20);
                        roomObjects.add(lordM);
                        break;
                    case 21:
                        //sleepCitizen.setImageColor(0.1f, 0.1f, 0.9f);
                        Barrier sCitizen = new Barrier(sleepCitizen, xpos,
                                                       ypos + (tileWidth - sleepCitizen.getHeight()));
                        roomObjects.add(sCitizen);
                        break;
                    case 22:
                        Barrier sCitizenWest = new Barrier(
                                sleepCitizen.getFlippedCopy(true, false), xpos,
                                ypos + (tileWidth - sleepCitizen.getHeight()));
                        roomObjects.add(sCitizenWest);
                        break;
                    case 23:
                        Barrier sCitizenL = new Barrier(
                                sleepCitizenL, xpos,
                                ypos + (tileWidth - sleepCitizenL.getHeight()));
                        roomObjects.add(sCitizenL);
                        break;
                    case 24: // Creates the 'glitching' flower barrier

                        fFlower.setImageColor(r, g, b);
                        Barrier flashFlower = new Barrier(fFlower, xpos,
                                                          ypos + (tileWidth - fFlower.getHeight()));
                        roomObjects.add(flashFlower);
                        break;
                    case 25:
                        Image brokenTopBarImg = barrierSide.getFlippedCopy(false,
                                                                           false);
                        brokenTopBarImg.setImageColor(r, g, b);
                        Barrier brokenTopBar = new Barrier(brokenTopBarImg, xpos,
                                                           ypos);
                        brokenTopBar.setPassThrough();
                        roomObjects.add(brokenTopBar);
                        break;

                    case 26:
                        Image brokenBottomBarImg = barrierSide.getFlippedCopy(
                                false,
                                true);
                        brokenBottomBarImg.setImageColor(r, g, b);
                        Barrier brokenBottomBar = new Barrier(brokenBottomBarImg,
                                                              xpos, ypos);
                        brokenBottomBar.setPassThrough();
                        roomObjects.add(brokenBottomBar); // Add object to obstacles list.
                        break;
                    case 27:
                        Barrier CitizenWorried = new Barrier(
                                citizenWorriedImg, xpos,
                                ypos + (tileWidth - citizenWorriedImg.getHeight()));
                        roomObjects.add(CitizenWorried);
                        break;
                    case 30:
                        Portal Anomaly = new Portal(AnomalyImg, xpos, ypos);
                        Anomaly.setWidth(AnomalyImg.getWidth());
                        Anomaly.setHeight(AnomalyImg.getHeight());
                        roomObjects.add(Anomaly);

                }

            }
        }
        for (int i = 0; i < LevelOne.players.size(); i++) {
            roomObjects.add(LevelOne.players.get(i));
        }
    }

    public void update(GameContainer gc, StateBasedGame sbg, int delta) {
        // Slick2D Method
    }

    // Getter for the background image
    public Image getBackgroundImg() {
        return backgroundImg;
    }

// Give this background an ID
    public int getID() {
        return 10;
    }

    // Getter for the list of players
    public ArrayList<Character> getPlayers() {
        return players;
    }
}
