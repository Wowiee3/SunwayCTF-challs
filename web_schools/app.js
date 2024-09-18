const express = require("express")
const path = require("path")
const fs = require('fs');

const app = express()
const PORT = 5001

app.use(express.urlencoded({ extended: false }))
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.get('/file', (req, res) => {
    let school = req.query.school;

    if (school.includes('self')){
        res.status(500).send('Flag stealer detected, no reading node process environment variables.')
        return
    }

    // Sanitise school path to prevent file inclusion
    school = school.replaceAll("../", '')
    
    const filePath = path.join(__dirname, 'public', school);
  
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
          res.status(500).send('Error finding school');
          return;
        }
        res.send(data);
      });
  });
  
  
app.listen(PORT,()=>{
    console.log(`[+] Started on ${PORT}`)
})