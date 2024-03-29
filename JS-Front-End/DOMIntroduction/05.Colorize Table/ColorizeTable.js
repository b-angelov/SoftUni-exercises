function colorize() {
    const colorizedElements = document.querySelectorAll("table tr:nth-of-type(even)")
    Array.from(colorizedElements).forEach(element=>element.style.backgroundColor = 'teal')
}