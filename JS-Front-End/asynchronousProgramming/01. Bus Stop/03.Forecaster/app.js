function attachEvents() {
    const baseUrl = "http://localhost:3030/jsonstore/forecaster"
    const [locationInput, getWeatherButton] = document.querySelectorAll("#request input");
    const forecastElement = document.querySelector("#forecast");
    const upcomingElement = document.querySelector("#upcoming");
    const forecastTemplate = forecastElement.querySelectorAll("*[id]");
    console.log(forecastTemplate);
    const weatherMap ={
        Sunny:"☀",
        "Partly sunny":"⛅",
        Overcast:"☁",
        Rain:"☂",
        Degrees:"°",
    }

    getWeatherButton.addEventListener("click", (event) => {
        forecastTemplate.forEach((item) => {item.querySelectorAll(":scope > div:nth-child(1n+2)").forEach(item2=>item2.remove())});
        forecastElement.style.display = "block"
        getLocation(locationInput.value)
    })

    function getLocation(location) {
        fetch(`${baseUrl}/locations`)
            .then(response => response.json())
            .then(response => Object.values(response).find(element => element.name.toLowerCase() === location.toLowerCase()))
            .then(response => {
                return ({"city": response, "today": fetch(`${baseUrl}/today/${response.code}`).then(response=>response.json())})
            })
            .then(response=> {
                return ({...response,"upcoming":fetch(`${baseUrl}/upcoming/${response.city.code}`).then(response=>response.json())})
            })
            .then(response=> {
                Promise.all([response.today, response.upcoming]).then(response=>displayWeather(response[0], response[1]))
            })
            .catch(error)
    }

    function displayWeather(today, upcoming) {

        const createDataElement = (data,city,upcoming=false,classname="condition")=>{
            const frag = document.createDocumentFragment();
            if(!Array.isArray(data)) data = [data]
            data.forEach(element=>{
                const spanForecastInfo = document.createElement("span")
                spanForecastInfo.className = classname
                console.log(element,!upcoming)
                if(!upcoming) {
                    element = [city, `${element.low}${weatherMap.Degrees}/${element.high}${weatherMap.Degrees}`, element.condition]
                }else{
                    console.log("upcom")
                    const nEl = document.createElement("span")
                    nEl.className = "symbol"
                    nEl.textContent = weatherMap[element.condition]
                    spanForecastInfo.appendChild(nEl)
                    element = [`${element.low}${weatherMap.Degrees}/${element.high}${weatherMap.Degrees}`, element.condition]
                }
                Object.values(element).forEach(el=> {
                    const spanEl = document.createElement("span");
                    spanEl.textContent = el
                    spanEl.className = "forecast-data"
                    spanForecastInfo.appendChild(spanEl)
                })
                frag.appendChild(spanForecastInfo)
            })
            return frag
        }

        const fragment = document.createDocumentFragment()
        const [forecastsInnerElement, upcomingInnerElement] = [document.createElement('div'),document.createElement('div')]
        const conditionSymbolElement = document.createElement("span")
        const conditionElement = document.createElement("span")

        forecastsInnerElement.appendChild(conditionSymbolElement)
        forecastsInnerElement.appendChild(conditionElement)
        conditionElement.appendChild(createDataElement(today.forecast,today.name))
        fragment.appendChild(forecastsInnerElement)
        forecastElement.appendChild(forecastTemplate[0])
        forecastElement.appendChild(forecastTemplate[1])
        forecastTemplate[0].appendChild(forecastsInnerElement)
        // fragment.appendChild(upcomingElement)

        conditionSymbolElement.className = "condition symbol"
        conditionSymbolElement.textContent = `${weatherMap[today.forecast.condition]}`
        conditionElement. className = "condition"
        forecastsInnerElement.id = "forecasts"
        upcomingInnerElement.className = "forecast-info"
        upcomingInnerElement.appendChild(createDataElement(upcoming.forecast,null,true,"upcoming"))
        forecastTemplate[1].appendChild(upcomingInnerElement)



    }


    const error = (error) => {
        const err = document.createElement("div");
        err.style.className = "label"
        err.textContent = "Error" + error
        forecastElement.appendChild(err)
    }
}

attachEvents();