const Report = require('../models/Report');

// Create a new report
exports.createReport = async (req, res) => {
    try {
        const { restaurantId, description, violationType } = req.body;
        
        const newReport = new Report({
            restaurantId,
            description,
            violationType,
        });

        const savedReport = await newReport.save();
        res.status(201).json(savedReport);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Server Error' });
    }
};

// Get all reports
exports.getAllReports = async (req, res) => {
    try {
        const reports = await Report.find();
        res.status(200).json(reports);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: 'Server Error' });
    }
};
