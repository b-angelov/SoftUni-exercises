function solve() {
    const cases = {
        "Pascal Case":text => text.split(" ").map(element => element[0].toUpperCase() + element.slice(1).toLowerCase()).join(""),
        "Camel Case": text => {
            text = cases["Pascal Case"](text)
            text = text[0].toLowerCase() + text.slice(1)
            return text
        },
    }
    const [text,convention] = document.querySelectorAll("form div input")
    const result = document.getElementById("result")

    result.textContent = cases[convention.value]?cases[convention.value](text.value):"Error!"

}