function solve(n,numArr){
    return numArr.slice(0,n).reverse().join(" ");
}

console.log(solve(4, [-1, 20, 99, 5]))