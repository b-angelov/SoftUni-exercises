/*Creating function for task name: solve*/

function solve(JSONList) {
    const res = JSONList.reduce((prev,piece) => ({...prev,...JSON.parse(piece)}),{})
    Object.entries(res)
        .sort(([terma,a],[termb,b])=>terma.localeCompare(termb))
        .forEach(([term,desc])=>console.log(`Term: ${term} => Definition: ${desc}`))
}

console.log(solve([
        '{"Coffee":"A hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub."}',
        '{"Bus":"A large motor vehicle carrying passengers by road, typically one serving the public on a fixed route and for a fare."}',
        '{"Boiler":"A fuel-burning apparatus or container for heating water."}',
        '{"Tape":"A narrow strip of material, typically used to hold or fasten something."}',
        '{"Microphone":"An instrument for converting sound waves into electrical energy variations which may then be amplified, transmitted, or recorded."}'
    ]
))