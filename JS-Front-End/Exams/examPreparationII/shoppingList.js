/*Creating function for task name: solve*/

function solve(data) {
    const items = data[0].split("!")
    const commands = data.slice(1,data.indexOf("Go Shopping!"))

    const actions = {
        Urgent(item){
            if(!items.includes(item))items.unshift(item)
        },
        Unnecessary(item){
            if(items.includes(item))items.splice(items.indexOf(item),1)
        },
        Correct(item,newItem){
            if(items.includes(item))items[items.indexOf(item)] = newItem
        },
        Rearrange(item){
            if(items.includes(item))items.push(items.splice(items.indexOf(item),1))
        }
    }

    commands.forEach(item=>{
        const [command,...options] = item.split(" ")
        actions[command](...options)
    })
    return items.join(", ")
}

console.log(solve(["Tomatoes!Potatoes!Bread",
    "Unnecessary Milk",
    "Urgent Tomatoes",
    "Go Shopping!"])
)

console.log(solve((["Milk!Pepper!Salt!Water!Banana",
    "Urgent Salt",
    "Urgent Watermelon",
    "Unnecessary Grapes",
    "Unnecessary Salt",
    "Correct Pepper Onion",
    "Rearrange Grapes",
    "Rearrange Water",
    "Correct Tomatoes Potatoes",
    "Correct Milk Eggs",
    "Go Shopping!"])
))