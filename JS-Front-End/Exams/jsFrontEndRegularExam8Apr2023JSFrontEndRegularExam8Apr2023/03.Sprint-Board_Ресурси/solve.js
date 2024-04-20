// TODO:
function attachEvents() {
    const baseUrl = `http://localhost:3030/jsonstore/tasks`
    const [loadBoardButton,titleField,descriptionArea,createTaskButton] = document.querySelectorAll("#form-section input,#form-section textarea")
    const [todoSection,inProgressSection,codeReviewSection,doneSection] = document.querySelectorAll("#todo-section ul,#in-progress-section ul,#code-review-section ul,#done-section ul")

    loadBoardButton.addEventListener("click",loadTasks)

    createTaskButton.addEventListener("click",async e=>{
        const fields = [titleField,descriptionArea].map(el=>el.value)
        if (!fields.every(el=>el)) return
        const [title,description] = fields;
        [titleField,descriptionArea].forEach(el=>el.value = "")
        await fetch(baseUrl,{
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({
                title,
                description,
                status:"ToDo",
            })
        })
        loadTasks()
    })

    const sectionsMapper = {
        ToDo:{fn:id=>patch("In Progress",id),text:"Move to In Progress",section:todoSection},
        "In Progress":{fn:id=>patch("Code Review",id),text:"Move to Code Review",section:inProgressSection},
        "Code Review":{fn:id=>patch("Done",id),text:"Move to Done",section:codeReviewSection},
        "Done":{fn:id=>remove(id),text:"Close",section:doneSection}
    }

    function createTask(title,description,section,id){
        let elements = {
            main: {tag:"li",options:{className:"task"}},
            title: {tag:"h3",options:{textContent:title}},
            description: {tag:"p",options:{textContent:description}},
            button: {tag:"button",options:{textContent:sectionsMapper[section].text}},
        }
        elements = Object.entries(elements).reduce((prev,[key,{tag,options}])=>{
            prev[key] = Object.assign(document.createElement(tag),options)
            return prev
        },{})
        elements.main.appendChild(elements.title)
        elements.main.appendChild(elements.description)
        elements.main.appendChild(elements.button)
        sectionsMapper[section].section.appendChild(elements.main)
        elements.button.addEventListener("click",e=>sectionsMapper[section].fn(id))
    }

    async function loadTasks(){
        [todoSection,inProgressSection,codeReviewSection,doneSection].forEach(el=>el.innerHTML = "")
        let tasks = await fetch(baseUrl)
        tasks = await tasks.json()
        Object.values(tasks).forEach(task=>{
            createTask(task.title,task.description,task.status,task._id)
        })
    }

    async function patch(newStatus,id){
        await fetch(`${baseUrl}/${id}`,{
            method:"PATCH",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({
                status:newStatus
            })
        })
        loadTasks()
    }
    async function remove(id){
        await fetch(`${baseUrl}/${id}`,{
            method:"DELETE"
        })
        loadTasks()
    }
}

attachEvents();