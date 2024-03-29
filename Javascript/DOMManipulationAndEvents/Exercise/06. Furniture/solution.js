function solve() {
    const [inputElement, outputElement] = Array.from(document.querySelectorAll("#exercise textarea"))
    const templateTd = document.querySelector("table.table tbody tr")
    const tableBody = document.querySelector("table.table tbody")
    const [generateButton, buyButton] = document.getElementsByTagName("button")
    generateButton.addEventListener("click",createElements)
    buyButton.addEventListener("click", buyItems)

    function createElements(){
        const values = JSON.parse(inputElement.value)
        values.forEach(el=>{
            let element = templateTd.cloneNode(true)
            element.innerHTML = element.innerHTML.replace(/(?<=$|^|>)\s+/g,'')
            const [image,name,price,decorationFactor,checkbox] = Array.from(element.querySelectorAll("td img, td p,td input"))
            checkbox.removeAttribute("disabled")
            image.src = el.img.trim()
            name.textContent = el.name
            price.textContent = el.price
            decorationFactor.textContent = el.decFactor
            tableBody.appendChild(element)
        })
    }

    function buyItems(event){
        outputElement.value = ""
        const checkedElements = document.querySelectorAll(" table tbody td input[type='checkbox']:checked")
        const [furniture, price, factor] = [[],[],[]]
        Array.from(checkedElements).forEach(element=>{
            element = element.parentElement.parentElement
            const [furn,pri,fact] = Array.from(element.querySelectorAll("td p"))
            furniture.push(furn.textContent)
            price.push(Number(pri.textContent))
            factor.push(Number(fact.textContent))
        })
        outputElement.value += `Bought furniture: ${furniture.join(", ")}\n`
        outputElement.value += `Total price: ${price.reduce((a,b)=>a+b,0).toFixed(2)}\n`
        outputElement.value += `Average decoration factor: ${(factor.reduce((a,b)=>a+b,0) / factor.length)}`
    }
}