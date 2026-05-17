import fs from 'fs';

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) {
        reject(err);
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);
      const fields = {};

      students.forEach((student) => {
        const [firstName, , , field] = student.split(',');
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
      });

      resolve(fields);
    });
  });
}

export default readDatabase;
