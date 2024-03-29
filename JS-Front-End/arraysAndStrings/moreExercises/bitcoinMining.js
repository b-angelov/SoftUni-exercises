/*Creating function for task name: solve*/

function solve(days) {
    let [oneG, oneB] = [67.51 ,11949.16 ]
    let [dayOfFirstBough, totalEarn, boughtB] = [0,0,0]
    for (let i = 0; i < days.length; i++){
        let day = days[i];
        if (!((i + 1) % 3)){
            day *= 0.7;
        }
        totalEarn += day * oneG;
        while (totalEarn >= oneB){
            totalEarn -= oneB;
            boughtB++;
            if (!dayOfFirstBough) dayOfFirstBough = i + 1;
        }
    }
    console.log(`Bought bitcoins: ${boughtB}`)
    if (dayOfFirstBough) console.log(`Day of the first purchased bitcoin: ${dayOfFirstBough}`)
    console.log(`Left money: ${totalEarn.toFixed(2)} lv.`)
}

solve([100, 200, 300])
solve([50, 100])
solve([3124.15, 504.212, 2511.124])