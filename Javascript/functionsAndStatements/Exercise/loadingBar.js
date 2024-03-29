/*Creating function for task name: solve*/

function solve(percentage) {
    percentage /= 10
    let bar = `[${"%".repeat(percentage)}${".".repeat(10 - percentage)}]`
    return percentage < 10 ? `${percentage * 10}% ${bar}\n Still loading...` : `100% Complete!\n${bar}`
}

console.log(solve(30))
console.log(solve(50))
console.log(solve(100))