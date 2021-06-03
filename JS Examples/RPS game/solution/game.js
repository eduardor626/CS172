function play(userChoice) {
	var item = document.getElementById("result");
	var pcChoice = randomChoice();

	if (userChoice==pcChoice) {
		item.innerHTML= "its a tie";
	}
	else if (userChoice=="rock" && pcChoice =="scissor" ||
		     userChoice=="scissor" && pcChoice =="rock" ){
		item.innerHTML= "you win";
	} else{
		item.innerHTML= "you lose";
	}
}

function randomChoice() {
	var choice = Math.floor(Math.random()*3+1);
	switch(choice){
		case 1:  return "rock";
				 break;
		case 2:  return "paper";
				 break
		case 3:  return "scissor";
				 break;
		}
	/* returns a random number between 1-3 */
}