function generateReport() {
    const keyElements = document.querySelectorAll("main table thead tr th input")
    const tableRows = document.querySelectorAll("tbody tr")
    const output = document.getElementById("output")
    const reportData = []

    Array.from(tableRows).forEach(row=>{
        row = row.children
        const data = {}
        Array.from(keyElements).forEach((element,idx)=>{
            if(element.checked){
                data[element.name] = row[idx].textContent
            }
        })
        reportData.push(data)
    })

    output.value = JSON.stringify(reportData,null,2)
}