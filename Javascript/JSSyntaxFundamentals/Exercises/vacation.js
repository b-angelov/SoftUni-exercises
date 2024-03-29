function solve(groupCount, groupType, weekDay){
    let values ={"Students":{"Friday":8.45,"Saturday":9.80,"Sunday":10.46},"Business":{"Friday":10.90,"Saturday":15.60,"Sunday":16},"Regular":{"Friday":15,"Saturday":20,"Sunday":22.50}};
    let totalPrice = values[groupType][weekDay] * groupCount;
    let discounts = {
        "Students": function(){if(groupCount >= 30) totalPrice *= 0.85;},
        "Business": function(){if(groupCount >= 100) totalPrice -= 10 * values[groupType][weekDay]},
        "Regular": function(){if (groupCount >= 10 && groupCount <= 20) totalPrice *= 0.95}
    }
    discounts[groupType]();
    return `Total price: ${totalPrice.toFixed(2)}`;
}

console.log(solve(40,
    "Regular",
    "Saturday"

))

