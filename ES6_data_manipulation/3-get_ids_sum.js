export default function getStudentIdsSum(students){
    if (!Array.isArray(students)) return;
     return students.reduce((accumulateur, element) => accumulateur + element.id, 0);

    }

