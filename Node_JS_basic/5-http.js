const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  if (req.url === '/') {
    res.write('Hello Holberton School!');
  }
  if (req.url === '/students') {
    res.write('This is the list of our students');
    res.write(`${await countStudents(process.argv[2])}`);
  }
  res.end();
}).listen(1245);

module.exports = app;
