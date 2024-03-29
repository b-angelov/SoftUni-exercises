function extract(content) {
    const element = document.getElementById(content)
    return element.textContent.match(/(?<=\()[^)]+/gm).join("; ")
}
