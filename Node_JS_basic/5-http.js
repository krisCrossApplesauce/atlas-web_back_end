const http = require('http');
const fs = require('fs').promises;

const app = http.createServer(async (req, res) => {
  if (req.url === '/') {
    res.write('Hello Holberton School!');
  }
  if (req.url === '/students') {
    res.write('This is the list of our students\n');
    const path = process.argv[2];
    let idx;
    let i;
    let ii;
    let y;
    let x;
    try {
      const data = await fs.readFile(path, { encoding: 'utf8', flag: 'r' });
      const studs = data.split('\n');
      const students = [];
      for (idx = 0; idx < studs.length - 1; idx += 1) {
        students.push(studs[idx].split(','));
      }

      const studObjs = [];
      for (i = 1; i < students.length; i += 1) {
        const temp = {};
        for (ii = 0; ii < students[0].length; ii += 1) {
          temp[students[0][ii]] = students[i][ii];
        }
        studObjs.push(temp);
      }

      res.write(`Number of students: ${studObjs.length}\n`);

      const distinctFields = [...new Set(studObjs.map((x) => x.field))];

      for (y = 0; y < distinctFields.length; y += 1) {
        const studsInField = [];
        for (x = 0; x < studObjs.length; x += 1) {
          if (studObjs[x].field === distinctFields[y]) studsInField.push(` ${studObjs[x].firstname}`);
        }
        res.write(`Number of students in ${distinctFields[y]}: ${studsInField.length}. List:${studsInField}\n`);
      }
    } catch (err) {
      res.write('Cannot load the database');
    }
  }
  res.end();
}).listen(1245);

module.exports = app;
