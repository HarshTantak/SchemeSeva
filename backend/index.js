require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

const PORT = process.env.PORT || 8000;
const MONGODB_URL = process.env.MONGODB_URL || 'mongodb://127.0.0.1:27017';
const DB_NAME = process.env.DB_NAME || 'MySchemesDB';

// Mongoose model for Schemes
const schemeSchema = new mongoose.Schema({}, { strict: false, collection: 'Schemes' });
const Scheme = mongoose.model('Scheme', schemeSchema);

// Connect to MongoDB
mongoose.connect(`${MONGODB_URL}/${DB_NAME}`, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// API Endpoints
app.get('/api/schemes', async (req, res) => {
  try {
    const { category } = req.query;
    let query = {};
    if (category) {
      query['Scheme Category'] = category;
    }
    const schemes = await Scheme.find(query);
    res.json(schemes);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.get('/api/schemes/:id', async (req, res) => {
  try {
    const scheme = await Scheme.findById(req.params.id);
    if (!scheme) return res.status(404).json({ error: 'Scheme not found' });
    res.json(scheme);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
}); 