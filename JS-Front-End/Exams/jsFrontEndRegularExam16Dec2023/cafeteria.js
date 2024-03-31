/*Creating function for task name: jsFrontEndRegularExam16Dec2023*/

function jsFrontEndRegularExam16Dec2023(input) {
    const baristasCount = Number(input[0])
    let baristaData = input.slice(1,1+baristasCount)
    const commands = input.slice(1+baristasCount,input.length-1)

    baristaData = baristaData.reduce((prev,barista)=>{
        let [name,shift,coffeeTypes] = barista.split(" ")
        coffeeTypes = coffeeTypes.split(",")
        prev[name] =  {
            shift: shift,
            coffee: coffeeTypes,
        }
        return prev
    },{})

    const actions = {
        "Prepare":(name,shift,coffeeType) =>{
            const barista  = baristaData[name]
            if(barista.shift === shift && barista["coffee"].includes(coffeeType)){
                console.log(`${name} has prepared a ${coffeeType} for you!`)
                return
            }
            console.log(`${name} is not available to prepare a ${coffeeType}.`)
        },
        "Change Shift":(name,shift) =>{
            baristaData[name].shift = shift
            console.log( `${name} has updated his shift to: ${shift}`)
        },
        "Learn":(name,coffeeType) =>{
            const barista = baristaData[name]
            if(barista.coffee.includes(coffeeType)){
                console.log(`${name} knows how to make ${coffeeType}.`)
                return
            }
            barista.coffee.push(coffeeType)
            console.log(`${name} has learned a new coffee type: ${coffeeType}.`)
        },

    }

    commands.forEach(command=>{
        const [action,...params] = command.split(" / ")
        actions[action](...params)
    })

    Object.entries(baristaData).forEach(([name,barista])=>{
        console.log(`Barista: ${name}, Shift: ${barista.shift}, Drinks: ${barista.coffee.join(", ")}`)
    })
}

jsFrontEndRegularExam16Dec2023([
    '3',
    'Alice day Espresso,Cappuccino',
    'Bob night Latte,Mocha',
    'Carol day Americano,Mocha',
    'Prepare / Alice / day / Espresso',
    'Change Shift / Bob / night',
    'Learn / Carol / Latte',
    'Learn / Bob / Latte',
    'Prepare / Bob / night / Latte',
    'Closed']
)