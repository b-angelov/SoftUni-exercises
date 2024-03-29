/*Creating function for task name: solve*/

function solve(text) {
    let pattern = /#([a-zA-Z]+)/gm;
    let words = [...text.matchAll(pattern)];
    let result = [];
    words = words.forEach((element) => result.push(element[1]));
    result.forEach((element)=>console.log(element))
}

solve('Nowadays everyone uses # to tag a #special word in #socialMedia')
solve('The symbol # is known #variously in English-speaking #regions as the #number sign')