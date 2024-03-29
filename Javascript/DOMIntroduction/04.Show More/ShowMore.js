function showText() {
    const hiddenTextElement = document.querySelector("span#text")
    hiddenTextElement.style.display = hiddenTextElement.style.display === 'none' ?  'inline' : 'none'
    document.getElementById('more').style.display = 'none'
}