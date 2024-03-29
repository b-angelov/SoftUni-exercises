function attachEventsListeners() {

    const mainElement = document.getElementsByTagName("main")[0]
    mainElement.addEventListener("change",handleInput)
    mainElement.addEventListener("click",handleConversion)

    const convertorsFrom = {
        days: (value) => Number(value) * 24 * 60 * 60,
        hours: (value) => Number(value) * 60 * 60,
        minutes: (value) => Number(value) * 60,
        seconds: (value) => Number(value),
    }

    const convertorsTo = {
        days: (value) => Number(value) / 24 / 60 / 60,
        hours: (value) => Number(value) / 60 / 60,
        minutes: (value) => Number(value) / 60,
        seconds: (value) => Number(value),
    }

    function handleInput(event){

    }

    function handleConversion(event){
        if(event.target.type !== "button") return
        const inputElement = event.target.previousElementSibling
        const inputElements = document.querySelectorAll("main div input[type='text']")
        const input = convertorsFrom[inputElement.id](inputElement.value)
        Array.from(inputElements).forEach(element=>element.value = convertorsTo[element.id](input))
    }

}