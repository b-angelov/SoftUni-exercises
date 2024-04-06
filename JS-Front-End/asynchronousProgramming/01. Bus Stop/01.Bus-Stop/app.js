function getInfo() {
    const [idElement,submitButton, stopNameEl, busesUl] = Array.from(document.querySelectorAll("#stopInfo div input, #stopInfo div div, #stopInfo div ul"))
    const infoUrl = "http://localhost:3030/jsonstore/bus/businfo"
    // console.log(idElement,submitButton,stopNameEl,busesUl)
    let busInfo = {}

    fetch(`${infoUrl}/${idElement.value}`)
        .then(response=>{
            return response.json()
        })
        .then(response=>{
            loadFields(response)
        })
        .catch(error)

    function error(err){
        busesUl.innerHTML = ""
        stopNameEl.textContent = "Error"
    }

    function loadFields(fieldsObj){
        busesUl.innerHTML = ""
        stopNameEl.textContent = fieldsObj.name
        Object.entries(fieldsObj.buses).forEach(([number,time])=>{
            const newLi = document.createElement("li")
            newLi.textContent = `Bus ${number} arrives in ${time} minutes`
            busesUl.appendChild(newLi)
        })
    }
}