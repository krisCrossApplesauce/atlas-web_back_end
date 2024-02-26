var app = require('http');

app.createServer(function (req, res) {
  res.write('Hello Holberton School!');
  res.end();
}).listen(1245);
