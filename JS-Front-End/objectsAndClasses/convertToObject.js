/*Creating function for task name: solve*/

function solve(JSONString) {
    return Object.entries(JSON.parse(JSONString)).forEach(element => console.log(`${element[0]}: ${element[1]}`))
}

console.log(solve('{"name": "George", "age": 40, "town": "Sofia"}'))