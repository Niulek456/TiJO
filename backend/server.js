require('dotenv').config();
const express = require('express');
const cors = require('cors');
const axios = require('axios');

const app = express();
app.use(cors());
app.use(express.json());

app.post('/analyze', async (req, res) => {
    const { codeSnippet } = req.body;

    try {
        const response = await axios.post(
            'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent',
            {
                contents: [{ parts: [{ text: codeSnippet }] }],
                generationConfig: {
                    temperature: 0.2,
                    maxOutputTokens: 512,
                },
            },
            {
                params: {
                    key: process.env.GEMINI_API_KEY,
                },
            }
        );

        res.json({ analysis: response.data.candidates[0].content.parts[0].text });
    } catch (err) {
        console.error(err.response?.data || err.message);
        res.status(500).json({ error: 'Błąd połączenia z API Gemini.' });
    }
});

app.listen(4000, () => console.log('✅ Backend działa na http://localhost:4000'));
