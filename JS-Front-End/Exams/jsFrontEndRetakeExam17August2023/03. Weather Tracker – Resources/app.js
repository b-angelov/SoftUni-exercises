function logicHandler(){
    const baseUrl = "http://localhost:3030/jsonstore/tasks"
    const loadHistoryButton = document.querySelector("#history button#load-history")
    const [locationInput,temperatureInput,dateInput,buttonAddWeather,buttonEditWeather] = document.querySelectorAll("#main-container #form input,#main-container #form button")
    const templateContainer = document.querySelector("#history #list")
    const templateElement = templateContainer.querySelector(":scope > div.container")
    templateElement.remove()

    loadHistoryButton.addEventListener("click",loadHistory)
    buttonAddWeather.addEventListener("click",addWeather)
    // buttonEditWeather.addEventListener("click",editWeather)


    async function loadHistory() {
        templateContainer.innerHTML = ""
        let locations = await fetch(baseUrl)
        locations = await locations.json()
        Object.values(locations).forEach(location=>{
            addWeatherItem(
                location.location,
                location.temperature,
                location.date,
                location._id,
                changeFunction,
                deleteFunction
                )
        })
    }


    async function addWeather(e,itemId=false) {
        const [location,temperature,date] = [locationInput.value,temperatureInput.value,dateInput.value]
        if(![location,temperature,date].every(val=>val)) return
        const method = !itemId?"POST":"PUT"
        const body = {location,temperature,date}
        if(itemId) body._id = itemId
        await fetch(itemId?`${baseUrl}/${itemId}`:baseUrl,{
            method,
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify(body)
        })
        setFields()
        loadHistory()
    }


    function editWeather(itemId) {
        disableElement(buttonEditWeather)
        enableElement(buttonAddWeather)
        addWeather(false,itemId)
    }

    function changeFunction(e,location,temperature,date,id){
        enableElement(buttonEditWeather)
        disableElement(buttonAddWeather)
        setFields(location,temperature,date)
        buttonEditWeather.addEventListener("click",(e)=>editWeather(id),{once:true})
    }
    async function deleteFunction(e,id){
        await fetch(`${baseUrl}/${id}`,{
            method:"DELETE"
        })
        loadHistory()
    }
    enableElement = (element)=>element.removeAttribute("disabled")
    disableElement = (element)=>element.setAttribute("disabled","disabled")

    function addWeatherItem(location,temperature,date,id,changeFunc,delFunc){
        const item = templateElement.cloneNode(true)
        const [locationP,dateP,temperatureP,changeButton,deleteButton] = item.querySelectorAll("h2,h3,button")
        locationP.textContent = location
        temperatureP.textContent = temperature
        dateP.textContent = date
        changeButton.addEventListener("click",(e)=>changeFunc(e,location,temperature,date,id))
        deleteButton.addEventListener("click",(e)=>delFunc(e,id))
        templateContainer.appendChild(item)
    }

    function setFields(location="",temperature="",date=""){
        locationInput.value = location
        temperatureInput.value = temperature
        dateInput.value = date
    }


}

logicHandler()