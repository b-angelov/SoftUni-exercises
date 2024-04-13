/*Creating function for task name: Wild West Adventure */

function wildWestAdventure(data) {


    class Hero{
        #hp = 0;
        constructor(name,hp,bullets){
            this.name = name;
            this.hp = hp;
            this.bullets = Number(bullets);
        }

        get hp(){
            return this.#hp
        }
        set hp(value){
            this.#hp = value
            if (this.#hp > 100){
                this.#hp = 100
            }
        }

        FireShot(target){
            if(this.bullets > 0){
                this.bullets--
                console.log(`${this.name} has successfully hit ${target} and now has ${this.bullets} bullets!`)
            }else{
                console.log(`${this.name} doesn't have enough bullets to shoot at ${target}!`)
            }
        }
        TakeHit(damage,attacker){
            this.hp -= damage
            if(this.hp > 0){
                console.log(`${this.name} took a hit for ${damage} HP from ${attacker} and now has ${this.hp} HP!`)
            }else{
                delete heroes[this.name]
                console.log(`${this.name} was gunned down by ${attacker}!`)
            }
        }
        Reload(){
            if (this.bullets < 6){
                console.log(`${this.name} reloaded ${6 - this.bullets} bullets!`)
                this.bullets = 6
            }else{
                console.log(` ${this.name}'s pistol is fully loaded!`)
            }
        }
        PatchUp(amount){
            if (this.hp >= 100){
                console.log(` ${this.name} is in full health!`)
            }else{
                const currHp = this.hp
                this.hp += Number(amount)
                console.log(` ${this.name} patched up and recovered ${(this.hp - currHp)} HP!`)
            }
        }

    }

    const heroes = data.slice(1,1+Number(data[0])).reduce((prev,hero)=>{
        const [name,hp,bullets] = hero.split(" ")
        return {...prev,[name]:new Hero(name, hp, bullets)}
    },{})

    const commands = data.slice(1+Number(data[0]),data.indexOf("Ride Off Into Sunset" ))

    commands.forEach(command=>{
        const [com,name,...rest] = command.split(" - ")
        heroes[name][com](...rest)
    })

    Object.entries(heroes).forEach(([hero,data])=>{
        console.log(hero)
        console.log(` HP: ${data.hp}`)
        console.log(` Bullets: ${data.bullets}`)
    })

}

wildWestAdventure(["2",
    "Gus 100 0",
    "Walt 100 6",
    "FireShot - Gus - Bandit",
    "TakeHit - Gus - 100 - Bandit",
    "Reload - Walt",
    "Ride Off Into Sunset"])

wildWestAdventure(["2",
    "Jesse 100 4",
    "Walt 100 5",
    "FireShot - Jesse - Bandit",
    "TakeHit - Walt - 30 - Bandit",
    "PatchUp - Walt - 20" ,
    "Reload - Jesse",
    "Ride Off Into Sunset"])

wildWestAdventure(["2",
    "Gus 100 4",
    "Walt 100 5",
    "FireShot - Gus - Bandit",
    "TakeHit - Walt - 100 - Bandit",
    "Reload - Gus",
    "Ride Off Into Sunset"])


