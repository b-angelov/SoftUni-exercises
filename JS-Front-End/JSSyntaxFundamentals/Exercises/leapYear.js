function solve(year) {
    return (!(year % 4) && ((year % 100) || !(year % 400))) ? "yes" : "no";
}

console.log(solve(4));