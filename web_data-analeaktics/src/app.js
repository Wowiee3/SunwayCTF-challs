'use strict';

const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');
const cors = require('cors');
const path = require('path');
const console = require("node:console");
const res = require("express/lib/response");

const app = express();
app.use(bodyParser.json());
app.use(cors());
app.use(express.static(path.join(__dirname, 'public')));

const db = mysql.createConnection({
    socketPath: '/var/run/mysqld/mysqld.sock',
    // host: 'localhost',
    user: 'root',
    password: 'root',
    database: 'sunctf'
});

db.connect((err) => {
    if (err) {
        throw err;
    }
    console.log('Connected to MySQL database');
});

app.get('/search', (req, res) => {
    const sortBy = req.query.sortBy || 'id';  // Default sorting by id

    if (!/^[\x20-\x7E]*$/.test(sortBy) || sortBy.split(' ').length - 1 > 1) {
        return res.status(400).json({error: 'malicious'});
    }
    for (const c of '~}|[,./$%!>={@#]\\:";\'*_+`-<^&?') {
        if (sortBy.includes(c)) {
            return res.status(400).json({error: 'malicious'});
        }
    }

    const query = `SELECT * FROM customers ORDER BY ${sortBy} LIMIT 10`;

    db.query(query, (err, results) => {
        if (err) {
            console.error('Error retrieving records:', err);
            return res.status(500).json({error: 'Failed to fetch orders'});
        }

        if (!Array.isArray(results)) {
            console.error('Results not an array:', results);
            return res.status(500).json({error: 'Unexpected result type'});
        }

        res.status(200).json(results);
    });
});

app.listen(5004, () => {
    console.log('Server is running on port 5004');
});
