export default function updateStudentGradeByCity(students, city, newGrades) {
  const filteredStudents = students.filter(
    student => student.location === city
  );

  return filteredStudents.map(student => {
    const gradeObj = newGrades.find(
      g => g.studentId === student.id
    );

    let grade = "N/A";

    if (gradeObj) {
      grade = gradeObj.grade;
    }

    return {
      id: student.id,
      firstName: student.firstName,
      location: student.location,
      grade: grade
    };
  });
}
