/*Creating function for task name: MotoGP Race*/

function motoGpRace(data) {

    class Racer{
        #fuelCapacity = 0
        #position = 0
        constructor(name,fuelCapacity,position) {
            this.position = position
            this.#fuelCapacity = fuelCapacity
            this.name = name
        }

        StopForFuel(...values){
            const [minimumFuel,changedPosition] = values.map(Number)
            if(minimumFuel > this.fuelCapacity){
                this.position = changedPosition
                this.fuelCapacity = 100
                console.log(`${this.name} stopped to refuel but lost his position, now he is ${changedPosition}.`)
                return
            }
            console.log(`${this.name} does not need to stop for fuel!`)
        }
        Overtaking(rider2){
            if(!racers[rider2]) return
            const rider1 = this
            rider2 = racers[rider2]
            const [idx1,idx2] = [Object.keys(racers).indexOf(rider1.name) , Object.keys(racers).indexOf(rider2.name)]
            if(rider1.position < rider2.position){
                [rider1.position,rider2.position] = [rider2.position,rider1.position]
                console.log(`${rider1.name} overtook ${rider2.name}!`)
            }
        }
        EngineFail(lapsLeft){
            console.log(`${this.name} is out of the race because of a technical issue, ${lapsLeft} laps before the finish.`)
            delete racers[this.name]
        }


        get fuelCapacity(){
            return this.#fuelCapacity
        }

        set fuelCapacity(value){
            this.#fuelCapacity = value
            if(this.#fuelCapacity > 100){
                this.#fuelCapacity = 100
            }
        }

    }

    let racers = data.slice(1,Number(data[0])+1)
    const commands = data.slice(Number(data[0])+1,data.length-1)

    racers = racers.reduce((prev,curr)=>{
        const [name,...rest] = curr.split("|")
        const [fuelCapacity,position] = rest.map(Number)
        prev[name] = new Racer(name,fuelCapacity,position)
        return prev
    },{})
    commands.forEach(command=>{
        let [action,rider,...rest] = command.split(" - ")
        if(racers.hasOwnProperty(rider)) {
            racers[rider][action](...rest)
        }
    })
    Object.entries(racers).forEach(([name,racer])=>{
        console.log(`${racer.name}
    Final position: ${racer.position}`
    )
    })
}

// motoGpRace(["3",
//     "Valentino Rossi|100|1",
//     "Marc Marquez|90|2",
//     "Jorge Lorenzo|80|3",
//     "StopForFuel - Valentino Rossi - 50 - 1",
//     "Overtaking - Marc Marquez - Jorge Lorenzo",
//     "EngineFail - Marc Marquez - 10",
//     "Finish"]
// )

motoGpRace((["4",
    "Valentino Rossi|100|1",
    "Marc Marquez|90|3",
    "Jorge Lorenzo|80|4",
    "Johann Zarco|80|2",
    "StopForFuel - Johann Zarco - 90 - 5",
    "Overtaking - Marc Marquez - Jorge Lorenzo",
    "Overtaking - Marc Marquez - Valentino Rossi",
    "EngineFail - Marc Marquez - 10",
    "Finish"])
)