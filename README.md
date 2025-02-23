## Game Time

The piano rocks but its time to add more fun to the Piano Rock star, how about creating a game around our event

To get turn the piano into a game we want to 
* Add songs to the game
* Add keyboard support
* Add choose piano note support
* Add score functionality

We should create a cool panel on top of our piano to enable these festures

![alt text](https://raw.github.com/CoderDojo/piano-game/master/game/doc-files/piano-game.png?login=noelking&token=e3573361872dca184dca5ebeb8df868e "Piano Rock Star")


## Create the game section on the page

we will give it css style of __gameDiv__ so add a class attribute to with the __gameDiv__ value.

````html

<div class="gameDiv">			
				
</div>


````

This __div__ should be located immediately inside the __body__ tag

````html

<body>
			<div class="gameDiv">	

			</div>
````

We now need to add the style for our game panel.  So what does our style want to achieve?  We need to 
* Set left padding to zero
* Set right padding to zero
* A border on the bottom to emphasis on piano panel, the color should be  #222222 solid and width of 1px
* Add shadow with following details: 0 1px 3px rgba(0, 0, 0, 0.25), 0 -1px 0 rgba(0, 0, 0, 0.1) inset;
* Min height of 130px
* Width of the panel to 1050px
* Margin for left of auto
* Margin for right of auto

Now add a new style to the bottom of style.css called ````div.gameDiv```` 

````css

div.gameDiv {
    padding-left: 0;
    padding-right: 0;
    border-bottom: 1px solid #222222;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.25), 0 -1px 0 rgba(0, 0, 0, 0.1) inset;
    min-height: 130px;
    width: 1050px;
    margin-left: auto;
    margin-right: auto;
}

````

## Add songs to the game

On the very right of the game section we see the play note section which look like this


![alt text](https://raw.github.com/CoderDojo/piano-game/master/game/doc-files/play-note.png "Piano Rock Star")

We not need to add the HTML and CSS to display this panel so lets get started, what HTML tag should we use?  Yes you are right __div__ tag so lets go and create that div just inside the 
__gameDiv__

__NOTE__ Remember to create the closing div tag as well


````html

<div class="gameDiv">   
                <div>

                </div>
````

Now lets add some styling inside the __class__ attribute.  Can you add three styles
* songOption
* spanAuto
* span230

We create different styles so they can shared in different ares of the website, it is good standard to create small styles classes which can be reused

The class can take multiple styles as long as you seperate them by a space

````html

<div class="gameDiv">

    <div class="gamePanel spanAuto span230">
                    
                </div>      

````

Now lets add the style for this div, with the following aims

#### gamePanel style
* Set the background to #3A3A3A
* Add a border of type solid, width 1px and color #CCCCCC;
* Add a box shadow with color rgba(0, 0, 0, 0.075);
* Add text folor of #333333;
* Display block
* Set the position to relative
* Set the transistion to .02s with each of 0s
* Set padding on the div to 4px
* Add a margin top of 10px

````css

.gamePanel {
    background: #3A3A3A;
    border: 1px solid #CCCCCC;
    box-shadow: 0 1px 1px rgba(0, 0, 0, 0.075);
    color: #333333;
    display: block;
    position: relative;
    transition: transform 0.2s ease 0s;
    padding: 4px;
    height: 100px;
    margin-top: 10px;
}
````

Now refresh your page and is it looking like your div? not yet well we have more styling to do


#### Add hover for the song option

One cool feature that can be added in CSS is __hover__ so when you put the mouse over a section of a screen it can cause the style to change.  To do this 
you use the style __class__ in our case __gamePanel__ and then put __:hover__ after it.  This is now the style that will appear once the mouse is over this 
section.

Lets make the __div__ a little bigger when the mouse appears over the sections of its feels like 3D

````css
.songOption:hover {
    transform: scale(1.04);
 }
````


#### spanAuto style

Now lets style the spanAuto
* Set margin of 10px
* Set the float to left


````css
.spanAuto {
    margin: 10px;
    float: left;
}
````

#### span230 style

There is one important property we have not set yet? Yes its the width
* Set the width to 230px

````css
.span230 {
    width: 230px;
}
````
#### Style inside the song div

Would you agree we are slitting the div in half 
* First half with bullet > and Play note message
* Second hand displaying the note

Well its now time to add the notice div for the message, add a new div with span50p style
* Add new div with class of __span50p__
* Add new span with class __notice__  and text __>__
* Add h3 with text __Play Note__
* Add hr tag
* Close div tag

````html
<div class="gameOption spanAuto span230">
        <div class="span50p">
            <span class="notice">></span>
                <h3>Play Note</h3>
            <hr/>
            </div>

````

Great refresh the page, how does this look? not great right? Well we now need to style it.  First lets handle the __span50p__ style in style.css
* We want the __width__ to be __50%__
* Set the __float__ to __left__ 

````css
.span50p {
    width:50%;
    float: left;
}
````

Great its now time to style the notice, which adds the orange section with __>__ bullet
* Set the __margin__ to __10px__
* Set the __background__ to __#EB3C00__
* Set the __border-radius__ to __50%__ for each corner, so its a circle
* Set the text __color__ to __#FFFFFF__
* Set the __display__ to __inline-block__
* Set the __float__ to __left__
* Set the __font-size__ to __15px__
* Set the __font-weight__ to __bold__
* Set the __height__ to __32px__
* Set the __line-height__ to __30px__
* Set the __margin-right__ to __10px__
* Set the __text-align__ to __center__
* Set the __width__ to __30px__

````css
 span.notice {
    margin-top: 10px;
    background: #EB3C00;
    border-radius: 50% 50% 50% 50%;
    color: #FFFFFF;
    display: inline-block;
    float: left;
    font-size: 15px;
    font-weight: bold;
    height: 32px;
    line-height: 30px;
    margin-right: 10px;
    text-align: center;
    width: 30px;
}
```` 
#### Set the h3 style

We now need to style the __h3__ so go to __style.css__ and using the tag name create a new style that
* Set the __font-family__ to __'Lato',sans-serif__
* Set the text __color__ to __ #AAAAAA__
* Set the __font-size__ to __12px__

````css
h3 {
    font-family: 'Lato',sans-serif;
    color: #AAAAAA;
    font-size: 12px;
}
````

Now refresh and your play note section should be looking alot better

#### Add the section to display the note

Now add a section for displaying the note, by creating a new __div__

````html
<div class="span50p">
                <div id="note" class="info"></div>
            </div>
````

The play note __div__ is now complete and should look exactly like this

````html

      <div class="gameOption spanAuto span230">
        <div class="span50p">
            <span class="notice">></span>
                <h3>Play Note</h3>
            <hr/>
            </div>
            <div class="span50p">
                <div id="note" class="info"></div>
            </div>
        </div>
    </div>
````

We have already see the __span50p__ style, but we need to add the new style for __info__ to style.css

####Style for info
* Set __margin__ of __5px__
* Set the __border__ of __thin solid__ and color __#000__
* Set the __padding-top__ of __15px__
* Set the __height__ of __75px__
* Set the __font-size__ of __50px__
* Set the __text-align__ to __center__

````css
div.info {
    margin: 5px;
    border: thin solid #000;
    padding-top: 15px;
    height: 75px;
    font-size: 50px;
    text-align: center;
}
````

## Add songs to the game

Now lets create and style the song loader, would you agreed the song panel is inside the game div?  Lets see if we can build the play song __div__ to look like this 

![alt text](https://raw.github.com/CoderDojo/piano-game/master/game/doc-files/select-song.png "Piano Rock Star")

This panel should
* Have message tell players to __Select Song__
* Have a drop down we can load songs into 
* A button to play the song

This panel is going to be very similar to the play note one we just created, so lets create add the following HTML

````html
	<div class="gamePanel spanAuto">
        <span class="notice">></span>
        <h3></h3>
        <hr/>
        
     </div>
````

Now inside the __h3__ tags add the text __Select Song__ so we now look like this

````html
    <div class="gamePanel spanAuto">
        <span class="notice">></span>
        <h3></h3>
        <hr/>
        
     </div>
````

Now create a new html __select__ tag, with an __option__ for __Select__, the select song html should now look like this


````html
    <div class="gamePanel spanAuto">
        <span class="notice">></span>
        <h3>Select Song</h3>
        <hr/>
        <select id="songs"><option>Select</option></select>
     </div>
````

Great this looks really good, but dont have a button to start the game, lets add a __button__ with existing style classes
* btn
* btn-red

* Give the button an __id__ of __playSong__

The select song html should now look like this.

````html
    <div class="gamePanel spanAuto">
        <span class="notice">></span>
        <h3>Select Song</h3>
        <hr/>
        <select id="songs"><option>Select</option></select>
        <button id="playSong" class="btn btn-red" type="submit" >Play Now!</button>
     </div>
````


## Add the Score 

We want the score to appear right? like the play note section this is inside the __gameDiv__ , so we need to create a div that looks like this

![alt text](https://raw.github.com/CoderDojo/piano-game/master/game/doc-files/score.png "Piano Rock Star")

This panel should
* Hightlight its the score panel
* Have message tell players the __Score__

Ok its great that this panel is very similar to the previous two see we can use their style and html code.  To get started create add the following html just like we did in previous sections


````html
   <div class="gamePanel spanAuto span230">
    <div class="span50p">
    <span class="notice">></span>
        <h3></h3>
    <hr/>
    </div>
    <div class="span50p">
        <div id="scre" class="info red">0</div>
    </div>
</div>
````

Now inside the __h3__ tags add the text __Score__ so we now look like this

````html
   <div class="gamePanel spanAuto span230">
    <div class="span50p">
    <span class="notice">></span>
        <h3>Score</h3>
    <hr/>
    </div>
    <div class="span50p">
        
    </div>
</div>
````

Now create a new __div__ tag to display the score with two style class of 
* info
* red

````html
   <div class="gamePanel spanAuto span230">
    <div class="span50p">
    <span class="notice">></span>
        <h3>Score</h3>
    <hr/>
    </div>
    <div class="span50p">
        <div id="score" class="info red">0</div>
    </div>
</div>
````

To emhasise this is the score, we are going to set the text color red, so lets open style.css and add a new style for class red
* Set the __color__ to __#CC0000__

````css
.red {
    color: #CC0000;
}
````

## Add the Keyboard helper 

You would a keyboard helper to tell you what key to hit right? so we need to create a div that looks like this inside the __gameDiv__

![alt text](https://raw.github.com/CoderDojo/piano-game/master/game/doc-files/keyboard-help.png "Piano Rock Star")

This panel should
* Hightlight its the keybooard panel
* Have message tell players which key to hit

Ok its great that this panel is very similar to the previous two see we can use their style and html code.  To get started create add the following html just like we did in previous sections


````html
<div class="gamePanel spanAuto span230">
    <div class="span50p">
    <span class="notice">></span>
        <h3></h3>
    <hr/>
    </div>
    <div class="span50p">
    </div>
</div>
````

Now inside the __h3__ tags add the text __Keyboard__ so we now look like this

````html
<div class="gamePanel spanAuto span230">
    <div class="span50p">
    <span class="notice">></span>
        <h3>Keyboard</h3>
    <hr/>
    </div>
    <div class="span50p">
    </div>
</div>
````

Now create a new __div__ tag to display the keyboard key with an __id__ of __keyboard__ and two style class of 
* info
* keyboardInfo

````html
 <div class="gamePanel spanAuto span230">
    <div class="span50p">
    <span class="notice">></span>
        <h3>Keyboard</h3>
    <hr/>
    </div>
    <div class="span50p">
        <div id="keyboard" class="info keyboardInfo"></div>
    </div>
</div>
````

To emhasise this is the score, we are going to set the text color red, so lets open style.css and add a new style for class red
* Set the __background__ to __gray__
* Set the __font-weight__ to __bold__

````css
.keyboardInfo {
    background: gray;    
    font-weight: bold;
}
````

Congratulations you have now created the game panels for Piano Rock Star.  Just to review your HTML should now look like this

````html
<div class="gameDiv">   
    <div class="gamePanel spanAuto span230">
        <div class="span50p">
        <span class="notice">></span>
            <h3>Play Note</h3>
        <hr/>
        </div>
        <div class="span50p">
            <div id="note" class="info"></div>
        </div>
    </div>      
    <div class="gamePanel spanAuto">
        <span class="notice">></span>
        <h3>Select Song</h3>
        <hr/>
        <select id="songs"><option>Select</option></select>
        <button id="playSong" class="btn btn-red" type="submit" 
          name="play">Play Now!</button>
    </div>
    <div class="gamePanel spanAuto span230">
        <div class="span50p">
        <span class="notice">></span>
            <h3>Score</h3>
        <hr/>
        </div>
        <div class="span50p">
            <div id="score" class="info red">0</div>
        </div>
    </div>
    
    <div class="gamePanel spanAuto span230">
        <div class="span50p">
        <span class="notice">></span>
            <h3>Keyboard</h3>
        <hr/>
        </div>
        <div class="span50p">
            <div id="keyboard" class="info keyboardInfo"></div>
        </div>
    </div>
    
</div>

````

## Game Time - JavaScript

To get started we have created a new JavaScript Object you are going to need to build to complete the game, this object is the __Game__ itself.  

### Object
A JavaScript Object is a code representation of an REAL THING or ENTITY.  In our game we had serveral objects
* Piano
* Keyboard
* Tunes
* MusicKey

You can easily visual what these are on the screen.  An object can have functions which like the Music Key has a play function to play the note.  They can also have variables values like the piano has a keyboard.


### To create a JavaScript Object 

You start with the word __function__ followed by the __object name__ in our case Game.  If you would like to pass any additionaly information into the object you can do that inside circular brackets with a parameter __()__.  Inside the brackets you can add some 
variable that will be used inside the Game object, as we need to know __keyboard__ information this is passed in

````javascript
function Game(keyboard) {
        
}
````

The Game object along with the __isGameRunning__ are already setup in game.js as they are being used by piano.js, we will now start adding the rest of the required code for our game.

````javascript
function Game(keyboard) {

    this.isGameRunning = isGameRunning;
    
    function isGameRunning() {

    }

}
````

### Functions
Functions perform single actions for you in the code, in this example our function checks if the game is running.  Dont worry we will add the code later

To add a function
* Start with the word __function__
* Then add the function name in our case __isGameRunning__
* Then add circular brackets __()__
* Open the function code with open bracket __{__
* Close the function code with close bracket __}__, add this a few lines down

__NOTE__ Later we will see how to pass paramters to your function between __()__

### Sharing functions

Functions be default inside Java Script objects can only be called by other functions inside that JavaScript Object.  But some functions you will want to be called by other code for example when the keyboard is hit on the piano you want to tell the game right? Ye so the game can calculate if the correct key was hit and update the score.

To share a function use 
* Add __this__ which means the current object in our case the Game
* Then add __.__ and the name of the function __isGameRunning__
* Then add __=__ equals the function name __isGameRunning__

Just like below

```` this.isGameRunning = isGameRunning; ````

Here you can see the code to share a function, and the creation of the same function

````javascript
function Game(keyboard) {

    this.isGameRunning = isGameRunning;
    
    function isGameRunning() {

    }

}
````  

Before we get started with the code lets review what we want our game to do
* Setup the game
* Loads songs
* Display notes
* Display computer keyboard key
* Manage scoring

### Setup the game

We now need to setup the game, so remember when we worked with the HTML we allow users to select a song for their game
and we added a score panel for the score.  So lets get started with adding a variable for each of these
* songs drop down - to provide a drop down list of songs
* score - to hold the score value
* score panel - to display the score on the screen


#### Variable
A variable is something we can store values against such as score, of something we want to change such as the scorePanel. In JavaScript to create a variable

* Start with the word __var__
* Then add the variable name in our case __score__ (NOTE: no spaces in the variable name) 
* Then close it with a semicolan __;__

Later we will see assigining a value to a variable, now lets add our 3 variables like so

```` var score; ````

````javascript
function Game(keyboard) {
            
    var songsDropDown;
    var score;
    var scorePanel;

    this.isGameRunning = isGameRunning;
    
    function isGameRunning() {

    }
}
````

Now lets setup the game with a new function called __setupGame__, we always want the function name to be clear, so function name should descripe what the function will do.

Inside the function we want to 
* Get the songs drop down from the HTML code
* Get the score panel from the HTML code
* Set the starting score value

So you may be asking yourself why do we need access to the web page HTML code?  Well if you want to changing anything visual on the screen you will need to access parts of the webpage to do that.

### JQuery
JQuery is a javascript framework, its provides functions to make working with JavaScript easier.  We will use it in a very small way to gain access to parts of our webpage.  To get started we will look for the songs __select__ element.  Remember the __id__ of the __select__ element is __songs__.  To get JQuery to return this HTML code
* Set the variable your are assigning it to __songsDropDown__ and then add __equals__
* Now add __jQuery__ with round __()__ brackets
* Inside the round brackets __()__ add __#__ to find the value based on id of HTML element in our case __songs__
* Finished with __;__
* Should now look like this ```` songsDropDown = jQuery("#songs"); ````

We will now need to find the HTML elememts for __songsDropDown__ and __scorePanel__ inside the __setupGame()__ function
* __songsDropDown = jQuery("#songs");__
* __scorePanel = jQuery("#score");__

Our game.js will now look like this

````javascript
function Game(keyboard) {
            
    var songsDropDown;
    var score;
    var scorePanel;

    this.isGameRunning = isGameRunning;
    
    setupGame();

    function setupGame() {
        songsDropDown = jQuery("#songs");
        scorePanel = jQuery("#score");
    }
}
````

Its time to add the __score__, would you agree the start value for the score is __0__, to do this simply
* variable name __score__ followed by __equals__ and then the value __0__ and finish with __;__

Set the score to zero inside the __setupGame()__ function, just below where you set the __scorePanel__

````javascript
function Game(keyboard) {
            
    var songsDropDown;
    var score;
    var scorePanel;

    this.isGameRunning = isGameRunning;
    
    setupGame();

    function setupGame() {
        songsDropDown = jQuery("#songs");
        scorePanel = jQuery("#score");
        score = 0;
    }
}
````

### Lets load the songs into the play list

Great you have written your first part of the game code, but not seen anything happen on the screen yet, its time to start having more fun.  Remember we developed a panel
to display the game songs.  Well its now time to load these

![alt text](https://raw.github.com/CoderDojo/piano-game/master/game/doc-files/play-note.png "Piano Rock Star")

To get started we need to create a new function called __loadTunes__, this will be created just below the __setupGame()__ function.  so how do you create a function again?
* Start with the word __function__
* Space then the function name __loadTunes__
* Now round brackets __()__ and then opening function bracket __{__
* Hit Enter twice and the add closing function bracket __}__


````javascript
    function loadTunes() {
        
    }

````
Lets start coding this function by creating a new tunes variable with from the __Tunes__ object.


````javascript
    function loadTunes() {
        var tunes = new Tunes();
    }

````

Sure go ahead a talk a look at __tunes.js__, you will see the songs available inside this file along with the music note and the corresponding key.  

Inside tunes.js there is an object called __Tunes__ this object has one variable called __list__ which has the tunes.

Now extend the __loadTunes__ function to set the __tunesList__ to your new variable __tunes__ and retrieve the __list__ of tunes.


````javascript
    function loadTunes() {
        var tunes = new Tunes();
        tunesList = tunes.list;
    }

````

You now need to call this function from the __setupGame__function so add the call to the last line of that function.

````javascript
function setupGame() {
        songsDropDown = jQuery("#songs");
        scorePanel = jQuery("#score");
        score = 0;
        loadTunes();
    }
````

Now its time to add this function called __loadSongsToScreen__ that will 
* navigate through the list of tunes
* get their name
* display it on the screen 

So get started with creating a function called __loadSongsToScreen__

````javascript
    function loadSongsToScreen() {
    
    }
````

### for loop
A __for__ loop allows you to preform a set of actions a dedicated number of times.  In 
our example we want a the __for__ loop to navigate through our list and add the name to the screen.

To write a __for__ loop
* Start with the word __for__
* Add round brackets __()__
* Inside the round bracket start with assigning the first number for a variable __var currentSongNumber = 0; __ closing with a semi colan __;__
* Now add the evaluation, in our case the currentSongNumber is less than the max in the element in the list __currentSongNumber < tunesList.length;__ and close with semicolan
* We will need to navigate through each song, so if __currentSongNumber__ represents the current song number then we must increase this every time.
* Now add open brackets __{__
* Hit enter twice and add closing bracket __{__

The __for__ loop should now look like this

````javascript
    for(var currentSongNumber = 0; currentSongNumber < tunesList.length; currentSongNumber = currentSongNumber+1) {
            
    } 
````
In between the brackets we will add the code to get the name and add it to the screen. 

### List note:
The first element in the list is zero, not one.

The first line of code will require us to create a variable for the sone name for current Song Number, this can be done a list by using the list variable name __tunesList__ the use square brackets __[]__ then inside the square brakets add the current song number of the song you want to use.  From the song you can retrieve the name by adding a dot __.__ then the variable name __name__


````javascript
var songName = tunesList[currentSongNumber].name;
````

The __loadSongsToScreen__ function should now look like this

````javascript

    function loadSongsToScreen() {
        for(var currentSongNumber = 0; currentSongNumber < tunesList.length; currentSongNumber = currentSongNumber+1) {
            var songName = tunesList[currentSongNumber].name;
            
        } 
    }
````

Now lets create a function just under the __loadSongsToScreen__ function that will add an individual song name to the screen.  The function should be called __appendOption__ and take in two parameters
* First is the song name you want to see on the screen
* Second is the currentSongNumber, the location this song is in the tune list

Create a function to look like this

````javascript
    function appendOption(songName, songVal) {
       
    }
````

Inside this function you want to add the HTML code so it appears on the screen, you may remember 
* adding ````<select> ```` tag for the songs
* in the __setupGame__ function retrieve the __songsDropDown__ using its songs id

We can simply add HTML to this __songsDropDown__, to add an option to __select__ tag, the tag name is __option__, you can add
* __value__ 
* __display text__

To append the HTML to the __songsDropDown__ call ```` songsDropDown.append() ````, inside the brackets you can add the html, in our case

```` <option value="' +songVal+'">'+
            songName +'</option> ````

The __appendOption__ function should now look like this

````javascript
    function appendOption(songName, songVal) {
       songsDropDown.append('<option value="' +songVal+'">'+
            songName +'</option>');
    }
````
 
We now need to call the __appendOption__ function from the __loadSongsToScreen__.

````javascript

    function loadSongsToScreen() {
        for(var currentSongNumber = 0; currentSongNumber < tunesList.length; currentSongNumber = currentSongNumber+1) {
            var songName = tunesList[currentSongNumber].name;
            appendOption(soneName, currentSongNumber);
        } 
    }
````

### Handle the playing of the song

To play the game the user selects a song and they are scored based on how well the song
is played.  

Create a function to handle this called __handlePlaySong__. We need this function to
* get the play button
* setup the button to play the song on click 

````javascript
    function handlePlaySong() {
 
    }
````

We need to get the playSong button and this can be retrieving the object with jquery function using the element __id__ which is __playSong__.  Assign the button to a new
variable called __playButton__.

````javascript
    var playButton = jQuery("#playSong");
````

Now we want to add the functionality for when the button is clicked.  To do this you call __click__ function on the __playButton__ and tell it to play the song by calling the __playSong__

````javascript
    function handlePlaySong() {
        var playButton = jQuery("#playSong");
        playButton.click(function() {
            playSong();         
        });
    }
````

### Playing song

To play the song we need to 
* Get the selected song from the dropdown
* Get the selected value
* Create the song from the value
* Set the score to zero
* Set the score panel to zero
* Play the song

Get started by creating the __playSong()__ function
````javascript
    function playSong() {
        
    }
````

#### Get the selected song from the dropdown
We will create a new variable called songOption which will get the selected song from the drop down.  This can be done by using the
* __jQuery__ function 
* Followed by the id with hash __#songs__
* Then you can add __option:selected__ to return the choosen value

The code here takes the choosen value and assigns it to a variable __songOption__

````javascript
    function playSong() {
        var songOption = jQuery("#songs option:selected");
    }
````

#### Get the selected value

Now we need to get the song value (remember we set this to the number in the __loadSongsToScreen__ function).  To get the value all you need to do is call the __val()__ function on the __songOption__ variable.

Assign the __songOption.val()__ value to a new variable called __songValue__

````javascript
    function playSong() {
        var songOption = jQuery("#songs option:selected");
        var songValue = songOption.val();
    }
````

#### Create the song from the value

We can now create teh song by
* retrieving the tune from the __tunesList__ the __songValue__ ```` tunesList[songValue] `````
* setting the song timeout be 1000 milli-seconds between note
* set the keyboard into the song
* Create the new variable called __song__ using the __Song__ object already created for you.

````javascript
    function playSong() {
        var songOption = jQuery("#songs option:selected");
        var songValue = songOption.val();
        song = new Song(tunesList[songValue], 1000, keyboard);
    }
````

#### Set the score to zero

Set the score variable to zero by creating a shared variable at the top and then updating the variable value in the __playSong__ function.  We created a shared variable earlier so more than 1 function can use it.  All our share variables are at the top of the screen.

Now inside the __playSong__ function set this to __0__

````javascript
    function playSong() {
        var songOption = jQuery("#songs option:selected");
        var songValue = songOption.val();
        song = new Song(tunesList[songValue], 1000, keyboard);
        score = 0;
    }
````

#### Set the score panel to zero

Update the scorePanel to have the zero __text__ value

````javascript
    function playSong() {
        var songOption = jQuery("#songs option:selected");
        var songValue = songOption.val();
        song = new Song(tunesList[songValue], 1000, keyboard);
        score = 0;
        scorePanel.text(score);
    }
````

* Play the song

The song variable we create early has a function called __play()__ which plays the nodes on the screen.  Can you now add this the play functionality to this function using the __song__ variable.

````javascript
    function playSong() {
        var songOption = jQuery("#songs option:selected");
        var songValue = songOption.val();
        song = new Song(tunesList[songValue], 1000, keyboard);
        score = 0;
        scorePanel.text(score);
        song.play();
    }
````

### Is game running

So why do we want to know if the game is running? Well the piano needs to know, if the game is playing the key information is sent to the game.  

How do you know the game is running, well if the notes are playing? Lets create a function to handle this called isGameRunning.

````javascript
    function isGameRunning() {
        
    }
````

Get the current note from the song, but we have not defined the song yet, right

````javascript
    function isGameRunning() {
        var currentNote = song.note();
    }
````

Using the scorePanel

````javascript
    function isGameRunning() {
        var currentNote = song.note();
        //if current note is blank game not playing
        if(currentNote == "") {
            return false;
        } else { //note value is not blank so game playing
            return true;
        }
    }
````

### Handle the keyboard click

Normally when the keyboard clicks in the piano it just plays a sound right, but when added the game the keyboard click got
so much more important as we now need to
* Get the current note
* Get the keyboard key hit
* Get the keyboard key for the current note
* Check if the selected keyboard key and note keyboard key match
* If they do match, we should play the note
* Then add 10 to the score
* Then display the new score

To get stared create function called __handleKeyboardClick__ that takes in a parameter called __keyHit__

````javascript
    function handleKeyboardClick(keyHit) {
    }
````

#### Get the current note

You can get the __currentNote from the __song__ object with function __note()__, so can you create a variable called __currentNote__ to retrieve this value


````javascript
    function handleKeyboardClick(keyHit) {
        var currentNote = song.note();
    }
````

#### Get the keyboard key hit

The current key for the note can be retrieved from the __song__ object __getCurrentKey()__ function, can you create a new variable called __musicKey__ to retrieve this value.

````javascript
    function handleKeyboardClick(keyHit) {
        var currentNote = song.note();
        var musicKey = song.getCurrentKey();
    }
````

#### Get the keyboard key for the current note

The __keyboard__ object has a function called __getKey()__ which takes in the __currentNote__ as a paranter and wiull return keyboardKey for that note.

````javascript
    function handleKeyboardClick(keyHit) {

        var currentNote = song.note();
        var musicKey = song.getCurrentKey();
        var keyboardKey = keyboard.getKey(currentNote);

    }
````

#### Check if the selected keyboard key and note keyboard key match

Create an __if__ condition that checks if the __keyHit__ equals the __keyboardKey__

````javascript
    function handleKeyboardClick(keyHit) {

        var currentNote = song.note();
        var musicKey = song.getCurrentKey();
        var keyboardKey = keyboard.getKey(currentNote);

        if(keyHit == keySelect) {
            
        }
    }
````


#### If they do match, we should play the note

To play the note the __musicKey__ variable has a function called __clickNote()__ which should be added inside the __if__ condition.

````javascript
    function handleKeyboardClick(keyHit) {

        var currentNote = song.note();
        var musicKey = song.getCurrentKey();
        var keyboardKey = keyboard.getKey(currentNote);

        if(keyHit == keySelect) {
            musicKey.clickNote();
        }

    }
````

#### Then add 10 to the score

To add 10 to the score we will just increase the variable value by 10.  

````javascript
    function handleKeyboardClick(keyHit) {

        var currentNote = song.note();
        var musicKey = song.getCurrentKey();
        var keyboardKey = keyboard.getKey(currentNote);

        if(keyHit == keySelect) {
            musicKey.clickNote();
            score = score + 10;
        }

    }
````

#### Then display the new score 

To display the new score we will need to update the __scorePanel__ usiung its __text__ function with the __score__ value as a parameter.

````javascript
    function handleKeyboardClick(keyHit) {

        var currentNote = song.note();
        var musicKey = song.getCurrentKey();
        var keyboardKey = keyboard.getKey(currentNote);

        if(keyHit == keySelect) {
            musicKey.clickNote();
            score = score + 10;
            scorePanel.text(score);
        }
    }
````

## Congratulations

Well done you have just developed Piano Rock Star, go time to do a full test and play against your friends to see who wins.  Be cool

