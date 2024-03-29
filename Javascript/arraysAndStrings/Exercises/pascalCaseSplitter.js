/*Creating function for task name: solve*/

function solve(text) {
    let pattern = /[A-Z][^A-Z0-9\s]*/gm;
    return [...text.matchAll(pattern)].join(", ");
}

console.log(solve('SplitMeIfYouCanHaHaYouCantOrYouCan'))
console.log(solve('HoldTheDoor'))
console.log(solve('ThisIsSoAnnoyingToDo'))