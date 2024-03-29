function solve() {
    const cellLength = 3
    const fieldRows = Array.from(document.querySelectorAll("#exercise tbody tr"))
    const [checkButton, clearButton] = document.querySelectorAll("tfoot button")
    const tableElement = document.querySelector("table")
    const pElement = document.querySelector("div#check p")
    checkButton.addEventListener("click", solutionCheck)
    clearButton.addEventListener("click", clear)

    function getCells() {
        let field = Array(~~(fieldRows.length / cellLength)).fill().map(() => [])
        fieldRows.forEach(row => {
            row = Array.from(row.querySelectorAll("td > input"))
            for (let i = 0; i < row.length; i += cellLength) {
                field[i / cellLength].push(row.slice(i, i + cellLength))
            }
        })
        field = field.reduce((prev, column) => {

            const cells = column.reduce((p, c) => {
                if (!p.length || p[p.length - 1].length === 3) p.push([])
                p[p.length - 1].push(c)
                return p
            }, [])
            prev.push(cells)
            return prev
        }, [])
        return field
    }

    function isCellSolved(cell) {
        for (let i = 1; i <= Math.trunc(fieldRows.length / cellLength) * cellLength; i++) {

            if (!cell.some(row => row.includes(i.toString()))) {
                return false

            }
        }
        return true
    }

    function isSolved() {
        const checkCells = getCells().every(column => {
            return column.every(cell => {
                cell = cell.map(element => element.map(el => el.value))
                return isCellSolved(cell)
            })
        })
        const cols = []
        const checkRows = fieldRows.every(row => {
            row = Array.from(row.querySelectorAll("td > input"))
            row = row.reduce((p, n) => {
                p.push(n.value);
                return p
            }, [])
            if (!cols.length) cols.push(...Array(row.length).fill(1).map(() => []))
            row.forEach((v, idx) => cols[idx].push(v))
            return isCellSolved(row)
        })
        const checkCols = cols.every(col => {
            return isCellSolved(col)
        })
        return [checkCells, checkRows, checkCols].every(a => a)
    }

    function solutionCheck() {
        const solved = isSolved()
        if (solved) {
            tableElement.style.border = "2px solid green"
            pElement.textContent = "You solve it! Congratulations!"
            pElement.style.color = "green"
        } else {
            tableElement.style.border = "2px solid red"
            pElement.textContent = "NOP! You are not done yet..."
            pElement.style.color = "red"
        }
    }

    function clear() {
        tableElement.style.border = "none"
        pElement.textContent = ""
        getCells().forEach(column => {
            column.forEach(cell => {
                cell.forEach(row => {
                    row.forEach(inp => {
                        inp.value = ""
                    })
                })
            })
        })
    }

    this.sudokuPopulate = function (arr) {
        const fields = Array.from(document.querySelectorAll("table tbody tr td input"))
        for (let i = 0; i < arr.length; i++) {
            fields[i].value = arr[i]
        }
    }

}