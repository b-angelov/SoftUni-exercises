/*Creating function for task name: solve*/

function solve(data) {
    let leaders = {}
    const actions = {
        arrives: leader => {
            leaders[leader.trim()] = {}
        },
        ":": (leader, data) => {
            const [aName, aCount] = data.split(", ")
            if (leaders.hasOwnProperty(leader)) leaders[leader][aName.trim()] = Number(aCount)
        },
        "+": (aName, aCount) => {
            aName = aName.trim()
            Object.entries(leaders).forEach(([leader, obj]) => {
                if (obj.hasOwnProperty(aName)) obj[aName] += Number(aCount)
            })
        },
        defeated: (leader) => delete leaders[leader]
    }
    data.forEach(command => {
        let a = ["arrives", "defeated"]
        a.forEach(c => {
            if (command.includes(c)) actions[c](...command.split(` ${c}`))
        })
        a = ["+", ":"]
        a.forEach(c => {
            if (command.includes(c)) actions[c](...command.split(c))
        })

    })
    Object.entries(leaders).sort(([name, obj],[name2,obj2]) => {
        return Object.values(obj2).reduce((a, b) => a + b,0) - Object.values(obj).reduce((a, b) => a + b,0)
    })
        .forEach(([leader, data]) => {
            const sum = Object.values(data).reduce((a, b) => a + b,0)
            console.log(`${leader}: ${sum}`)
            Object.entries(data)
                .sort(([a,b],[a1,b1])=>b1-b)
                .forEach(([name, count]) => console.log(`>>> ${name} - ${count}`))
        })
}

console.log(solve(['Rick Burr arrives', 'Fergus: Wexamp, 30245', 'Rick Burr: Juard, 50000', 'Findlay arrives', 'Findlay: Britox, 34540', 'Wexamp + 6000', 'Juard + 1350', 'Britox + 4500', 'Porter arrives', 'Porter: Legion, 55000', 'Legion + 302', 'Rick Burr defeated', 'Porter: Retix, 3205']))
console.log(solve(['Rick Burr arrives', 'Findlay arrives', 'Rick Burr: Juard, 1500', 'Wexamp arrives', 'Findlay: Wexamp, 34540', 'Wexamp + 340', 'Wexamp: Britox, 1155', 'Wexamp: Juard, 43423']))