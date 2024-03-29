/*Creating function for task name: solve*/

function solve(a,b) {
    function factorial(num){
        if (num === 1) return num
        num = num * factorial(num-1)
        return num
    }
    return (factorial(a) / factorial(b)).toFixed(2)
}

console.log(solve(5,2))
console.log(solve(6,2))