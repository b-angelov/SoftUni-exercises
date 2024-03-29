/*Creating function for task name: solve*/

function solve(employees) {
    employees.forEach(element => console.log(`Name: ${element} -- Personal Number: ${element.length}`))
}

console.log(solve([
        'Silas Butler',
        'Adnaan Buckley',
        'Juan Peterson',
        'Brendan Villarreal'
    ]
))
console.log(solve([
        'Samuel Jackson',
        'Will Smith',
        'Bruce Willis',
        'Tom Holland'
    ])
)