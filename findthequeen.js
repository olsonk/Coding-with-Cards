// set up and relate to canvas
var my_canvas = document.getElementById('canvas');
var context = my_canvas.getContext('2d');
my_canvas.addEventListener("mousedown", doMouseClick, false);

var suits = ["Clubs", "Hearts", "Spades", "Diamonds"];
var values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"];

var deck = [];

function Card(value, suit) {
    this.value = value;
    this.suit = suit;
    this.name = this.value + " of " + this.suit;
	this.isRed = function() {
		if (this.suit === "Diamonds" || this.suit === "Hearts") {
			return true;
		} else {
			return false;
		}
	};
}

function Player(number, name) {
	this.number = number;
	this.name = name;
	this.points = 0;
}

var updateScores = function() {
	context.fillStyle = 'white';
	context.fillRect(90, 480, 410, 55);
	context.fillStyle = 'black';
	context.fillText(player1.points, 120, 510);
	context.fillText(player2.points, 420, 510);
};

var currentPlayer = function(player) {
	if (player.name === player1.name) {
		context.strokeStyle = 'red';
		context.strokeRect(90, 540, 80, 40);
		context.strokeStyle = 'white';
		context.strokeRect(390, 540, 80, 40);
	} else {
		context.strokeStyle = 'red';
		context.strokeRect(390, 540, 80, 40);
		context.strokeStyle = 'white';
		context.strokeRect(90, 540, 80, 40);
	}
};

var player1 = new Player(1, prompt("Player 1, enter your name:"));
var player2 = new Player(2, prompt("Player 2, enter your name:"));

context.font = "20px Garamond";

context.fillText(player1.name, 100, 560);
context.fillText(player2.name, 400, 560);
updateScores();

// create the deck
for (var suitcounter = 0; suitcounter < 4; suitcounter++) {
    for (var valuecounter = 0; valuecounter < 13; valuecounter++){
        var newCard = new Card(values[valuecounter], suits[suitcounter]);
        deck.push(newCard);
    }
}

// shuffle the cards
var shuffle = function (o) {
	for(var j, x, i = o.length; i; j = Math.floor(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
    return o;
};

shuffle(deck);

/*
// test to make sure all cards are in deck

context.fillStyle = 'black';
context.font = "8px Garamond";
var yPlace = 10;
for (var i = 0; i < deck.length; i++) {
	context.fillText(deck[i].name, 40, yPlace);
	yPlace += 10;
}
*/

// choose a random card from the deck, and return its array index
var usedCards = [];

var drawCard = function() {
	if (deck.length < 1) {
		context.fillStyle = "black";
		context.fillText("Out of Cards! Game Over!", 300, 300);
	}
	var card = deck.pop();
	usedCards.push(card);
	context.fillStyle = '#FFFFAA';
	context.fillRect(200, 50, 125, 200);
	if (card.isRed()) {
		context.fillStyle = 'red';
	} else {
		context.fillStyle = 'black';
	}
	context.fillText(card.value, 215, 75);
	context.fillText(card.suit, 220, 150);
	if (card.value === "10") {
		context.fillText(card.value, 300, 230);
	} else {
		context.fillText(card.value[0], 300, 230);
	}
	return card;
};

var play = function(player, opponent, card) {
	currentPlayer(player);
	player.points++;
	if (card.suit === "Hearts") {
		player.points++;
		updateScores();
	} else {
		context.fillStyle = 'black';
		context.fillText("Opponent's turn", 50, 50);
	}
};

// 'pick' button
context.fillStyle = 'green';
context.fillRect(450, 20, 150, 40);

context.fillStyle = 'white';
context.fillText("Pick a Card", 480, 45);

// Click "Pick a Card!" button and draw the chosen card on the canvas
function doMouseClick(event) {
	var canvasX = event.pageX;
	var canvasY = event.pageY;
	if (canvasX >= 450 && canvasX <= 600 && canvasY >= 20 && canvasY <= 80) {
		var drawnCard = drawCard();
		while (drawnCard.isRed()) {
			play(player1, player2, drawnCard);
			drawnCard = drawCard();
		}
	}
};