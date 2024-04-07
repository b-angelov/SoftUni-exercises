function attachEvents() {
    const baseUrl = "http://localhost:3030/jsonstore/phonebook"
    const [phoneBookUlElement, loadButton, personInputElement, phoneInputElement, createButton] = document.querySelectorAll("ul,button,input")

    loadButton.addEventListener("click", loadContacts)

    phoneBookUlElement.addEventListener("click", event => {
        if (event.target.tagName !== "BUTTON") return
        fetch(`${baseUrl}/${event.target.value}`,{
            method:"DELETE",
            headers:{
                "Content-Type":"application/json"
            }
        })
            .then(response=>{
                event.target.parentElement.remove()
            })
            .catch(error)
    })

    createButton.addEventListener("click",event=>{
        fetch(baseUrl,{
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({
                person: personInputElement.value,
                phone:phoneInputElement.value
            })
        })
            .then(response=>{
                personInputElement.value = ""
                phoneInputElement.value = ""
            })
            .then(loadContacts)
            .catch(error)
    })

    const error = error => console.log(error)

    function loadContacts(){
        fetch(baseUrl)
            .then(response => response.json())
            .then(response => {
                viewContacts(Object.values(response).map(item => {
                    const el = document.createElement("li")
                    const delItem = document.createElement("button")
                    delItem.textContent = "Delete"
                    delItem.value = item._id
                    el.textContent = `${item.person}: ${item.phone}`
                    el.appendChild(delItem)
                    return el
                }))
            })
            .catch(error)
    }

    function viewContacts(contacts) {
        phoneBookUlElement.innerHTML = ""
        contacts.forEach(contact => phoneBookUlElement.appendChild(contact))
    }

}

attachEvents();