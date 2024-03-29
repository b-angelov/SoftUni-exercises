function solve(lostFights, helmetPrice, swordPrice, shieldPrice, armorPrice){
    let expenses = 0;
    let shieldBreaks = 0;
    for (let i = 1; i <= lostFights; i++){
        if (!(i % 2)){
            expenses += helmetPrice;
            if (!(i % 3)) {
                expenses += shieldPrice;
                shieldBreaks += 1;
                if (!(shieldBreaks % 2)){
                    expenses += armorPrice;
                }
            }
        }
        if (!(i % 3)){
            expenses += swordPrice;
        }

    }
    return `Gladiator expenses: ${expenses.toFixed(2)} aureus`
}

console.log(solve(23,
    12.50,
    21.50,
    40,
    200

))