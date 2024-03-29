function solve(array,n){
    for (let i = 0; i < n; i++){
        let value = array.shift();
        array.push(value);
    }
    return array.join(' ');
}

console.log(solve([51, 47, 32, 61, 21], 2))
console.log(solve([32, 21, 61, 1], 4))
console.log(solve([2, 4, 15, 31], 5))
