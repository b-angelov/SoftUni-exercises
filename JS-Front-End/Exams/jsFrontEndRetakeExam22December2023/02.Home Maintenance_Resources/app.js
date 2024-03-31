window.addEventListener("load", solve)

function solve(){
    const [placeField,actionField,personField, addButton] = Array.from(document.querySelectorAll("#add-task form input"))
    const taskList = document.querySelector("#tasks #task-list")
    const doneList = document.querySelector("#tasks #done-list")
    taskList.addEventListener("click",(event)=>{
        if(event.target.tagName !== "BUTTON") return
        taskEvents[event.target.textContent.toLowerCase()](event.target)
    })
    doneList.addEventListener("click",(event)=>{
        if(event.target.tagName !== "BUTTON") return
        event.target.parentElement.remove()
    })

    addButton.addEventListener("click",(event)=>{
        const options = [placeField,actionField,personField]
        if(!options.every(el=>el.value)) return
        attachElement(taskList,createTask(options))
        clearFields(options)
    })

    const taskEvents = {
        edit: (target)=>{
            const mainParent = target.parentElement.parentElement
            const fields = Array.from(mainParent.querySelectorAll("article p"))
            const options = [placeField,actionField,personField]
            fields.forEach((field,idx)=>{
                options[idx].value = field.textContent.split(":")[1]
            })
            mainParent.remove()
        },
        done: (target)=>{
            const mainParent = target.parentElement.parentElement
            const elements = mainParent.querySelector("article")
            const buttons = mainParent.querySelector(".buttons")
            const buttonTemplate = buttons.querySelector("button")
            mainParent.removeAttribute("class")
            buttonTemplate.textContent = "Delete"
            buttonTemplate.classList.remove("edit")
            buttonTemplate.classList.add("delete")
            buttons.remove()
            mainParent.appendChild(buttonTemplate)
            mainParent.remove()
            doneList.appendChild(mainParent)

        }
    }

    function createTask(options){
        const mainFragment = document.createElement("li")
        mainFragment.classList.add(`clean-task`)
        const article = document.createElement("article")
        const buttonsDiv = document.createElement("div",)
        buttonsDiv.classList.add("buttons")
        const editButton = document.createElement("button")
        editButton.textContent = "Edit"
        editButton.classList.add("edit")
        const doneButton = document.createElement("button")
        doneButton.textContent = "Done"
        doneButton.classList.add("done")
        buttonsDiv.appendChild(editButton)
        buttonsDiv.appendChild(doneButton)
        options.forEach(option=>{
            const pEl = document.createElement("p")
            pEl.textContent = `${option.placeholder}:${option.value}`
            article.appendChild(pEl)
        })
        mainFragment.appendChild(article)
        mainFragment.appendChild(buttonsDiv)
        return mainFragment
    }

    function attachElement(element,attachment){
        element.appendChild(attachment)
    }

    function clearFields(fields){
        fields.forEach(field=>field.value = "")
    }


}