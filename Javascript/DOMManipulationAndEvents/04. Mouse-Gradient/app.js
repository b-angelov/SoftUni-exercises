function attachGradientEvents() {
    const gradientElement = document.querySelector("#gradient")
    const resultElement = document.getElementById("result")
    gradientElement.addEventListener("mouseout",hidePercentage)
    gradientElement.addEventListener("mousemove",showPercentage)

    function showPercentage(event) {
        const percentage = Math.trunc(event.offsetX / (event.target.clientWidth-1) * 100)
        resultElement.textContent = `${percentage}%`
    }


    function hidePercentage(event) {
        resultElement.textContent = ''
    }


}