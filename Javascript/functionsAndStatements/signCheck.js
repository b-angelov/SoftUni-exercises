/*Creating function for task name: solve*/

function solve(a,b,c) {
    const isNegative = (value) => (value < 0) ? "Negative" : "Positive";
    const values = {
        "Positive,Positive,Positive": "Positive",
        "Negative,Positive,Positive":"Negative",
        "Positive,Negative,Positive":"Negative",
        "Positive,Positive,Negative":"Negative",
        "Negative,Negative,Negative":"Negative",
        "Positive,Negative,Negative":"Positive",
        "Negative,Positive,Negative":"Positive",
        "Negative,Negative,Positive":"Positive",
    }
    return values[[isNegative(a),isNegative(b),isNegative(c)].join(',')]
}

console.log(solve( 5,
    12,
    -15
))
console.log(solve(-6,
    -12,
    14
))
console.log(solve(-1,
    -2,
    -3
))