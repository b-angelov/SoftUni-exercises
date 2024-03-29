/*Creating function for task name: solve*/

function solve(password) {
    const validations = {
        "length":password => password.match(/^.{6,10}$/)?false:"Password must be between 6 and 10 characters",
        "alnum":password => password.match(/^[A-Za-z0-9]*$/)?false:"Password must consist only of letters and digits",
        "twoDigits":function(password) {
            let res = password.match(/\d/g);
            return res && res.length >= 2?false:"Password must have at least 2 digits"
        }
    }
    let failures = [];
    for (let validation in validations){
        let result = validations[validation](password)
        if (result) failures.push(result)
    }
    if (failures.length) return failures.join("\n")
    return "Password is valid"
}

console.log(solve('logIn',"\n"))
console.log(solve('MyPass123',"\n"))
console.log(solve('Pa$s$s'))