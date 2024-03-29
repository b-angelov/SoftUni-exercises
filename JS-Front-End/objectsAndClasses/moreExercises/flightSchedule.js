/*Creating function for task name: solve*/

function solve(data) {
    const [flights,status,lookup] = data
    let flightList = {}

    const parser = arr => arr.split(/^(\w+\s)/g).slice(1)
    flights.map(element=>{
        const [key,value] = parser(element);
        return flightList[key] = {Destination:value}
    })
    status.forEach(element=>{
        const [key,value] = parser(element)
        if(flightList.hasOwnProperty(key))flightList[key]["Status"] = value
    })
    Object.entries(flightList).forEach((element,key)=>{
        const status = lookup[0]
        if (status === "Ready to fly" && !element[1].hasOwnProperty("Status")){
            console.log({...element[1],Status:"Ready to fly"})
        }else if(status !== "Ready to fly" && element[1].hasOwnProperty("Status")){
            console.log(element[1])
        }
    })
}

// console.log(solve([['WN269 Delaware',
//         'FL2269 Oregon',
//         'WN498 Las Vegas',
//         'WN3145 Ohio',
//         'WN612 Alabama',
//         'WN4010 New York',
//         'WN1173 California',
//         'DL2120 Texas',
//         'KL5744 Illinois',
//         'WN678 Pennsylvania'],
//         ['DL2120 Cancelled',
//             'WN612 Cancelled',
//             'WN1173 Cancelled',
//             'SK430 Cancelled'],
//         ['Cancelled']
//     ]
// ))

console.log(solve([['WN269 Delaware',
        'FL2269 Oregon',
        'WN498 Las Vegas',
        'WN3145 Ohio',
        'WN612 Alabama',
        'WN4010 New York',
        'WN1173 California',
        'DL2120 Texas',
        'KL5744 Illinois',
        'WN678 Pennsylvania'],
        ['DL2120 Cancelled',
            'WN612 Cancelled',
            'WN1173 Cancelled',
            'SK330 Cancelled'],
        ['Ready to fly']
    ]
))