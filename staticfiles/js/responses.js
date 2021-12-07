function getBotResponse(input) {
    //rock paper scissors
    if (input == "blood groups") {
        return "A+ A- B+ B- AB+ AB- O+ O-"
    } else if (input == "paper") {
        return "scissors";
    } else if (input == "scissors") {
        return "rock";
    }

    // Simple responses
    if (input == "hello" || input == "hi" || input == "hey") {
        return "Hello there!";
    } else if (input == "goodbye" || input == "bye") {
        return "Talk to you later!";
    } else {
        return "Try asking something else!";
    }
}