const express = require('express');
const router = express.Router();

// Define your route
router.get('/', (req, res) => {
    res.send('Reports route');
});

// Export the router
module.exports = router;
