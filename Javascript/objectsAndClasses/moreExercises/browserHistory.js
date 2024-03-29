/*Creating function for task name: solve*/

function solve(browser,commands) {
    const actions ={
        "Open":(site,command)=> {
            browser["Open Tabs"].push(site)
            browser["Browser Logs"].push(command)
        },
        "Close":(site,command)=> {
            if (!browser["Open Tabs"].includes(site)) return
            browser["Open Tabs"].splice(browser["Open Tabs"].indexOf(site), 1)
            browser["Recently Closed"].push(site)
            browser["Browser Logs"].push(command)
        },
        "Clear":(...v)=>{
            browser["Open Tabs"].splice(0)
            browser["Recently Closed"].splice(0)
            browser["Browser Logs"].splice(0)

    },
    }
    commands.forEach(command=>{
        let cmd = command.split(" ")
        actions[cmd[0]](cmd.slice(1).join(" "),command)
    })
    console.log(browser["Browser Name"])
    delete browser["Browser Name"]
    Object.entries(browser).forEach(([name,values])=>console.log(`${name}: ${values.join(", ")}`))

}

console.log(solve({"Browser Name":"Google Chrome","Open Tabs":["Facebook","YouTube","Google Translate"],
        "Recently Closed":["Yahoo","Gmail"],
        "Browser Logs":["Open YouTube","Open Yahoo","Open Google Translate","Close Yahoo","Open Gmail","Close Gmail","Open Facebook"]},
    ["Close Facebook", "Open StackOverFlow", "Open Google"]
))

console.log(solve({"Browser Name":"Mozilla Firefox",
        "Open Tabs":["YouTube"],
        "Recently Closed":["Gmail", "Dropbox"],
        "Browser Logs":["Open Gmail", "Close Gmail", "Open Dropbox", "Open YouTube", "Close Dropbox"]},
    ["Open Wikipedia", "Clear History and Cache", "Open Twitter","Close zanzibart"]
))