function solve(a,operator,b){
    let operations = {
        '+': function (a,b){return a+b;},
        '-': function (a,b){return a-b},
        '/':function(a,b){return a/b},
        '*': function (a,b){return a*b}
    }
    return operations[operator](a,b).toFixed(2);
}

console.log(solve(5,
    '+',
    10
))
console.log((solve(25.5,
    '-',
    3
)))