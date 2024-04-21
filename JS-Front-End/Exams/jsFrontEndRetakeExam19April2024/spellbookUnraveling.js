/*Creating function for task name: solve*/

function solve(data) {
    let spell = data[0]
    const commands = data.slice(1,data.indexOf("End"))

    const actions = {
        RemoveEven(){
           let newSpell = ""
            for (let i = 0; i <spell.length; i+=2) {
                newSpell += spell[i]
            }
            spell = newSpell
            console.log(spell)
        },
        TakePart(x,y){
            spell = spell.slice(x,y)
            console.log(spell)
        },
        Reverse(portion){
            if(spell.indexOf(portion) === -1){
                console.log("Error")
                return
            }
            const newPortion = portion.split("").reverse().join("")
            spell = spell.replace(portion,"") + newPortion
            console.log(spell)
        },
    }

    commands.forEach(el=>{
        const [command,...options] = el.split("!")
        actions[command](...options)
    })
    console.log(`The concealed spell is: ${spell}`)

}

solve(["asAsl2adkda2mdaczsa",
    "RemoveEven",
    "TakePart!1!9",
    "Reverse!maz",
    "End"])


solve(["hZwemtroiui5tfone1haGnanbvcaploL2u2a2n2i2m",
    "TakePart!31!42",
    "RemoveEven",
    "Reverse!anim",
    "Reverse!sad",
    "End"])
