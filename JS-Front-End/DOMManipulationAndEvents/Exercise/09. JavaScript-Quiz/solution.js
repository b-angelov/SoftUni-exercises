function solve() {
    const correctAnswerLst = [0, 1, 0];
    const answerSections = Array.from(document.querySelectorAll("#quizzie section"));
    const resultUl = document.querySelector("#quizzie > ul:last-of-type")
    let activeSectionIdx = 0
    let correctAnswers = 0
    handleAnswer()

    function handleAnswer() {
        const section = answerSections[activeSectionIdx]
        const answers = Array.from(section.querySelectorAll("ul li.quiz-answer"))
        section.style.display = 'block'

        answers.forEach((button, idx) => {
            if (idx === correctAnswerLst[activeSectionIdx]) {
                button.addEventListener("click", () => {correctAnswers++;nextAnswer()})
            } else {
                button.addEventListener("click", nextAnswer)
            }
        })

    }

    function nextAnswer() {
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

}
