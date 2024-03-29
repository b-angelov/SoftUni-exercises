function calc() {
    const [x,y,output] = document.querySelectorAll("input[type=text]")
    output.value = Number(x.value) + Number(y.value)
}
