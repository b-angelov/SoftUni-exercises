/*Creating function for task name: solve*/

function solve(students) {
    students = students.map(element=> {
        const elements = {}
        element.split(", ").forEach(el=>{
            const [key,value] = el.split(": ")
            elements[key] = value
        })
        return elements
    })
        .filter(element=>Number(element['Graduated with an average score']) >= 3)
    students = students.reduce((prev,element)=>{
        if(!prev.hasOwnProperty(element.Grade)) prev[element.Grade] = []
        prev[element.Grade].push(element)
        return prev
    },{})
    Object.entries(students).forEach(([grade,students])=> {
        console.log(`${Number(grade)+1} Grade`)
        console.log("List of students:", Array(students.length).fill().map((element,idx)=>students[idx]["Student name"]).join(", "))
        console.log("Average annual score from last year:",(Array(students.length).fill().map((el,idx)=>students[idx]['Graduated with an average score']).reduce((a,b)=>Number(a)+Number(b))/students.length).toFixed(2))
        console.log()
    })
}

solve([
        "Student name: Mark, Grade: 8, Graduated with an average score: 4.75",
        "Student name: Ethan, Grade: 9, Graduated with an average score: 5.66",
        "Student name: George, Grade: 8, Graduated with an average score: 2.83",
        "Student name: Steven, Grade: 10, Graduated with an average score: 4.20",
        "Student name: Joey, Grade: 9, Graduated with an average score: 4.90",
        "Student name: Angus, Grade: 11, Graduated with an average score: 2.90",
        "Student name: Bob, Grade: 11, Graduated with an average score: 5.15",
        "Student name: Daryl, Grade: 8, Graduated with an average score: 5.95",
        "Student name: Bill, Grade: 9, Graduated with an average score: 6.00",
        "Student name: Philip, Grade: 10, Graduated with an average score: 5.05",
        "Student name: Peter, Grade: 11, Graduated with an average score: 4.88",
        "Student name: Gavin, Grade: 10, Graduated with an average score: 4.00"
    ]
)