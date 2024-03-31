/*Creating function for task name: Astro Adventure*/

function astroAdventure(data) {

    class Astronaut {
        #oxygenLevel = 0
        #energyReserves = 0
        #name

        constructor(name,oxygenLevel, energyReserves) {
            this.name = name
            this.oxygenLevel = oxygenLevel
            this.energyReserves = energyReserves
        }

        Explore(energyNeeded){
            if (this.energyReserves - energyNeeded >= 0){
                this.energyReserves -= energyNeeded
                console.log(`${this.name} has successfully explored a new area and now has ${this.energyReserves} energy!`)
                return
            }
            console.log(`${this.name} does not have enough energy to explore!`)
        }

        Refuel(amount){
            const prevAmount = this.energyReserves
            this.energyReserves += amount
            console.log(`${this.name} refueled their energy by ${this.energyReserves - prevAmount}!`)
        }

        Breathe(amount){
            const prevAmount = this.oxygenLevel
            this.oxygenLevel += amount
            console.log(`${this.name} took a breath and recovered ${this.oxygenLevel - prevAmount} oxygen!`)
        }

        set oxygenLevel(value) {
            this.#oxygenLevel = value
            if (this.#oxygenLevel > 100) {
                this.#oxygenLevel = 100
            }
        }

        set energyReserves(value) {
            this.#energyReserves = value
            if (this.#energyReserves > 200) {
                this.#energyReserves = 200
            }
        }

        get oxygenLevel() {
            return this.#oxygenLevel
        }

        get energyReserves() {
            return this.#energyReserves
        }
    }

    let astronauts = data.slice(1, 1 + Number(data[0]))
    const commands = data.slice(1 + Number(data[0]), data.length - 1)

    astronauts = astronauts.reduce((prev, curr) => {
        const [name, ...rest] = curr.split(" ")
        const [oxygenLevel, energyReserves] = rest.map(Number)
        prev[name] = new Astronaut(name, oxygenLevel, energyReserves)
        return prev
    }, {})

    commands.forEach(command=>{
        const [action,...rest] = command.split(" - ")
        let [name,value] = rest
        value = Number(value)
        if(astronauts.hasOwnProperty(name)) {
            astronauts[name][action](value)
        }
    })

    Object.entries(astronauts).forEach(([name,astronaut])=>{
        console.log(`Astronaut: ${astronaut.name}, Oxygen: ${astronaut.oxygenLevel}, Energy: ${astronaut.energyReserves}`)
    })


}

astroAdventure(['3',
    'John 50 120',
    'Kate 80 180',
    'Rob 70 150',
    'Explore - John - 50',
    'Explore - Hannah - 50',
    'Refuel - Kate - 30',
    'Refuel - Kate - 180',
    'Breathe - Rob - 20',
    'Breathe - Rob - 120',
    'End']
)