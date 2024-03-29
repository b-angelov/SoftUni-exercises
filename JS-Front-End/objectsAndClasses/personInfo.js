/*Creating function for task name: solve*/

function solve(...params) {
    let obj = {
        firstName: params[0],
        lastName: params[1],
        age: params[2],
    }
    return obj
}

console.log(solve("Peter",
    "Pan",
    "20"
))
console.log(solve("George",
    "Smith",
    "18"
))