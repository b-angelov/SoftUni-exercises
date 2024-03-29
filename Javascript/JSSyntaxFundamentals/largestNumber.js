function solve(...numbers){
    let max = -Infinity;
    numbers.forEach(function(number){number > max ? max = number : undefined;})
    console.log(`The largest number is ${max}.`)
}

solve(5, -3, 16)