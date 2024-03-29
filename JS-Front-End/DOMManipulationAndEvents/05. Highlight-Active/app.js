function focused() {
    function addFocus(event){
        event.target.parentNode.classList.add("focused")
    }
    function removeFocus(event){
        event.target.parentNode.classList.remove("focused")
    }
    const divElements = document.querySelectorAll("body div div")

    Array.from(divElements).forEach(element=>{
        element = element.getElementsByTagName("input")[0]
        element.addEventListener('focus',addFocus)
        element.addEventListener("blur",removeFocus)
    })


}