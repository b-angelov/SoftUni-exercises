/*Creating function for task name: solve*/

function solve(products) {
    const productsList = {}
    products.sort((a,b)=>a.localeCompare(b)).forEach(element=>{
            const [name,quantity] = element.split(" : ");
            if(!productsList.hasOwnProperty(name[0])) productsList[name[0]] = []
            productsList[name[0]].push({[name]:quantity})
        })

    Object.entries(productsList).forEach(([key,val])=> {
        console.log(key)
        val.forEach((element)=> {
            el = Object.entries(element)
            console.log(`  ${el[0][0]}: ${el[0][1]}`)
        })
    })
}

console.log(solve([
        'Appricot : 20.4',
        'Fridge : 1500',
        'TV : 1499',
        'Deodorant : 10',
        'Boiler : 300',
        'Apple : 1.25',
        'Anti-Bug Spray : 15',
        'T-Shirt : 10'
    ]
))

console.log(solve([
        'Omlet : 5.4',
        'Shirt : 15',
        'Cake : 59'
    ]
))