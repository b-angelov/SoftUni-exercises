/*Creating function for task name: solve*/

function solve(a, b, operator) {
    const operators = {
        'multiply': (a, b) => a * b,
        'divide': (a, b) => a / b,
        'add': (a, b) => a + b,
        'subtract': (a, b) => a - b
    }
    return operators[operator](a, b);

}

console.log(solve(5,
    5,
    'multiply'
))
console.log(solve(40,
    8,
    'divide'
))
console.log(solve(12,
    19,
    'add'
))
console.log(solve(50,
    13,
    'subtract'
))