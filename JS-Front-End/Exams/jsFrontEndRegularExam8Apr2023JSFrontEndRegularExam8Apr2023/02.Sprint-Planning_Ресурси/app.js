window.addEventListener('load', solve);

function solve() {
    const [taskIdHiddenElement,titleField,descriptionField,labelField,pointsField,assigneeField,createTaskButton,deleteTaskButton] = Array.from(document.querySelectorAll("#create-task-form input, #create-task-form textarea,#create-task-form select"))
    const taskSection = document.querySelector("#tasks-section")
    const taskPointsElement = taskSection.querySelector("p")
    const bugClasses = {"Feature": {class:"feature",symbol:"&#8865;"},"Low Priority Bug": {class:"low-priority",symbol:"&#9737;"},"High Priority Bug": {class:"high-priority",symbol:"&#9888;"}}
    let tasksCount = 0
    let currentPoints = 0
    createTaskButton.addEventListener("click",createTask)

    function resetPoints(points){
        currentPoints += Number(points)
        taskPointsElement.textContent = `Total Points ${currentPoints}pts`
    }

    function createTask(){
        const fields = [titleField,descriptionField,labelField,pointsField,assigneeField].map(el=>el.value)
        if (!fields.every(el=>el)) return
        setFields()
        const [title,description,label,points,assignee] = fields
        tasksCount++
        resetPoints(points)
        let elements = {
            main: {tag:"article",options:{className:"task-card",id:`task-${tasksCount}`}},
            label:{tag:"div",options:{className:`task-card-label ${bugClasses[label].class}`,innerHTML:`${label} ${bugClasses[label].symbol}`,"data-value":label}},
            title: {tag:"h3",options:{className:"task-card-title",textContent:title,"data-value":title}},
            description: {tag:"p",options:{className:"task-card-description",textContent:description,"data-value":description}},
            estimatedPoints:{tag:"div",options:{className:"task-card-points",textContent:`Estimated at ${points} pts`,"data-value":points}},
            assignee:{tag:"div",options:{className:"task-card-assignee",textContent:`Assigned to: ${assignee}`,"data-value":assignee}},
            actions:{tag:"div",options:{className:"task-card-actions"}},
            deleteButton:{tag:"button",options:{textContent:"Delete"}}
        }
        elements = Object.entries(elements).reduce((prev,[key,{tag,options}])=>{
            prev[key] = Object.assign(document.createElement(tag),options)
            return prev
        },{})
        elements.main.appendChild(elements.label)
        elements.main.appendChild(elements.title)
        elements.main.appendChild(elements.description)
        elements.main.appendChild(elements.estimatedPoints)
        elements.main.appendChild(elements.assignee)
        elements.main.appendChild(elements.actions)
        elements.actions.appendChild(elements.deleteButton)

        elements.deleteButton.addEventListener("click",e=>{
            setFields(title,description,label,points,assignee,elements.main.id)
            deleteTaskButton.removeAttribute("disabled")
            createTaskButton.setAttribute("disabled","disabled")
            disableFields()
            deleteTaskButton.addEventListener("click",e=>{
                elements.main.remove()
                resetPoints(-points)
                setFields()
                createTaskButton.removeAttribute("disabled")
                deleteTaskButton.setAttribute("disabled","disabled")
                enableFields()
            },{once:true})
        })

        taskSection.appendChild(elements.main)
    }

    function setFields(title="",description="",label="",points="",assignee="",taskId = ""){
        [titleField.value,descriptionField.value,labelField.value,pointsField.value,assigneeField.value,taskIdHiddenElement.value] = [title,description,label,points,assignee,taskId]
    }

    function disableFields(){
        [titleField,descriptionField,labelField,pointsField,assigneeField].forEach(el=>el.setAttribute("disabled","disabled"))
    }

    function enableFields(){
        [titleField,descriptionField,labelField,pointsField,assigneeField].forEach(el=>el.removeAttribute("disabled"))
    }
}