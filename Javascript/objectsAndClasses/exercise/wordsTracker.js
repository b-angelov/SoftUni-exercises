/*Creating function for task name: solve*/

function solve(words) {
    const searches = words[0].split(" ").reduce((word,name) => ({...word, [name]:0}),{})
    words.slice(1).forEach(word => {
        searches.hasOwnProperty(word)?searches[word]+=1:null
    })
    Object.entries(searches)
        .sort(([idx,a],[idxb,b])=>b-a)
        .forEach(([word,occurrences])=>console.log(`${word} - ${occurrences}`))
}

console.log(solve([
        'this sentence',
        'In', 'this', 'sentence', 'you', 'have', 'to', 'count', 'the', 'occurrences', 'of', 'the', 'words', 'this', 'and', 'sentence', 'because', 'this', 'is', 'your', 'task'
    ]
))
console.log(solve([
    'is the',
    'first', 'sentence', 'Here', 'is', 'another', 'the', 'And', 'finally', 'the', 'the', 'sentence']
))