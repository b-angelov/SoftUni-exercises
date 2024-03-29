function solve(input) {
    const result = new Set();
    for(let car of input){
        let [action,number] = car.split(", ");
        (action === "IN")?result.add(number):result.delete(number)
    }

    result.size?
        Array.from(result).sort((a,b)=>a.localeCompare(b))
            .forEach(element=>console.log(element))
        :console.log("Parking Lot is Empty")
}

console.log(solve(['IN, CA2844AA',
    'IN, CA1234TA',
    'OUT, CA2844AA',
    'IN, CA9999TT',
    'IN, CA2866HI',
    'OUT, CA1234TA',
    'IN, CA2844AA',
    'OUT, CA2866HI',
    'IN, CA9876HH',
    'IN, CA2822UU',
    "IN, sld;fklsdklf44545454654dfsf,sdklfl;sdk;sdf878798789797"]
))
console.log(solve(['IN, CA2844AA',
    'IN, CA1234TA',
    'OUT, CA2844AA',
    'OUT, CA1234TA',
    ]
))