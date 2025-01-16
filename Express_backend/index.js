const express = require('express');
const cors = require('cors');
const app = express();
const PORT = 3000;

// Enable CORS
app.use(cors());

app.use(express.json());

const randomNumber = Math.floor(Math.random() * 100);

app.post('/guess', (req, res) => {
    const guess = req.body.number; // Get the number from the request body
    let message = '';
    if (guess < randomNumber) {
        message = 'Too low!';
    } else if (guess > randomNumber) {
        message = 'Too high!';
    } else {
        message = 'You guessed it!';
    }
    res.send({ 
        message: message,
        number: randomNumber
    });
});
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
