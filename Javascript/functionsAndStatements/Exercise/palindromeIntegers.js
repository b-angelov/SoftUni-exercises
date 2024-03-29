/*Creating function for task name: solve*/

function solve(integersArray) {
    function IsIntPalindrome(n){
        n = n.toString()
        return n === n.split("").reverse().join("");
    }
    integersArray.forEach(element => console.log(IsIntPalindrome(element)))
}

console.log(solve([123,323,421,121]))
console.log(solve([32,2,232,1010]))