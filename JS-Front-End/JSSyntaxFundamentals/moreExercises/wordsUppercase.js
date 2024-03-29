function solve(text){
    let exp = /\w+/gm
    let words = text.match(exp);
    words.forEach(function(element,index){words[index] = words[index].toUpperCase();})
    console.log(words.join(', '))
}

solve('Hi, how are you?')