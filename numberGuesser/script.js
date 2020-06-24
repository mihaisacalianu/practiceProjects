let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:

const generateTarget = () => {
  let randomNumber = Math.floor(Math.random() * 9);
  console.log(randomNumber);
  return randomNumber;
};

const compareGuesses = (human, computer, secretTarget) => {
  if (human > 9 || computer > 9) {
    alert("Number is out of range");
  } else if (
    getAbsoluteDistance(human, computer) >= getAbsoluteDistance(computer, human)
  ) {
    return true;
  } else if (
    getAbsoluteDistance(human, computer) < getAbsoluteDistance(computer, human)
  ) {
    return false;
  }
};

const getAbsoluteDistance = (num1, num2) => {
  const distance = Math.abs(num1 - num2);
  return distance;
};

const updateScore = (winner) => {
  if (winner === "human") {
    humanScore += 1;
  } else if (winner === "computer") {
    computerScore += 1;
  }
};

const advanceRound = () => {
  currentRoundNumber += 1;
};
