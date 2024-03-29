function solve(fruitType, weightInGr, pricePerKg){
    return `I need $${(weightInGr / 1000 * pricePerKg).toFixed(2)} to buy ${(weightInGr / 1000).toFixed(2)} kilograms ${fruitType}.`;
}

console.log(solve('apple', 1563, 2.35))