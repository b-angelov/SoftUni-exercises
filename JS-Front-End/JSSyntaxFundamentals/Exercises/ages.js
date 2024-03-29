function solve(age){
    let ages = {"baby":[0,2],"child":[3,13],"teenager":[14,19],"adult":[20,65]};
    for (let i = 0; i < Object.keys(ages).length; i++){
        let value = Object.keys(ages)[i];
        let type = ages[value];
        if (type[0] <= age && age <= type[1]){
            return value;
        }
    }
    if (age >= 66) return "elder";
    return "out of bounds";
}

console.log(solve(-1))
