const mongoose = require('mongoose');

const ReportSchema = new mongoose.Schema({
    restaurantId: {
        type: String,
        required: true
    },
    description: {
        type: String,
        required: true
    },
    violationType: {
        type: String,
        required: true
    },
    date: {
        type: Date,
        default: Date.now
    }
});

module.exports = mongoose.model('Report', ReportSchema);
