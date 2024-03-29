/*Creating function for task name: solve*/

function solve(first,second) {
    [first,second] = [first.charCodeAt(0),second.charCodeAt(0)].sort((a,b)=>a-b)
    let result = "";
    for (let i = first+1; i < second; i++) {
        result = result.concat(String.fromCharCode(i)," ")
    }
    return result;
}

console.log(solve('a',
    'd'
))
console.log(solve('#',
    ':'

))
console.log(solve('C',
    '#'

))