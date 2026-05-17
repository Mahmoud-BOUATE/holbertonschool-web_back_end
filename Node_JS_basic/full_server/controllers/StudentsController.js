import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response) {
    const databaseFile = process.argv[2];

    readDatabase(databaseFile)
      .then((students) => {
        const fields = Object.keys(students).sort((fieldA, fieldB) => (
          fieldA.toLowerCase().localeCompare(fieldB.toLowerCase())
        ));
        const lines = ['This is the list of our students'];

        fields.forEach((field) => {
          const names = students[field];
          lines.push(
            `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`,
          );
        });

        response.status(200).send(lines.join('\n'));
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;

    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    const databaseFile = process.argv[2];

    readDatabase(databaseFile)
      .then((students) => {
        const names = students[major] || [];
        response.status(200).send(`List: ${names.join(', ')}`);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
