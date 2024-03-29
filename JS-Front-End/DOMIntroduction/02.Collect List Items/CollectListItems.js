function extractText() {
    const listItems = document.querySelectorAll("#items li")
    const textarea = document.getElementById("result")
    console.log(listItems)
    Array.from(listItems).forEach(item=>textarea.textContent += item.textContent+"\n")
}