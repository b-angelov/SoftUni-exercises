function solve(n){
    let sum = 0;
    let np = n % 10;
    let equal = true;
    while (n){
        let nx = n % 10;
        if (nx !== np) equal = false;
        np = nx;
        sum += n % 10;
        n = Math.trunc(n / 10);
    }
    console.log(equal)
    console.log(sum)
}

solve(2222222)
solve(1234)