function solve(weekday,age){
    let dayType = {
        "Weekday": [12,18,12],
        "Weekend": [15,20,15],
        "Holiday": [5,12,10],
    }

    if (0 <= age && age <= 18){
        age = 0;
    } else if(18 < age && age <= 64){
        age = 1;
    }else if(64 < age && age <= 122){
        age = 2;
    }else{
        age = 3;
    }

    weekday = dayType[weekday];

    if (age !== 3){
        console.log(`${weekday[age]}\$`);
    }else{
        console.log("Error!")
    }

}

solve('Weekday',
    42
)

let n = 22
let text = n.toString()
text.length