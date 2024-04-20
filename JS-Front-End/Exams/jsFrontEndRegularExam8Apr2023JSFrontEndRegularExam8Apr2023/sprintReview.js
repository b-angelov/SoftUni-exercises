/*Creating function for task name: Sprint Review*/

function sprintReview(data) {
    let assignees = data.slice(1, Number(data[0]) + 1)
    const commands = data.slice(Number(data[0]) + 1)

    assignees = assignees.reduce((prev, el) => {
        const [name, taskId, title, status, estimatedPoints] = el.split(":")
        if (!prev.hasOwnProperty(name)) prev[name] = {}
        prev[name][taskId] = {title, status, estimatedPoints: Number(estimatedPoints)}
        return prev
    }, {})


    function getAssignee(assignee) {
        if (!assignees.hasOwnProperty(assignee)) {
            console.log(`Assignee ${assignee} does not exist on the board!`)
            return
        }
        return assignees[assignee]
    }

    function getTask(assigneeName, taskId) {
        const assignee = getAssignee(assigneeName)
        if (assignee) {
            const idx = Object.keys(assignee).indexOf(taskId)
            if (idx > -1) {
                return assignee[taskId]
            }
            console.log(`Task with ID ${taskId} does not exist for ${assigneeName}!`)
        }
    }

    const actions = {
        "Add New": (assignee, taskId, title, status, estimatedPoints) => {
            assignee = getAssignee(assignee)
            if (assignee) {
                assignee[taskId] = {title, status, estimatedPoints: Number(estimatedPoints)}
            }
        },
        "Change Status": (assignee, taskId, newStatus) => {
            const task = getTask(assignee, taskId)
            if (task) task.status = newStatus
        },
        "Remove Task": (assignee, index) => {
            assignee = getAssignee(assignee)
            if (assignee) {
                const tasks = Object.keys(assignee)
                if (index < 0 || index >= tasks.length) {
                    console.log("Index is out of range!")
                    return
                }
                delete assignee[tasks[index]]
            }
        },
    }

    commands.forEach(command => {
        const [com, ...options] = command.split(":")
        actions[com](...options)
    })

    let donePoints = 0
    let elsePoints = 0

    const statuses = Object.values(assignees).reduce((prev, el) => {
        Object.values(el).forEach(sub=>
        {
            if (!prev.hasOwnProperty(sub.status)) prev[sub.status] = 0
            prev[sub.status] += sub.estimatedPoints
            if (sub.status === "Done") {
                donePoints += sub.estimatedPoints
            }else {
                elsePoints += sub.estimatedPoints
            }
        })
        return prev
    }, {})

    console.log(`ToDo: ${Number(statuses.ToDo) || 0}pts`)

    console.log(`In Progress: ${Number(statuses['In Progress']) || 0}pts`)

    console.log(`Code Review: ${Number(statuses['Code Review']) || 0}pts`)

    console.log(`Done Points: ${Number(statuses['Done']) || 0}pts`)

    if (donePoints >= elsePoints){
        console.log("Sprint was successful!")
    }else {
        console.log("Sprint was unsuccessful...")
    }


}

sprintReview([
        '5',
        'Kiril:BOP-1209:Fix Minor Bug:ToDo:3',
        'Mariya:BOP-1210:Fix Major Bug:In Progress:3',
        'Peter:BOP-1211:POC:Code Review:5',
        'Georgi:BOP-1212:Investigation Task:Done:2',
        'Mariya:BOP-1213:New Account Page:In Progress:13',
        'Add New:Kiril:BOP-1217:Add Info Page:In Progress:5',
        'Change Status:Peter:BOP-1290:ToDo',
        'Remove Task:Mariya:1',
        'Remove Task:Joro:1',
    ]
)

sprintReview([
        '4',
        'Kiril:BOP-1213:Fix Typo:Done:1',
        'Peter:BOP-1214:New Products Page:In Progress:2',
        'Mariya:BOP-1215:Setup Routing:ToDo:8',
        'Georgi:BOP-1216:Add Business Card:Code Review:3',
        'Add New:Sam:BOP-1237:Testing Home Page:Done:3',
        'Change Status:Georgi:BOP-1216:Done',
        'Change Status:Will:BOP-1212:In Progress',
        'Remove Task:Georgi:3',
        'Change Status:Mariya:BOP-1215:Done',
    ]
)