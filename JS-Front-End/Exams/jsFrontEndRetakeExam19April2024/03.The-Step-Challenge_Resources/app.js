function logicHandler(){
    const baseUrl = "http://localhost:3030/jsonstore/records"
    const templateItem = document.querySelector("#records #list li.record")
    const listElement = document.querySelector("#records #list")
    templateItem.remove()
    const [loadButton,pNameField,stepsField,caloriesField,addRecordButton,editRecordButton] = document.querySelectorAll("button,input")

    loadButton.addEventListener("click",loadRecords)
    addRecordButton.addEventListener("click",async e=>{
        const fields = [pNameField,stepsField,caloriesField].map(el=>el.value)
        if(!fields.every(el=>el)) return
        const [name,steps,calories] = fields
        e.preventDefault()
        await fetch(baseUrl,{
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({name,steps,calories})
        })
        loadRecords()
        setFields()
    })

    async function loadRecords(){
        listElement.innerHTML = ""
        let records = await fetch(baseUrl)
        records = await records.json()
        Object.values(records).forEach(el=>createRecord(el.name,el.steps,el.calories,el._id))
    }

    function createRecord(name,steps,calories,id){
        const elements = Object.entries({
            main:{tag:"li",options:{className:"record"}},
            info:{tag:"div",options:{className:"info"}},
            name:{tag:"p",options:{textContent:name}},
            steps:{tag:"p",options:{textContent:steps}},
            calories:{tag:"p",options:{textContent:calories}},
            buttons:{tag:"div",options:{className:"btn-wrapper"}},
            changeButton:{tag:"button",options:{textContent:"Change",className:"change-btn"}},
            deleteButton:{tag:"button",options:{textContent:"Delete",className:"delete-btn"}},
        }).reduce((prev,[name,{tag,options}])=>{
            prev[name] = Object.assign(document.createElement(tag),options)
            return prev
        },{})
        elements.main.appendChild(elements.info)
        elements.main.appendChild(elements.buttons)
        elements.info.appendChild(elements.name)
        elements.info.appendChild(elements.steps)
        elements.info.appendChild(elements.calories)
        elements.buttons.appendChild(elements.changeButton)
        elements.buttons.appendChild(elements.deleteButton)
        listElement.appendChild(elements.main)
        elements.deleteButton.addEventListener("click",async e=>{
            await fetch(`${baseUrl}/${id}`,{method:"DELETE"})
            loadRecords()
        })
        elements.changeButton.addEventListener("click",e=>{
            elements.main.remove()
            setFields(name,steps,calories)
            addRecordButton.setAttribute("disabled","disabled")
            editRecordButton.removeAttribute("disabled")
            editRecordButton.addEventListener("click",async e=>{
                editRecordButton.setAttribute("disabled","disabled")
                addRecordButton.removeAttribute("disabled")
                await fetch(`${baseUrl}/${id}`,{
                    method:"PUT",
                    headers:{"Content-Type":"application/json"},
                    body:JSON.stringify({
                        name:pNameField.value,
                        steps:stepsField.value,
                        calories:caloriesField.value,
                        _id:id
                    })
                })
                loadRecords()
                setFields()
            },{once:true})
        })

    }

    function setFields(pName="",steps="",calories=""){
        [pNameField.value,stepsField.value,caloriesField.value] = [pName,steps,calories]
    }
}

logicHandler()