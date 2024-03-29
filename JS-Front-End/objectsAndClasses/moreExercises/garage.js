/*Creating function for task name: solve*/

function solve(cars) {
    const garages = {}
    cars.forEach(car=>{
        const[garageNumber,carData] = car.split(" - ")
        if(!garages.hasOwnProperty(garageNumber)) garages[garageNumber] = []
        const obj = {}
        carData.split(", ").forEach(el=>{
            const [key,value] = el.split(": ")
            obj[key] = value
        })
        garages[garageNumber].push(obj)

    })
    Object.entries(garages).forEach(([garage,data])=>{
        console.log(`Garage № ${garage}`)
        data.forEach(car=>{
            car = Object.entries(car).map(([key,value],)=>`${key} - ${value}`)
            console.log(`--- ${car.join(", ")}`)
        })
    })
}

solve(['1 - color: blue, fuel type: diesel', '1 - color: red, manufacture: Audi', '2 - fuel type: petrol', '4 - color: dark blue, fuel type: diesel, manufacture: Fiat'])
solve(['1 - color: green, fuel type: petrol',
    '1 - color: dark red, manufacture: WV',
    '2 - fuel type: diesel',
    '3 - color: dark blue, fuel type: petrol']
)