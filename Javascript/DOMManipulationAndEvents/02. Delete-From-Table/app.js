function deleteByEmail() {
    const rows = document.querySelectorAll("tbody tr")
    const email = document.querySelector("label input").value
    const resultElement = document.querySelector("#result")
    let found = false

    Array.from(rows).forEach(row=>{
        const td = row.querySelector("td:last-of-type")
        if(td.textContent === email){
            found = true
            row.parentNode.removeChild(row)
        }
    })
    resultElement.textContent = found?"Deleted.":"Not found."
}