function addItem() {
    const textInput = document.getElementById("newItemText")
    const ulElement = document.getElementById("items")
    const newLi = document.createElement("li")
    const del = document.createElement("a")
    del.href = "#"
    del.textContent = "[Delete]"
    // del.style.color = "red"
    // del.style.cursor = "pointer"
    del.addEventListener("click",()=>ulElement.removeChild(newLi))
    newLi.textContent = textInput.value
    newLi.appendChild(del)

    ulElement.appendChild(newLi)
}