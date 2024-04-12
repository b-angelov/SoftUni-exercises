function logicHandler() {
    const baseUrl = "http://localhost:3030/jsonstore/tasks"
    const [nameInp, numberOfDaysInp, fromDateInp, addVacationButton, editVacationButton] = document.querySelectorAll("#form input,#form button")
    const loadVacationsButton = document.querySelector("#confirmed-vacantions > button")
    const confirmedListElement = document.querySelector("#confirmed-vacantions #list")
    const templateItem = confirmedListElement.querySelector("div.container")
    templateItem.remove()

    loadVacationsButton.addEventListener("click", loadItems)
    addVacationButton.addEventListener("click", e=> {
        e.preventDefault()
        addVacation()
        setFields()
    })

    function addNewItem(name, daysOfStay, fromDate, changeFunc, deleteFunc) {
        const item = templateItem.cloneNode(true)
        const [nameEl, dateEl, daysEl, changeBtn, delBtn] = item.querySelectorAll("h2,h3,button")
        nameEl.textContent = name
        dateEl.textContent = fromDate
        daysEl.textContent = daysOfStay
        changeBtn.addEventListener("click", changeFunc)
        delBtn.addEventListener("click", deleteFunc)
        confirmedListElement.appendChild(item)
    }

    async function loadItems() {
        confirmedListElement.innerHTML = ""
        let items = await fetch(baseUrl)
        items = await items.json()
        Object.values(items).forEach(item => {
            addNewItem(
                item.name,
                item.days,
                item.date,
                (e) => changeItem(e, item._id),
                (e) => deleteItem(e, item._id)
            )
        })
    }

    function setFields(name = "", days = "", date = "") {
        nameInp.value = name
        numberOfDaysInp.value = days
        fromDateInp.value = date
    }

    enableEl = el => el.removeAttribute("disabled")
    disableEl = el => el.setAttribute("disabled", "disabled")

    function changeItem(e,id) {
        enableEl(editVacationButton)
        disableEl(addVacationButton)
        const el = e.target.parentElement
        el.remove()
        const [name,date,days] = Array.from(el.querySelectorAll("h2,h3")).map(el=>el.textContent)
        nameInp.value = name
        numberOfDaysInp.value = days
        fromDateInp.value = date
        editVacationButton.addEventListener("click",async (e)=> {
            e.preventDefault()
            await addVacation(id)
            setFields()
            enableEl(addVacationButton)
            disableEl(editVacationButton)
        },{once:true})
    }

    async function deleteItem(e,id) {
        await fetch(`${baseUrl}/${id}`,{
            method:"DELETE"
        })
        loadItems()
    }

    async function addVacation(itemId) {
        const body = {}
        let method = "POST"
        let url = baseUrl
        if (itemId) {
            method = "PUT"
            body._id = itemId
            url = `${baseUrl}/${itemId}`
        }
        body.name = nameInp.value
        body.days = numberOfDaysInp.value
        body.date = fromDateInp.value
        await fetch(url, {
            method,
            "Content-Type": "application/json",
            body:JSON.stringify(body)
        })
        loadItems()
    }

    function editVacation(itemId) {

    }
}

logicHandler()