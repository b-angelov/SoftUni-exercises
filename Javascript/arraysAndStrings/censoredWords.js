function solve(text,word){
    while(text.includes(word)) {
        text = text.replace(word, "*".repeat(word.length));
    }
    return text
}

console.log(solve('A small sentence with some words of small ammount', 'small'));