/*Creating function for task name: solve*/

function solve(obj) {
    Object.entries(obj).forEach(
        element => console.log(`${element[0]} -> ${element[1]}`)
    )
}

console.log(solve({
        name: "Sofia",
        area: 492,
        population: 1238438,
        country: "Bulgaria",
        postCode: "1000"
    }
))