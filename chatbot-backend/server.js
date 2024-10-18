const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');
const cors = require('cors');
const path = require('path');

const app = express();
app.use(cors());
app.use(bodyParser.json());

// Serve static files from the 'frontend' directory
app.use(express.static(path.join(__dirname, '../frontend')));

app.post('/api/chat', async (req, res) => {
    try {
        const userMessage = req.body.message;
        const response = await axios.post('http://localhost:8000/chat', { message: userMessage });

        // Ensure that the response from the Python backend is properly structured
        res.json({ response: response.data.response });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'An error occurred while processing your request.' });
    }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
