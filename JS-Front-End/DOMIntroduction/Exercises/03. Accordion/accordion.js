function toggle() {
    const actions ={
        "More":(buttonElement,textElement)=> {
            buttonElement.textContent = "Less"
            textElement.style.display = 'block'
        },
        "Less":(buttonElement, textElement)=>{
            buttonElement.textContent = "More"
            textElement.style.display = 'none'
        },
    }

    const button = document.querySelector("#accordion .head .button")
    const text = document.querySelector("#accordion #extra")

    actions[button.textContent](button,text)
}