/*Creating function for task name: solve*/

function solve(n) {
    let matrix = []
    for (let i = 0; i < n; i++) {
        let row = []
        for (let j = 0; j < n; j++) {
            row.push(n)
        }
        matrix.push(row)
    }
    matrix.forEach(element => console.log(element.join(" ")))
}

console.log(solve(3))
console.log(solve(7))
console.log(solve(2))