const mongoose = require('mongoose');
require('dotenv').config(); // Load environment variables

const connectDB = async () => {
    try {
        console.log('MONGO_URI:', process.env.MONGO_URI); // Log to verify connection string
        const conn = await mongoose.connect(process.env.MONGO_URI, {
            useNewUrlParser: true,
            useUnifiedTopology: true,
        });
        console.log(`MongoDB Connected: ${conn.connection.host}`);
    } catch (err) {
        console.error('MongoDB connection error:', err);
        process.exit(1); // Exit process with failure
    }
};

module.exports = connectDB;
