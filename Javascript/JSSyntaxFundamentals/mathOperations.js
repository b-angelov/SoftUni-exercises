function solve(a,b,operator){
    let calc = {
        "+": function(a,b){return a + b;},
        "-": function(a,b){return a - b;},
        "*": function(a,b){return a * b;},
        "/": function(a,b){return a / b;},
        "%": function(a,b){return a % b;},
        "**": function(a,b){return a ** b;}
    }
    console.log(calc[operator](a,b))
}

solve(3, 5.5, '*')