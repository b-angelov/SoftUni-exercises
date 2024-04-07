function attachEvents() {
    const baseUrl = "http://localhost:3030/jsonstore/collections/students"
    const rowTemplate = document.querySelector("thead tr")
    const tableBody = document.querySelector("tbody")
    const [firstName, lastName, facultyNumber, grade, submit] = document.querySelectorAll("input,button")
    window.addEventListener("load", loadStudents)
    const error = error => console.log(error)

    submit.addEventListener("click", event => {
        const student = {
            firstName: firstName.value,
            lastName: lastName.value,
            facultyNumber: facultyNumber.value,
            grade: grade.value,
        }
        if (!Object.values(student).every(val=>val)) return
        console.log(student)
        fetch(baseUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(student)
        })
            .then(response => showStudents({student: student}))
            .then(function () {
                firstName.value = ""
                lastName.value = ""
                facultyNumber.value = ""
                grade.value = ""
            })
            .catch(error)
    })

    function loadStudents() {
        fetch(baseUrl)
            .then(response => response.json())
            .then(showStudents)
            .catch(error)
    }

    function showStudents(studentElements) {
        Object.values(studentElements).forEach(person => {
            const newRow = rowTemplate.cloneNode()
            for (let i = 0; i < rowTemplate.children.length; i++) {
                const td = document.createElement("td")
                newRow.appendChild(td)
            }
            const [firstName, lastName, facultyNumber, grade] = Array.from(newRow.querySelectorAll("td"))
            firstName.textContent = person.firstName
            lastName.textContent = person.lastName
            facultyNumber.textContent = person.facultyNumber
            grade.textContent = person.grade
            newRow.appendChild(firstName)
            newRow.appendChild(lastName)
            newRow.appendChild(facultyNumber)
            newRow.appendChild(grade)
            tableBody.append(newRow)
        })
    }
}

attachEvents();