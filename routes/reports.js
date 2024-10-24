const express = require('express');
const router = express.Router();

// Example: GET request to fetch all reports
router.get('/', (req, res) => {
    res.json({ message: 'GET request to /api/reports - fetching reports' });
});

// Example: POST request to create a new report
router.post('/', (req, res) => {
    const { title, description, date } = req.body;
    if (!title || !description || !date) {
        return res.status(400).json({ message: 'Please provide all required fields' });
    }
    res.json({ message: 'Report created successfully', report: { title, description, date } });
});

module.exports = router;
