/*Creating function for task name: solve*/

function solve(size) {
    let sequence = "ATCGTTAGGG";
    for (
        let i = 0, dash = 0, star = 2, char = 0;
        i < size;
        i++, star = star !== -1 ?(star - 1):2, char = (char + 2) % sequence.length, dash = 6 - (Math.abs(star) * 2 + 2)
    ) {
        let currentStar = Math.abs(star)
        let [a,b] = [sequence[char], sequence[char+1]]
        // console.log(i, dash, currentStar, char, a , b)
        console.log(`${'*'.repeat(currentStar)}${a}${'-'.repeat(dash)}${b}${'*'.repeat(currentStar)}`)
    }
}

console.log(solve(30))