/*Creating function for task name: solve*/
function solve(data) {
    data.map(element=>JSON.parse(element).sort((a,b)=>Number(b)-Number(a)).toString())
        .reduce((prev,element)=>{
            if (!prev.includes(element)){
                prev.push(element)
            }
            return prev
        },[])
        .map(element=>JSON.parse(`[${element}]`))
        .sort((a,b)=>a.length-b.length)
        .forEach(element=>console.log(`[${element.join(', ')}]`))
}

solve(["[-3, -2, -1, 0, 1, 2, 3, 4]",
    "[10, 1, -17, 0, 2, 13]",
    "[4, -3, 3, -2, 2, -1, 1, 0]"]
)
solve(["[7.14, 7.180, 7.339, 80.099]",
    "[7.339, 80.0990, 7.140000, 7.18]",
    "[7.339, 7.180, 7.14, 80.099]",
    "[9,0,-2,4,5,9,10]",
    "[9,-2,0,4,9,8]",
]
)

solve(["[   0,51]","[0,5,22]","[1.00,2.02511,22.02214]","[]"])
solve(["[1,2,1,2,1,3,1,2]"])