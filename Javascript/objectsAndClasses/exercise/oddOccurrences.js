/*Creating function for task name: solve*/

function solve(words) {
    words = words.toLowerCase()
    words = words.split(" ")
    words = words.reduce((prev,word)=>({...prev,[word]:prev.hasOwnProperty(word)?prev[word]+1:1}),{})
    let res = ""
    Object.entries(words)
        .filter(([key,val])=>val%2)
        .sort(([k1,v1],[k2,v2])=>v2-v1)
        .forEach(([key,val])=> {
            res = res.concat(" ",key)
        })
    return res
}

console.log(solve('Java C# Php PHP Java PhP 3 C# 3 1 5 C#'))
console.log(solve('Cake IS SWEET is Soft CAKE sweet Food'))