function countStudents(path) {
  const fs = require('fs');
  let data;
  try {
    data = fs.readFileSync(path, { encoding: 'utf8', flag: 'r' });
  }
  catch(err) {
    throw new Error('Cannot load the database');
  }

  const studs = data.split('\n');
  const students = [];
  for (s in studs) {
    students.append(s.split(','));
  }

  console.log(`Number of students: ${studs.length - 1}`);

  let nameIndex = 0;
  let fieldIndex = 0;
  for (i = 0; i < students[0].length; i++) {
    if (students[0][i] == 'name')
      nameIndex = i;
    if (students[0][i] == 'field')
      fieldIndex = i;
  }

  const fields = [];
  for (ii = 0; ii < studs.length - 1; ii++) {
    if (!(studs[ii][nameIndex] in fields.names)) {
      fields.names.append(studs[ii][nameIndex]);
    }

  }

  for (field in data.field) {
    list = '';
    count = 0;
    for (stud in data) {
      if (stud.field == field) {
        if (list != '')
          list += ', ';
        list += str(stud.firstName);
        count++;
      }
    }
    console.log(`Number of students in ${field}: ${count}. List: ${list}`);
  }
};

module.exports = countStudents;
