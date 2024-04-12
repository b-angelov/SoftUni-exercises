/*Creating function for task name: Horse Ricing*/

function horseRicing(data) {
    const horseList = data[0].split("|")
    const commands = data.slice(1,data.indexOf("Finish"))

    const actions = {
        Retake(overtaking,overtaken){
            const [otkng,otkn] = [horseList.indexOf(overtaking),horseList.indexOf(overtaken)]
            if(otkng < otkn){
                [horseList[otkng],horseList[otkn]] = [horseList[otkn],horseList[otkng]]
                console.log(`${overtaking} retakes ${overtaken}.`)
            }
        },
        Trouble(horse){
            const idx = horseList.indexOf(horse)
            if(idx > 0){
                horseList.splice(idx,1)
                horseList.splice(idx-1,0,horse)
                console.log(`Trouble for ${horse} - drops one position.`)
            }
        },
        Rage(horse){
            const idx = horseList.indexOf(horse)
            horseList.splice(idx,1)
            horseList.splice(idx+2,0,horse)
            console.log(`${horse} rages 2 positions ahead.`)
        },
        Miracle(){
            console.log(`What a miracle - ${horseList[0]} becomes first.`)
            horseList.push(horseList.shift())
        }
    }

    for (let command of commands){
        const [cmd,...rest] = command.split(" ")
        actions[cmd](...rest)
    }
    console.log(horseList.join("->"))
    console.log(`The winner is: ${horseList.pop()}`)
}

horseRicing(['Bella|Alexia|Sugar',
    'Retake Alexia Sugar',
    'Rage Bella',
    'Trouble Bella',
    'Finish'])

horseRicing(['Onyx|Domino|Sugar|Fiona',
    'Trouble Onyx',
    'Retake Onyx Sugar',
    'Rage Domino',
    'Miracle',
    'Finish']
)

horseRicing(['Fancy|Lilly',
    'Retake Lilly Fancy',
    'Trouble Lilly',
    'Trouble Lilly',
    'Finish',
    'Rage Lilly'])
