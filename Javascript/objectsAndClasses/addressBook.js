/*Creating function for task name: solve*/

function solve(addresses) {
    let addressBook = {}
    addresses.forEach(element => {
        let [name,address] = element.split(":")
        addressBook[name] = address
    })
    addressBook = Object.entries(addressBook).sort((a,b)=>a[0].localeCompare(b[0]))
    addressBook.forEach(([name,address]) => console.log(`${name} -> ${address}`))
}

console.log(solve(['Bob:Huxley Rd',
    'John:Milwaukee Crossing',
    'Peter:Fordem Ave',
    'Bob:Redwing Ave',
    'George:Mesta Crossing',
    'Ted:Gateway Way',
    'Bill:Gateway Way',
    'John:Grover Rd',
    'Peter:Huxley Rd',
    'Jeff:Gateway Way',
    'Jeff:Huxley Rd']
))