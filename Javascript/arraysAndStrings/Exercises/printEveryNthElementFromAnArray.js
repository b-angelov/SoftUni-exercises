/*Creating function for task name: solve*/

function solve(array,n) {
    return array.filter((word,idx) => !(idx % n));
}

console.log(solve(['1',
        '2',
        '3',
        '4',
        '5'],
    6


))