const fs = require('fs');

async function countStudents(path) {
  let idx;
  let i;
  let ii;
  let y;
  let x;
  fs.readFile(path, { encoding: 'utf8', flag: 'r' }, (err, data) => {
    if (err)
      throw new Error('Cannot load the database');

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

    console.log(`Number of students: ${studObjs.length}`);

    const distinctFields = [...new Set(studObjs.map((x) => x.field))];

    for (y = 0; y < distinctFields.length; y += 1) {
      const studsInField = [];
      for (x = 0; x < studObjs.length; x += 1) {
        if (studObjs[x].field === distinctFields[y]) studsInField.push(` ${studObjs[x].firstname}`);
      }
      console.log(`Number of students in ${distinctFields[y]}: ${studsInField.length}. List:${studsInField}`);
    }
  });
}

module.exports = countStudents;
