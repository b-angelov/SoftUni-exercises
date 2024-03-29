function solve(speed, drivingArea){
    let areas = {"motorway":130,"interstate":90,"city":50,"residential":20}
    let status = "";
    if (speed <= areas[drivingArea]){
        return `Driving ${speed} km/h in a ${areas[drivingArea]} zone`;
    }
    let difference = speed - areas[drivingArea];
    if (difference <= 20) {
        status = "speeding";
    }else if (difference <= 40){
        status = "excessive speeding";
    }else{
        status = "reckless driving"
    }
    return `The speed is ${difference} km/h faster than the allowed speed of ${areas[drivingArea]} - ${status}`
}

console.log(solve(40, 'city'))
console.log(solve(21, 'residential'))
console.log(solve(120, 'interstate'))
console.log(solve(200, 'motorway'))