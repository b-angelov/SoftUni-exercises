function solve() {
    const correctAnswerLst = [];

    // Original question list
    // const questionList = [["Which event occurs when the user clicks on an HTML element?",["onclick","onmouseclick"],0],["Which function converting JSON to string?",["JSON.toString()","JSON.stringify()"],1],["What is DOM?",["A programming API for HTML and XML documents","The DOM is your source HTML"],0]]

    // Chatgpt generated 30 question list
    var questionList = [
        ["What is the result of 2 + 2?", ["3", "4"], 1],
        ["Which keyword is used to declare a variable in JavaScript?", ["var", "let"], 0],
        ["What is the purpose of the 'typeof' operator in JavaScript?", ["To determine the type of a variable", "To declare a new variable"], 0],
        ["Which symbol is used for single-line comments in JavaScript?", ["//", "/*"], 0],
        ["What method is used to add an element to the end of an array in JavaScript?", ["push()", "pop()"], 0],
        ["Which loop is used to iterate over the properties of an object in JavaScript?", ["for...in loop", "for loop"], 0],
        ["What does DOM stand for in JavaScript?", ["Document Object Model", "Data Object Model"], 0],
        ["What is the purpose of the 'this' keyword in JavaScript?", ["Refers to the current object", "Declares a new variable"], 0],
        ["Which operator is used to compare both type and value in JavaScript?", ["===", "=="], 0],
        ["What method is used to remove the last element from an array in JavaScript?", ["pop()", "shift()"], 0],
        ["What is the correct way to write an IF statement in JavaScript?", ["if (x == 5) { }", "if x = 5 then { }"], 0],
        ["What is the purpose of the 'NaN' property in JavaScript?", ["Represents 'Not a Number'", "Represents 'Not a Null'"], 0],
        ["Which function is used to convert a string to an integer in JavaScript?", ["parseInt()", "parseFloat()"], 0],
        ["What is the result of typeof typeof 42 in JavaScript?", ["string", "number"], 0],
        ["Which method is used to join the elements of an array into a string in JavaScript?", ["join()", "split()"], 0],
        ["What does AJAX stand for in JavaScript?", ["Asynchronous JavaScript and XML", "Application JavaScript and XML"], 0],
        ["Which function is used to find the index of the first occurrence of a specified value in an array in JavaScript?", ["indexOf()", "lastIndexOf()"], 0],
        ["What is the purpose of the 'event' object in JavaScript?", ["Represents the current event", "Declares a new event"], 0],
        ["Which method is used to execute a function after a specified number of milliseconds in JavaScript?", ["setTimeout()", "setInterval()"], 0],
        ["What is the result of '5' + 3 in JavaScript?", ["'53'", "8"], 0],
        ["Which function is used to round a number to the nearest integer in JavaScript?", ["Math.round()", "Math.floor()"], 0],
        ["What is the purpose of the 'console.log()' method in JavaScript?", ["Outputs a message to the console", "Declares a new variable"], 0],
        ["Which operator is used to assign a value to a variable in JavaScript?", ["=", "=="], 0],
        ["What method is used to sort the elements of an array in JavaScript?", ["sort()", "reverse()"], 0],
        ["What is the purpose of the 'break' statement in JavaScript?", ["Exits a loop or a switch statement", "Continues to the next iteration of a loop"], 0],
        ["What does JSON stand for in JavaScript?", ["JavaScript Object Notation", "JavaScript Object Network"], 0],
        ["Which method is used to add one or more elements to the beginning of an array in JavaScript?", ["unshift()", "push()"], 0],
        ["What is the result of 10 % 3 in JavaScript?", ["1", "0"], 0],
        ["Which function is used to create a copy of an array with all falsy values removed in JavaScript?", ["filter()", "map()"], 0],
        ["What is the purpose of the 'try...catch' statement in JavaScript?", ["Handles errors in code", "Declares a new variable"], 0],
        ["Which method is used to return the characters in a string beginning at the specified location in JavaScript?", ["substring()", "charAt()"], 0]
    ];



    const template = document.querySelector("#quizzie section")
    const quizzie = document.querySelector("#quizzie")
    const resultUl = document.querySelector("#quizzie > ul:last-of-type")

    Array.from(document.querySelectorAll("#quizzie section")).forEach(element=>{
        quizzie.removeChild(element)
    })
    questionList.forEach((q,idx)=>createSection(q,idx))
    quizzie.removeChild(resultUl)
    quizzie.appendChild(resultUl)


    const answerSections = Array.from(document.querySelectorAll("#quizzie section"));
    let activeSectionIdx = 0
    let correctAnswers = 0
    handleAnswer()
    answerSections[0].classList.remove("hidden")
    answerSections[0].style.display = ''

    function handleAnswer() {
        const section = answerSections[activeSectionIdx]
        const answers = Array.from(section.querySelectorAll("ul li.quiz-answer"))
        section.style.display = 'block'

        answers.forEach((button, idx) => {
            if (idx === correctAnswerLst[activeSectionIdx]) {
                button.addEventListener("click", () => {correctAnswers++;nextQuestion()})
            } else {
                button.addEventListener("click", nextQuestion)
            }
        })

    }

    function nextQuestion() {
        answerSections[activeSectionIdx].style.display = "none"
        if(activeSectionIdx === answerSections.length-1){
            showResult()
            return
        }
        activeSectionIdx++
        handleAnswer()
    }

    function showResult(){
        resultUl.style.display = "block"
        const resultElement = resultUl.querySelector("li *")
        resultElement.textContent = correctAnswers === answerSections.length
            ?"You are recognized as top JavaScript fan!"
            :`You have ${correctAnswers} right answers`
    }

    function createSection(values,n){
        const temp = template.cloneNode(true)
        temp.classList.add("hidden")
        const [question,[first,second],correct] = values
        const [h2,p1,p2] = Array.from(temp.querySelectorAll("h2,p"))
        h2.textContent = `Question #${n+1}: ${question}`
        p1.textContent = first
        p2.textContent = second
        correctAnswerLst.push(correct)
        quizzie.appendChild(temp)
    }

}
