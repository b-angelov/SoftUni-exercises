function addItem() {
    const [nameElement, valueElement] = document.querySelectorAll("#newItemText,#newItemValue")
    const menu = document.querySelector("select#menu")
    const element = document.createElement("option")
    element.value = valueElement.value
    element.textContent = nameElement.value
    nameElement.value = valueElement.value = ""
    menu.appendChild(element)
}