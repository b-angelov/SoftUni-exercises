/*Creating function for task name: solve*/

function solve(...params) {
    const obj = {"name": params[0], "lastName": params[1], "hairColor": params[2]}
    return JSON.stringify(obj)
}

console.log(solve('George', 'Jones', 'Brown'))