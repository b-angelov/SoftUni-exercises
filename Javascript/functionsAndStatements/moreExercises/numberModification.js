/*Creating function for task name: solve*/

function solve(number) {
    number = number.toString().split('')
    while ((number.reduce((a,b)=>Number(a)+Number(b)) / number.length) <= 5){
        number.push(9)
    }
    return number.join("")
}

console.log(solve(101))
console.log(solve(5835))