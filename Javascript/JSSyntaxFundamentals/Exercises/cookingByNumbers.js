function solve(...arguments){
    let number = arguments[0];
    let mapper = {
        "chop":function(n){return n/2;},
        "dice":function(n){return n ** 0.5;},
        "spice":function(n){return n + 1},
        "bake":function(n){return n * 3},
        "fillet":function(n){return n - n * 0.2}
    }
    for(let i = 1; i < arguments.length; i++){
        number = mapper[arguments[i]](number);
        console.log(number);
    }
}

solve('9', 'dice', 'spice', 'chop', 'bake', 'fillet')