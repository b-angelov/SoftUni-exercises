/*Creating function for task name: solve*/

function solve(product, quantity) {
    const values = {"coffee": 1.50, "water": 1.00, "coke": 1.40, "snacks": 2.00};
    return (values[product] * quantity).toFixed(2);
}

console.log(solve("water", 5))
console.log(solve("coffee", 2))