class HolbertonCourse {
    constructor(name, length, students) {
        this.name = name;
        this.length = length;
        this.students = students;
    }

    get name() {
        return this._name;
    }

    get length() {
        return this._length;
    }

    get students() {
        return this._students;
    }

    set name(nom) {
        if (typeof nom !== "string") {
            throw new Error("Name must be a string");
        }
        this._name = nom;
    }

    set length(length) {
        if (typeof length !== "number") {
            throw new Error("Length must be a number");
        }
        this._length = length;
    }

    set students(students) {
        if (!Array.isArray(students) || !students.every(s => typeof s === "string")) {
            throw new Error("students must be an array of strings");
        }
        this._students = students;
    }
}

export default HolbertonCourse;
