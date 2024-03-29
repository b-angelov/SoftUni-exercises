function validate() {
    const fieldElement = document.querySelector("body input")
    const toggleClass = ()=> fieldElement.classList.contains("error")?fieldElement.classList.remove("error"):fieldElement.classList.add("error")
    function validateEmail(event){
        const email = event.target.value
        const valid = email.match(/^[a-z]+@[a-z]+\.[a-z]+$/)
        if(valid && event.target.classList.contains("error")){
            toggleClass()
        }else if(!valid && !event.target.classList.contains("error")){
            toggleClass()
        }
    }

    fieldElement.addEventListener("change",validateEmail)
}