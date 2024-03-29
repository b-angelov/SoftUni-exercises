/*Creating function for task name: solve*/

function solve(word,text) {
    text = ` ${text.toLowerCase()} `;
    if(text.includes(` ${word} `)){
        return word;
    }
    return `${word} not found!`
}

console.log(solve('javascript',
    'JavaScript is the best programming language'
))
console.log(solve('python',
    'JavaScript is the best programming language'
))