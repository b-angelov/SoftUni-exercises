/*Creating function for task name: solve*/
//Not fully working

function solve(data) {
    const userList = []
    const articlesList = []
    const info = {}
    const postsOn = []

    const splitConditions = {
        user: value => [value.split("user ")[1]],
        article: value => [value.split("article ")[1]],
        "posts on": value => {
            let [first, second] = value.split(": ")
            first = first.split(" posts on ")
            second = second.split(", ")
            return [...first,...second]
        },
    }
    const actions ={
        user: value => userList.push(value),
        article: value => articlesList.push(value),
        'posts on':(userName,article,commentTitle, commentContent)=>{
            if (userList.includes(userName) && articlesList.includes(article)){
                if(!info.hasOwnProperty(article)) info[article] = {}
                if(!info[article].hasOwnProperty(userName)) info[article][userName] = {}
                info[article][userName][commentTitle] = commentContent
            }
        },
    }

    for (let command of data){
        for(let action of Object.keys(actions)){
            if (command.includes(action) && action !== "posts on"){
                command = splitConditions[action](command)
                actions[action](...command)
                break
            }else if(command.includes(action) && action === "posts on"){
                postsOn.push(command)
                break
            }
        }
    }
    for (let command of postsOn){
        command = splitConditions["posts on"](command)
        actions["posts on"](...command)
    }
    // My sort
    Object.entries(info)
        .sort(([name,data],[nameB,dataB])=>
            Object.entries(dataB).reduce((a,b)=>
                Number(a) + Object.keys(Object.values(b)).length,0) -
            Object.entries(data).reduce((a,b)=>
                Number(a) + Object.keys(Object.values(b)).length,0))
        .forEach(([article,users])=>{
            console.log(`Comments on ${article}`)
            Object.entries(users)
                .sort(([username,comments],[usernameB,commentsB])=>username.localeCompare(usernameB))
                .forEach(([username,comment])=>{
                    Object.entries(comment).forEach(currentComment=> {
                        console.log(`--- From user ${username}: ${currentComment.join(' - ')}`)
                    })
                })
        })
}

solve(['user aUser123', 'someUser posts on someArticle: NoTitle, stupidComment', 'article Books', 'article Movies', 'article Shopping', 'user someUser', 'user uSeR4', 'user lastUser', 'uSeR4 posts on Books: I like books, I do really like them', 'uSeR4 posts on Movies: I also like movies, I really do', 'someUser posts on Shopping: title, I go shopping every day', 'someUser posts on Movies: Like, I also like movies very much'])
// solve(['user Mark', 'Mark posts on someArticle: NoTitle, stupidComment', 'article Bobby', 'article Steven', 'user Liam', 'user Henry', 'Mark posts on Bobby: Is, I do really like them', 'Mark posts on Steven: title, Run', 'someUser posts on Movies: Like'])