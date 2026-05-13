const http = require('http')
const countStudents = require('./3-read_file_async')

const app = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' })

    if (req.url === '/') {
        res.end('Hello Holberton School!')
    } else if (req.url === '/students') {
        const database = process.argv[2]

        res.write('This is the list of our students\n')

        countStudents(database)
            .then(() => {
                res.end()
            })
            .catch(() => {
                res.end('Cannot load the database')
            })
    } else {
        res.end('Not found')
    }
})

app.listen(1245)

module.exports = app
