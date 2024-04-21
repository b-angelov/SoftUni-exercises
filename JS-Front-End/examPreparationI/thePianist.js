/*Creating function for task name: solve*/

function solve(data) {
    const pieces = data.slice(1,Number(data[0])+1).reduce((prev,el)=>{
            const [piece,composer,key] = el.split("|")
            prev[piece] = {composer,key}
            return prev
    },{})
    const commands = data.slice(Number(data[0])+1,data.indexOf("Stop")).reduce((prev,el)=>{
        const [command,...options] = el.split("|")
        prev.push({command,options})
        return prev
    },[])

    const actions = {
        Add:(piece,composer,key)=>{
            if (!pieces.hasOwnProperty(piece)){
                console.log(`${piece} by ${composer} in ${key} added to the collection!`)
                pieces[piece] = {composer,key}
                return
            }
            console.log(`${piece} is already in the collection!`)
        },
        Remove:piece=>{
            if(pieces.hasOwnProperty(piece)){
                delete pieces[piece]
                console.log(`Successfully removed ${piece}!`)
                return
            }
            console.log(`Invalid operation! ${piece} does not exist in the collection.`)
        },
        ChangeKey:(piece,newKey)=>{
            if(pieces.hasOwnProperty(piece)){
                console.log(`Changed the key of ${piece} to ${newKey}!`)
                pieces[piece].key = newKey
                return
            }
            console.log(`Invalid operation! ${piece} does not exist in the collection.`)
        }
    }

    commands.forEach(({command,options})=>{
        actions[command](...options)
    })

    Object.entries(pieces).forEach(([piece,{composer,key}])=>{
        console.log(`${piece} -> Composer: ${composer}, Key: ${key}`)
    })
}

solve([
        '3',
        'Fur Elise|Beethoven|A Minor',
        'Moonlight Sonata|Beethoven|C# Minor',
        'Clair de Lune|Debussy|C# Minor',
        'Add|Sonata No.2|Chopin|B Minor',
        'Add|Hungarian Rhapsody No.2|Liszt|C# Minor',
        'Add|Fur Elise|Beethoven|C# Minor',
        'Remove|Clair de Lune',
        'ChangeKey|Moonlight Sonata|C# Major',
        'Stop'
    ]
)

solve([
        '4',
        'Eine kleine Nachtmusik|Mozart|G Major',
        'La Campanella|Liszt|G# Minor',
        'The Marriage of Figaro|Mozart|G Major',
        'Hungarian Dance No.5|Brahms|G Minor',
        'Add|Spring|Vivaldi|E Major',
        'Remove|The Marriage of Figaro',
        'Remove|Turkish March',
        'ChangeKey|Spring|C Major',
        'Add|Nocturne|Chopin|C# Minor',
        'Stop'
    ]
)