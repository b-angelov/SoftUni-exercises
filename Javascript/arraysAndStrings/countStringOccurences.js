function solve(text,word){
    let tArr = text.split(' ');
    let count = 0;
    tArr.forEach((element) => {element === word?count += 1:0;});
    return count;
}

console.log(solve('This is a word and it also is a sentence',
    'is'


))