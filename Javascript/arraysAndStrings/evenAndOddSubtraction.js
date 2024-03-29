function solve(numArr){
    let [even,odd] = [0,0];
    for (let n of numArr){
        if (!(n % 2)){
            even += n;
        } else{
            odd += n;
        }
    }
    return even - odd
}

console.log(solve([2,4,6,8,10]))