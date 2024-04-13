window.addEventListener("load", solve);

function solve() {
    // const [nameInp,phoneInp,categorySelect,addButton] = document.querySelectorAll("#add-contact form input,#add-contact form select")
    const nameInp = document.getElementById("name")
    const phoneInp = document.getElementById("phone")
    const categorySelect = document.getElementById("category")
    const addButton = document.getElementById("add-btn")
    const [checkEl,contactEl] = document.querySelectorAll("#check-contact ul")
    console.log(contactEl)

    checkEl.addEventListener("click",e=>{
        e.preventDefault()
        if (e.target.tagName !== "BUTTON") return
        if (e.target.className === "edit-btn"){
            edit(e)
        }else{
            save(e)
        }
    })


    function save(e){
        const parent = e.target.parentElement.parentElement
        const buttonEl = e.target.parentElement
        console.log(buttonEl)
        buttonEl.remove()
        const delButton = document.createElement("button")
        delButton.className = "del-btn"
        parent.appendChild(delButton)
        contactEl.appendChild(parent)
        delButton.addEventListener("click",e=>parent.remove())
    }

    function edit(e){
        const parent = e.target.parentElement.parentElement
        console.log(parent)
        const [name,phone,category] = Array.from(parent.querySelectorAll("p")).map(val=>val.textContent.split(":")[1])
        console.log(name)
        setFields(name,phone,category)
        parent.remove()
    }

    addButton.addEventListener("click",e=>{
        e.preventDefault()
        console.log(nameInp.value,phoneInp,categorySelect,addButton)
        if (![nameInp.value,phoneInp.value,categorySelect.value].every(val=>val)) return
        createItem(nameInp.value,phoneInp.value,categorySelect.value)
        setFields()
    })

    function setFields(name="",phone="",category=""){
        nameInp.value = name
        phoneInp.value = phone
        categorySelect.value = category
    }

    function createItem(name,phone,category){
        const newLi = document.createElement("li")
        const newArticle = document.createElement("article")
        const newButtonEL = document.createElement("div")
        newButtonEL.className = "buttons"
        newLi.appendChild(newArticle)
        newLi.appendChild(newButtonEL)
        const nameEl = document.createElement("p")
        const categoryEl = document.createElement("p")
        const phoneEl = document.createElement("p")
        nameEl.textContent = `name:${name}`
        phoneEl.textContent = `phone:${phone}`
        categoryEl.textContent = `category:${category}`
        newArticle.appendChild(nameEl)
        newArticle.appendChild(phoneEl)
        newArticle.appendChild(categoryEl)
        const editButton = document.createElement("button")
        editButton.className = "edit-btn"
        // editButton.textContent = "Edit"
        const saveButton = document.createElement("button")
        saveButton.className = "save-btn"
        // saveButton.textContent = "Save"
        newButtonEL.appendChild(editButton)
        newButtonEL.appendChild(saveButton)
        checkEl.appendChild(newLi)
    }
}
  