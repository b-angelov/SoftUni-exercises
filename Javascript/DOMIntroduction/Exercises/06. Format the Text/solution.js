function solve() {
    const textElement = document.querySelector("#exercise textarea#input")
    const output = document.getElementById("output")
    let text = textElement.value.split(".").filter(sentence=>sentence)
    output.innerHTML = ''
    for (let i = 0; i < text.length; i+=3) {
        output.innerHTML += `<p>${text.slice(i,i+3).join(".")}.</p>\n`
    }
}