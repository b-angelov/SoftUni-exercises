function encodeAndDecodeMessages() {
    const parentElement = document.querySelector("#container #main")
    const [encodeArea,decodeArea] = document.querySelectorAll("#main div textarea")
    parentElement.addEventListener("click",switchHandler)

    const buttonActions = {
        "Encode and send it":(event)=>{
            let input = encodeArea.value
            input = input.split("").map(char => String.fromCharCode(char.charCodeAt() + 1)).join("")
            encodeArea.value = ""
            decodeArea.value = input
        },
        "Decode and read it":(event)=>{
            decodeArea.value = decodeArea.value.split("").map(char => String.fromCharCode(char.charCodeAt() - 1)).join("")
        },
    }

    function switchHandler(event){
        if(event.target.tagName !== "BUTTON") return
        buttonActions[event.target.textContent](event.target.previousElementSibling.value)
    }
}