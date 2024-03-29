/*Creating function for task name: solve*/

function solve(meetings) {
    const meetBook = {}
    meetings.forEach(element => {
        [day,name] = element.split(" ")
        !meetBook[day]?console.log(`Scheduled for ${day}`):console.log(`Conflict on ${day}!`)
        if(!meetBook[day])meetBook[day] = name
    })
    Object.entries(meetBook).forEach(element => console.log(`${element[0]} -> ${element[1]}`))
}

console.log(solve(['Monday Peter',
    'Wednesday Bill',
    'Monday Tim',
    'Friday Tim']
))