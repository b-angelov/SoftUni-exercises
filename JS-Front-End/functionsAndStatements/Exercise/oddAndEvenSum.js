/*Creating function for task name: solve*/

function solve(number) {
    number = number.toString().split("")
    let [odd,even] = [0,0]
    number.forEach(n=>Number(n) % 2? odd += Number(n): even += Number(n))
    return `Odd sum = ${odd}, Even sum = ${even}`
}

console.log(solve(1000435))
console.log(solve(3495892137259234))