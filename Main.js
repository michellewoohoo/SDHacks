const express = require('express')
const app = express()

app.use(express.static('templates'));

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/templates/home.html');
})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})