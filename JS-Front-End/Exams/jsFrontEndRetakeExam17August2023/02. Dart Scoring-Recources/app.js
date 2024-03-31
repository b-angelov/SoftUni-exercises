window.addEventListener("load", solve);

function solve() {
    const [player, score, round, addButton] = Array.from(document.querySelectorAll("#form-container form input,#form-container form button"))
    const sureList = document.querySelector("#score-container ul#sure-list")
    const scoreBoardList = document.querySelector("#players-container ul#scoreboard-list")
    const fieldList = [player,score,round]
    const clearButton = scoreBoardList.nextElementSibling
    addButton.addEventListener("click", addToSureList)

    function addToSureList(){
        const li = document.createElement("li")
        const article = document.createElement("article")
        li.appendChild(article)
        const newElements = []
        li.className = "dart-item"

        fieldList.forEach(element=>{
            const pElement = document.createElement("p")
            newElements.push(pElement)
            pElement.textContent = element.value
            article.appendChild(pElement)
        });

        (["edit","ok"]).forEach(el=>{
            const button = document.createElement("button")
            button.classList.add("btn",el)
            button.textContent = el
            button.addEventListener("click",buttonActions[el])
            li.appendChild(button)
        })

        fieldList.forEach(el=>{
            el.value = ""
        })

        const [score,round] = newElements.slice(1)
        score.textContent = `Score: ${score.textContent}`
        round.textContent = `Round: ${round.textContent}`
        sureList.appendChild(li)
        addButton.setAttribute("disabled","disabled")

    }

    const buttonActions = {
        edit(event){
            const main = event.target.parentElement
            main.remove()
            let [name,scr,rnd] = Array.from(main.querySelectorAll("p")).map(el=>el.textContent);
            [scr, rnd] = [scr,rnd].map(val=>Number(val.split(": ")[1]))
            player.value = name
            score.value = scr
            round.value = rnd
            addButton.removeAttribute("disabled")
        },
        ok(event){
            const main = event.target.parentElement
            Array.from(main.querySelectorAll("button")).forEach(el=>el.remove())
            scoreBoardList.appendChild(main)
            addButton.removeAttribute("disabled")
        },
        clear(event){
            scoreBoardList.innerHTML = ""
        }
    }
    clearButton.addEventListener("click",buttonActions["clear"])

}
  