function attachEventsListeners() {

    const [fromElement,toElement] = document.querySelectorAll("body > div select")
    document.getElementsByTagName("body")[0].addEventListener("click",handleConversion)

    const unitsInMeters = {
        km: 1000,
        m: 1,
        cm: 0.01,
        mm: 0.001,
        mi: 1609.34,
        yrd: 0.9144,
        ft: 0.3048,
        in: 0.0254,
    }

    const unitToMeter = (unit,value) => Number(value) * unitsInMeters[unit]
    const unitFromMeter = (unit,value) => Number(value) / unitsInMeters[unit]

    function handleConversion(event){
        if(event.target.type !== "button") return
        const from = fromElement.value
        const to = toElement.value
        const fromInput = fromElement.previousElementSibling.value
        const toField = toElement.previousElementSibling
        if(!unitsInMeters[from] || !unitsInMeters[to]) return
        const result = unitFromMeter(to,unitToMeter(from,fromInput))
        toField.removeAttribute("disabled")
        toField.value = result
    }
}