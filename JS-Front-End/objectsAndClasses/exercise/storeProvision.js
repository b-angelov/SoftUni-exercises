/*Creating function for task name: solve*/

function solve(provisionA,provisionB) {
    const provisions = {}
    extract(provisionA);
    extract(provisionB);
    Object.entries(provisions).forEach(([key,val]) => console.log(`${key} -> ${val}`))
    function extract (arr) {
        for (let n = 0,q = 1; n < arr.length; n+=2,q+=2) {
            const [name,quantity] = [arr[n],arr[q]]
            provisions.hasOwnProperty(name)? provisions[name] += Number(quantity): provisions[name] = Number(quantity);
        }
    }

}

console.log(solve([
        'Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'
    ],
    [
        'Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30'
    ]
))
console.log(solve([
        'Salt', '2', 'Fanta', '4', 'Apple', '14', 'Water', '4', 'Juice', '5'
    ],
    [
        'Sugar', '44', 'Oil', '12', 'Apple', '7', 'Tomatoes', '7', 'Bananas', '30'
    ])
)