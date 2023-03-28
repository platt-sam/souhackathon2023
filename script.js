//in order to have multiple options work have to initialize all the text options first
const texts = [
    {
        //question
        choice: "How do you react in a tight situation?", 
        //options
        a: "I fight", 
        b: "Talk it out", 
        c: "I leave it to someone else", 
        d: "You'll never see me in a situation like that",
        //answers
        hamlet: "a",
        ophelia: "b",
        gertrude: "c", 
        cladius: "d"
    }, 
    {
        choice: "Do you believe in ghosts?", 
        a: "Pffft IM NOT CRAZY", 
        b: "The dead rest in peace", 
        c: "Don't be silly, no", 
        d: "Absolutely",
        hamlet: "d",
        ophelia: "b",
        gertrude: "c", 
        cladius: "a"
    }, 
    {
        choice: "Do you check your curtains?", 
        a: "No my maids open them everyday", 
        b: "I throw an object at them and see if they make a noise before checking", 
        c: "No I have other people do that", 
        d: "Yes every morning when I draw them open and close them at night",
        hamlet: "b",
        ophelia: "a",
        gertrude: "c", 
        cladius: "d"
    }, 
    {
        choice: "Your best friends piece of art has been vandalized! What do you do?", 
        a: "Seek Revenge", 
        b: "Console your friend before doing anything serious", 
        c: "Seek assistance from officers/those above to help with the situation", 
        d: "Talk to my friends and work as a group to find the culprit",
        hamlet: "a",
        ophelia: "b",
        gertrude: "c", 
        cladius: "d"
    }, 
    {
        choice: "Do you get jealous easily?", 
        a: "No I do not", 
        b: "Only to those that are above me", 
        c: "No I have everythign that I want", 
        d: "Yes, but because they don't deserve it",
        hamlet: "d",
        ophelia: "a",
        gertrude: "c", 
        cladius: "b"
    }, 
    {
        choice: "How are you when you meet new people?", 
        a: "It takes me a long time in order to trust them", 
        b: "Trust and being open to someone is earned not given", 
        c: "I spend a couple of minutes talking to them before opening up", 
        d: "I find meeting new people easy and do not struggle taking to them",
        hamlet: "b",
        ophelia: "d",
        gertrude: "c", 
        cladius: "a"
    }, 
    {
        choice: "Do you believe in justice?", 
        a: "I believe in karma", 
        b: "Justice will come eventually just takes time", 
        c: "Justice must be seeked immediately", 
        d: "There must have been a reaso why it was done",
        hamlet: "c",
        ophelia: "b",
        gertrude: "a", 
        cladius: "d"
    }, 
    {
        choice: "Is blood ever thicker than water?", 
        a: "Depends on the family member", 
        b: "No, blood will always betray you", 
        c: "Water will never question what you do", 
        d: "Yes family will always be there",
        hamlet: "b",
        ophelia: "d",
        gertrude: "a", 
        cladius: "c"
    }, 
    {
        choice: "Would you ever pick up a sword?", 
        a: "No, I am to week to pick one up", 
        b: "Why would I need a sword", 
        c: "Yes, I think i'd look cool with it", 
        d: "Yes, its a great weapon",
        hamlet: "d",
        ophelia: "a",
        gertrude: "b", 
        cladius: "c"
    }, 
    {
        choice: "Do you like nature?", 
        a: "Yes, i enjoy walking around the woods and the creeks", 
        b: "I enjoy walking around in gardens", 
        c: "No, im to busy to do that", 
        d: "HISS THE SUN",
        hamlet: "a",
        ophelia: "a",
        gertrude: "b", 
        cladius: "c"
    }
]

//connect all elements from html file to the js file
const text = document.getElementById("test-box");
const choiceELs = document.querySelectorAll(".choice");
const textEL = document.getElementById("text");

//make sure that all text values from js file go to the correct ones in the html
const aText = document.getElementById("aText");
const bText = document.getElementById("bText");
const cText = document.getElementById("cText");
const dText = document.getElementById("dText");

const submitButton = document.getElementById("submit");

//create variables in order to keep how many questions are on the test 
var currentTest = 0;
//create variables in order to keep count of total score and determine who you are
var scoreOphelia = 0;
var scoreHamlet = 0;
var scoreGertrude = 0;
var scoreCladius = 0;

//call the start test funciton
startTest();

//deselects options and moves text array into the the elements on the html file
function startTest() {
    deselectChoices();
    const currentTexts = texts[currentTest];

    textEL.innerText = currentTexts.choice;
    aText.innerText = currentTexts.a;
    bText.innerText = currentTexts.b;
    cText.innerText = currentTexts.c;
    dText.innerText = currentTexts.d;
}

//after each button set radio button to false/empty
function deselectChoices() {
    choiceELs.forEach(choiceEL => choiceEL.checked = false)
}

//get choice from user and compare it to the answer choice from above
//if user picks a, look for the answer that corresponds to option a
function getChoice () {
    let inInfo
    choiceELs.forEach(choiceEl => {
        if(choiceEl.checked) {
            inInfo = choiceEl.id;
        }
    })
    return inInfo;
}

//when submit button is clicked then check answer and move onto the next question
submitButton.addEventListener('click', () => {
    const inInfo = getChoice();
    if(inInfo) {
        //tests to make sure getting the right answers
        console.log("this is the correct: " + texts[currentTest].hamlet)
        console.log("this is the answer: " + inInfo);
        //if user choice matches to one of the answer add to that counter
        //i.e if user chooses a hamlet like answer add to hamlet counter
        //console logs to make sure that the current values are being placed on the correct score values
        if (inInfo === texts[currentTest].hamlet) {
            scoreHamlet++; 
            console.log("hamlet" + scoreHamlet); 
        } else if (inInfo === texts[currentTest].ophelia){
            scoreOphelia++;
            console.log("ophelia" + scoreOphelia);
        } else if (inInfo === texts[currentTest].gertrude){
            scoreGertrude++;
            console.log("gertrude" + scoreGertrude);
        } else if (inInfo === texts[currentTest].cladius){
            scoreCladius++;
            console.log("cladius" + scoreCladius);
        }
        
        //counts every question after you pass
        currentTest++;
        console.log(currentTest);
        
        //if currentTest number is lower than the current length of all the questions keep the test going
        if (currentTest < texts.length) {
            startTest()
        //else count up the scores and fidn out who you are :D
        } else if (scoreHamlet > scoreOphelia || scoreGertrude || scoreCladius) {
            text.innerHTML = "<h2>YOU ARE HAMLET</h2><br><p>Do you need a hug?</p>"
        } else if (scoreOphelia > scoreGertrude || scoreCladius || scoreHamlet) {
            text.innerHTML = "<h2>YOU ARE OPHELIA</h2><br><p>You are a ray of sunshine in the world and deserve to be happy</p>"
        } else if (scoreGertrude > scoreCladius || scoreHamlet || scoreOphelia) {
            text.innerHTML = "<h2>YOU ARE GERTRUDE</h2><br><p>You're always watching, but you're also not doing anything</p>"
        } else if (scoreCladius > scoreHamlet || scoreOphelia || scoreGertrude) {
            text.innerHTML = "<h2>YOU ARE CLADIUS</h2><br><p>WHAT HAVE YOU DONE! Bruh you caused a domino effect</p>"
        }
    }
});

