function solve(initialYield){
    let day = 0;
    let totalYield = 0;
    const [consumption,reduction] = [26,10];
    while (initialYield >= 100){
        day += 1;
        totalYield += initialYield - consumption;
        initialYield -= reduction;
    }
    totalYield -= consumption;
    if (totalYield < 0) totalYield = 0;
    return `${day}\n${totalYield}`;
}

console.log(solve(450))