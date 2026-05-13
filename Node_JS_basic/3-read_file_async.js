const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);

      const fields = {};
      for (const student of students) {
        const parts = student.split(',');
        const firstName = parts[0];
        const field = parts[3];
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
      }

      const output = [];
      output.push(Number of students: ${students.length});
      console.log(Number of students: ${students.length});

      for (const [field, names] of Object.entries(fields)) {
        const line = Number of students in ${field}: ${names.length}. List: ${names.join(', ')};
        output.push(line);
        console.log(line);
      }

      resolve(output);
    });
  });
}

module.exports = countStudents;
