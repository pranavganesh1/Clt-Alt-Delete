// Load environment variables
require('dotenv').config();

// Import dependencies
const express = require('express');
const cors = require('cors');
const connectDB = require('./config/db'); // Adjust path if necessary

// Initialize express app
const app = express();

// Connect to MongoDB
connectDB();

// Middleware
app.use(cors()); // Enable CORS
app.use(express.json()); // Parse JSON requests

// Routes
app.use('/api/reports', require('./routes/reports')); // Adjust path if necessary

// Define the port
const PORT = process.env.PORT || 5000;

// Start the server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
