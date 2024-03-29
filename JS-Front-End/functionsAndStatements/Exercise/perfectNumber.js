/*Creating function for task name: solve*/

function solve(number) {
    const divisors = []
    let currentDivisor = Math.trunc(number / 2)
    while (currentDivisor){
        if(number / currentDivisor === Math.trunc(number / currentDivisor)){
            divisors.push(currentDivisor)
        }
        currentDivisor--
    }

    const sum =  divisors.reduce((a,b) => a+b)
    return sum === number?"We have a perfect number!":"It's not so perfect."

}

console.log(solve(6))
console.log(solve(28))
console.log(solve(1236498))