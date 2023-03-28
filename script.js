const textOutput = document.getElementById("text");
const buttonOptions = document.getElementById("buttons");
const finalScoreOutput = document.getElementById("score");
// const imageOut = documnet.getElementById("mainImage");

var scoreOphelia = 0;
var scoreHamlet = 0;
var scoreGertrude = 0;
var scoreCladius = 0;

//making sure that scores are correct
console.log(scoreOphelia);
console.log(scoreHamlet);
console.log(scoreGertrude);
console.log(scoreCladius);

var myStage;
var myBg;
let state = {};
//this will start the test 
function startTest() {
    //begin with all states being empty
    state = {};
    //begin by showing the first text
    showText(1);
}

//this shows text
function showText(textIndex) {
    //textInfo will use the inputed number to find the correct textId 
    //then present to user
    const textInfo = texts.find(textInfo => textInfo.id === textIndex);

    //display text to the window
    textOutput.innerText = textInfo.text;

   //going to create the a child for each button then remove it
    while (buttonOptions.firstChild) {
        buttonOptions.removeChild(buttonOptions.firstChild);
    }
    //display the button options on the actual button elements
    textInfo.options.forEach(option => {
        if (showingOption(option)) {
            const button = document.createElement("button");
            button.innerText = option.text;
            button.classList.add("btn");
            button.addEventListener("click", () => decisions(option));
            buttonOptions.appendChild(button);
        }
    });

    //updating scores and makign sure they are going through 
    const scoreO = texts.find(scoreO => scoreO.id === textIndex);
    console.log(scoreO.scoreOpheliaUpdate);
    scoreOphelia = scoreOphelia + scoreO.scoreOpheliaUpdate;
    console.log("Ophelia Score: " + scoreOphelia);

    const scoreH = texts.find(scoreH => scoreH.id === textIndex);
    console.log(scoreH.scoreHamletUpdate);
    scoreHamlet = scoreHamlet + scoreH.scoreHamletUpdate;
    console.log("Hamlet Score: " + scoreHamlet);

    const scoreG = texts.find(scoreG => scoreG.id === textIndex);
    console.log(scoreG.scoreGertrudeUpdate);
    scoreGertrude = scoreGertrude + scoreG.scoreGertrudeUpdate;
    console.log("Gertrude Score: " + scoreGertrude);

    const scoreC = texts.find(scoreC => scoreC === textIndex);
    console.log(scoreC.scoreCladiusUpdate);
    scoreCladius = scoreCladius + scoreC.scoreCladiusUpdate;
    console.log("Cladius Score: " + scoreCladius);

}

//returns the state of an object 
function showingOption(option) {
    return option.requiredState == null || option.requireState(state);
}

function decisions(option) {
    const textIndex = option.nextText;
    //this is a state error capture
    //if the state is different from the the actual options are 
    //then otion.steState had the power to change the state
    state = Object.assign(state, option.setState);
    //show text
    showText(textIndex);
}

const texts = [
    //test start 
    {
        id: 1,
        text: "To Be or Not To Be? Who are you?",
        options: [
            {
                text: "Start",
                setState: {testBegin: true},
                nextText: 2
            },
            {
                text: "Exit",
                nextText: 0
            }
        ]
    },
    //are you sure for not taking the test
    {
        id: 0, 
        text: "Are you sure you want to leave?", 
        options: [
            {
                text: "Yes",
                nextText: -1
            }, 
            {
                text: "No", 
                setState: {testBegin: true}, 
                nextText: 1
            }
        ]
        
    },
    //not taking text
    {
        id: -1, 
        text: "Looks like you're a Horatio, only care to show up once in the story"
    }, 
    //
    {
        id: 2, 
        text: "How do you react in a tight situation?",
        options: [
            {
                text: "I fight", 

            }
        ]
    }
]

startTest();