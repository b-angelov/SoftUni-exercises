function sumTable() {
    const summedRows = document.querySelectorAll('table tbody tr td:last-of-type')
    const output = document.getElementById('sum')

    output.textContent = Array.from(summedRows,el=>el.textContent).slice(0,-1).reduce((a,b)=>(Number(a) + Number(b)))
}