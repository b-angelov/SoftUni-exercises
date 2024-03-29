function addItem() {
    const textInput = document.getElementById("newItemText")
    const ulElement = document.getElementById("items")
    const newLi = document.createElement("li")
    newLi.textContent = textInput.value

    ulElement.appendChild(newLi)
}