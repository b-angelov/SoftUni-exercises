/*Creating function for task name: solve*/

function solve(nameList) {
    const phoneBook = {}
    nameList.forEach(element => {
        const [name, number] = element.split(" ");
        phoneBook[name] = number;
    })
    Object.entries(phoneBook).forEach(element => console.log(`${element[0]} -> ${element[1]}`))
}

console.log(solve(['Tim 0834212554',
    'Peter 0877547887',
    'Bill 0896543112',
    'Tim 0876566344']
))
