/*Creating function for task name: solve*/

function solve(data){
    let username = data[0];
    let password = username.split("").reverse().join("");
    for (let i = 1; i < data.length; i++) {
        if (data[i] === password){
            return `User ${username} logged in.`
        } else if(i === 4){
            return `User ${username} blocked!`
        }
        console.log("Incorrect password. Try again.")
    }


}

console.log(solve(['Acer','login','go','let me in','recA']))
console.log(solve(['momo','omom']))
console.log(solve(['sunny','rainy','cloudy','sunny','not sunny']))