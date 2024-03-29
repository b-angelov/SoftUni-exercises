/*Creating function for task name: sorting numbers*/

function sortingNumbers(array) {
    let result = [];
    let i = 0;
    array.sort((a,b)=>Number(a)-Number(b));
    while (array.length) {
        if ((i % 2)){
            result.push(array.pop())
        }
        else{
            result.push(array.shift())
        }
        i++;
    }
    return result
}

console.log(sortingNumbers([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]))