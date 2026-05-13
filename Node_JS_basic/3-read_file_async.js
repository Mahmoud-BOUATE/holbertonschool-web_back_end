const fs = require('fs')

function countStudents(path) {
    return new Promise((resolve, reject) => {
        fs.readFile(path, 'utf8', (err, data) => {
            if (err) {
                reject(new Error('Cannot load the database'))
                return
            }

            const lines = data
                .split('\n')
                .filter(line => line.trim() !== '')

            const students = {}

            for (let i = 1; i < lines.length; i += 1) {
                const [firstname, , , field] = lines[i].split(',')

                if (!students[field]) {
                    students[field] = []
                }

                students[field].push(firstname)
            }

            const total = Object.values(students)
                .reduce((sum, arr) => sum + arr.length, 0)

            console.log(`Number of students: ${total}`)

            for (const field in students) {
                if (Object.prototype.hasOwnProperty.call(students, field)) {
                    console.log(
                        `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}`
                    )
                }
            }

            resolve()
        })
    })
}

module.exports = countStudents
