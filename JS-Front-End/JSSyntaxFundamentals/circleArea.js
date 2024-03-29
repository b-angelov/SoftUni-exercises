function solve(num){
    if (typeof num == "number"){
        return (Math.PI * (num ** 2)).toFixed(2);
    } else{
        return `We can not calculate the circle area, because we receive a ${typeof num}.`;
    }
}

console.log(solve('name'))