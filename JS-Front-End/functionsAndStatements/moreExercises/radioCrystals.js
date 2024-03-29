/*Creating function for task name: solve*/

function solve(parameters) {
    let [desiredThickness, ...chunks] = parameters
    const operationsOrder = ["Cut", "Lap", "Grind", "Etch"]
    const operations = {
        "Cut": (chunk) => chunk / 4,
        "Lap": (chunk) => chunk * 0.8,
        "Grind": (chunk) => chunk - 20,
        "Etch": (chunk) => chunk - 2,
        "X-ray": (chunk) => chunk + 1,
        "Transporting and washing": (chunk) => Math.floor(chunk),

    }

    function processChunk(chunk) {

        const operationsDone = {}

        for (let op of operationsOrder) {
            const operation = operations[op]
            while (operation(chunk) >= desiredThickness) {
                chunk = operation(chunk)
                if (!operationsDone[op]) operationsDone[op] = 0
                operationsDone[op] += 1
                chunk = operations["Transporting and washing"](chunk)
            }
        }

        if (chunk > desiredThickness) {
            operationsDone["X-ray"] = 1
            chunk = operations["X-ray"](chunk)
            chunk = operations["Etch"](chunk)
            if (!operationsDone["Etch"]) operationsDone["Etch"] = 0
            operationsDone["Etch"] += 1
        }
        if(chunk + 1 === desiredThickness){
            operationsDone["X-ray"] = 1
            chunk = operations["X-ray"](chunk)
        }

        return [operationsDone,chunk]
    }

    for (let chunk of chunks) {
        let [done,finalSize] = processChunk(chunk)
        let xray = done["X-ray"]
        delete done["X-ray"]
        console.log(`Processing chunk ${chunk} microns`)
        Object.entries(done).forEach((value) => console.log(
            `${value[0]} x${value[1]}\nTransporting and washing`
            ))
        if(xray) console.log(`X-ray x${xray}`)
        console.log(`Finished crystal ${finalSize} microns`)

    }
}

console.log(solve([1375, 50000]))
// console.log(solve([1000, 4000, 8100]))
console.log(solve([1000, 999]))