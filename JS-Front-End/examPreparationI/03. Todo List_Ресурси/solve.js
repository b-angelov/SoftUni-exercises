// TODO
function attachEvents() {
    const baseUrl = "http://localhost:3030/jsonstore/tasks"
    const [title,addButton,loadButton] = document.querySelectorAll("#root form input, #root form button")
    const todoList = document.querySelector("#todo-list")

    loadButton.addEventListener("click",e=>{
        e.preventDefault()
        loadAll()
    })

    addButton.addEventListener("click",async e=>{
        e.preventDefault()
        if(!title.value) return
        await fetch(baseUrl,{
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({name:title.value})
        })
        title.value = ""
        loadAll()
    })

    async function loadAll(){
        todoList.innerHTML = ""
        let items = await fetch(baseUrl)
        items = await items.json()
        Object.values(items).forEach(item=>createItem(item.name,item._id))
    }

    function createItem(title,id,editable=false){
        if(!title) return
        const elements = Object.entries({
            main:{tag:"li",options:{}},
            title:{tag:"span",options:{textContent:title}},
            titleEditable:{tag:"input",options:{value:title}},
            removeButton:{tag:"button",options:{textContent:"Remove"}},
            editButton:{tag:"button",options:{textContent:"Edit"}},
            submitButton:{tag:"button",options:{textContent:"Submit"}},
        }).reduce((prev,[name,{tag,options}])=>{
            prev[name] = Object.assign(document.createElement(tag), options)
            return prev
        },{})
        elements.main.appendChild(editable?elements.titleEditable:elements.title)
        elements.main.appendChild(elements.removeButton)
        elements.main.appendChild(editable?elements.submitButton:elements.editButton)

        elements.removeButton.addEventListener("click",async e=>{
            await fetch(`${baseUrl}/${id}`,{method:"DELETE"})
            loadAll()
        })
        elements.editButton.addEventListener("click",e=>{
            const editableEl = createItem(title,id,true)
            elements.main.innerHTML = ""
            Array.from(editableEl.children).forEach(el=>elements.main.appendChild(el))
            elements.main.querySelector("button:last-of-type").addEventListener("click",async e=>{
                await fetch(`${baseUrl}/${id}`,{
                    method:"PATCH",
                    headers:{"Content-Type":"application/json"},
                    body:JSON.stringify({
                        name:elements.main.querySelector("input").value
                    }),
                })
                loadAll()
            })
        })


        if (editable){
            return elements.main
        }else {
            todoList.appendChild(elements.main)
        }

    }
}

attachEvents();
