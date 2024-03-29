/*Creating function for task name: solve*/

function solve(doings) {
    class Cat {
        constructor(name, age) {
            this.name = name
            this.age = age
        }

        meow() {
            console.log(`${this.name}, age ${this.age} says Meow`)
        }
    }

    doings.forEach(element => {
        let [name, age] = element.split(" ")
        const cat = new Cat(name, age)
        cat.meow()

    })
}

console.log(solve(['Mellow 2', 'Tom 5']))
console.log(solve(['Candy 1', 'Poppy 3', 'Nyx 2']))