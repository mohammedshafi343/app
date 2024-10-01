import React, { useState } from 'react';

const flashcards = [
    { question: "What is the capital of France?", answer: "Paris" },
    { question: "What is 2 + 2?", answer: "4" },
    { question: "What is the largest planet?", answer: "Jupiter" },
];

function App() {
    const [index, setIndex] = useState(0);
    const [showAnswer, setShowAnswer] = useState(false);

    const nextCard = () => {
        setIndex((prevIndex) => (prevIndex + 1) % flashcards.length);
        setShowAnswer(false);
    };

    return (
        <div>
            <h1>Flashcards</h1>
            <div>
                <h2>{flashcards[index].question}</h2>
                {showAnswer && <h3>{flashcards[index].answer}</h3>}
                <button onClick={() => setShowAnswer(!showAnswer)}>
                    {showAnswer ? "Hide Answer" : "Show Answer"}
                </button>
                <button onClick={nextCard}>Next Card</button>
            </div>
        </div>
    );
}

export default App;
