function solve(words,text){
    words = words.split(",");
    for (let word of words){
        text = text.replace('*'.repeat(word.trim().length), word.trim());
    }
    return text;
}