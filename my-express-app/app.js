const express = require('express');
const app = express();
const port = 3000;

// Set the view engine to ejs
app.set('view engine', 'ejs');

// Serve static files from the 'public' folder
app.use(express.static('public'));

// Route for the homepage
app.get('/', (req, res) => {
    res.render('index');
});

// Route for the second page
app.get('/second', (req, res) => {
    res.render('second');
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});

