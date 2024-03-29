/*Creating function for task name: solve*/

function solve(heroes) {

    heroes.forEach((element, idx) => {
        let [name, level, items] = element.split(" / ")
        level = Number(level)
        heroes[idx] = {"Hero": name, "level": level, "items": items}
    })

    Object.entries(heroes)
        .sort(([idxa, a], [idxb, b]) => a.level - b.level)
        .forEach(([idx, obj]) => {
            console.log(`Hero: ${obj.Hero}\nlevel => ${obj.level}\nitems => ${obj.items}`)
        })

}

console.log(solve([
        'Isacc / 25 / Apple, GravityGun',
        'Derek / 12 / BarrelVest, DestructionSword',
        'Hes / 1 / Desolator, Sentinel, Antara'
    ]
))
console.log(solve([
        'Batman / 2 / Banana, Gun',
        'Superman / 18 / Sword',
        'Poppy / 28 / Sentinel, Antara'
    ])
)