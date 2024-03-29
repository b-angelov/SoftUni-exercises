/*Creating function for task name: solve*/

function solve(commandList) {
    let value = 0
    const commands = {
        "soap": () => value += 10,
        "water": ()=> value *= 1.2,
        "vacuum cleaner": ()=> value *= 1.25,
        "mud": ()=> value *= 0.9,

    }
    commandList.forEach(value => commands[value]())
    return `The car is ${value.toFixed(2)}% clean.`
}

console.log(solve(['soap', 'soap', 'vacuum cleaner', 'mud', 'soap', 'water']))
console.log(solve(["soap", "water", "mud", "mud", "water", "mud", "vacuum cleaner"]))