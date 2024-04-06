function solve() {
    let nextStopId = "depot"
    const url = `http://localhost:3030/jsonstore/bus/schedule`
    const toggleEnable = v => v.disabled ? v.removeAttribute("disabled") : v.setAttribute("disabled", "disabled")
    const infoEl = document.querySelector("#info .info")
    const [controlEl, departEL, arriveEl] = document.querySelectorAll("#controls,#controls input");

    function depart() {
        fetch(`${url}/${nextStopId}`)
            .then(response => response.json())
            .then(response => {
                toggleEnable(departEL);
                toggleEnable(arriveEl);
                infoEl.textContent = `Next stop ${response.name}`

            })
            .catch(error => {
                infoEl.textContent = "Error"
                departEL.setAttribute("disabled", "disabled")
                arriveEl.setAttribute("disabled", "disabled")
            })
    }

    async function arrive() {
        try {
            toggleEnable(departEL);
            toggleEnable(arriveEl);
            let response = await fetch(`${url}/${nextStopId}`)
            response = await response.json()
            nextStopId = response.next
            infoEl.textContent = `Arriving at ${response.name}`
        } catch {
            infoEl.textContent = "Error"
            departEL.setAttribute("disabled", "disabled")
            arriveEl.setAttribute("disabled", "disabled")
        }
    }

    return {
        depart,
        arrive
    };
}

let result = solve();