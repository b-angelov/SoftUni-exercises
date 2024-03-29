function solve(a,b){
    let total = 0;
    let numbers = '';
    for (i = a; i <= b; i++){
        numbers += `${i} `;
        total += i;
    }
    return `${numbers.trimEnd()}\nSum: ${total}`;
}

console.log(solve(5,10))