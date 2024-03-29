function subtract() {
    const elements = document.querySelectorAll("#wrapper input")
    const result = document.getElementById('result')

    const [a,b] = Array.from(elements,element=>element.value)

    result.textContent = a-b
}