/*Creating function for task name: solve*/

function solve(...values) {
    return values.slice(0,2).reduce((a,b) => a+b) - values[2]
}

console.log(solve(23,
    6,
    10
))
console.log(solve(1,
    17,
    30
))
console.log(solve(42,
    58,
    100
))