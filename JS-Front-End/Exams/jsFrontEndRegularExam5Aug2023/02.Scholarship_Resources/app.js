window.addEventListener("load", solve);

function solve() {

    const previewElement = document.querySelector("#preview-list")
    const candidatesElement = document.querySelector("#candidates-container #candidates-list")
    const [nameInput,universityInput,scoreInput,nextButton] = document.querySelectorAll("#newApply input,#newApply button")
    const applicationContainer = document.querySelector("ul#preview-list")

    nextButton.addEventListener("click",e=>{
        const [name,university,score] = [nameInput.value,universityInput.value,scoreInput.value]
        if(![name,university,score].every(val=>val))return
        newElement(name,university,score)
        nextButton.setAttribute("disabled","disabled")
        nameInput.value = ""
        universityInput.value = ""
        scoreInput.value = ""
    })

    function newElement(name, university, score) {
        const liContainer = document.createElement("li")
        liContainer.className = "application"
        const newArticle = document.createElement("article")
        liContainer.appendChild(newArticle)
        const h4El = document.createElement("h4")
        newArticle.appendChild(h4El)
        h4El.textContent = name
        const p1El = document.createElement("p")
        newArticle.appendChild(p1El)
        const p2El = document.createElement("p")
        newArticle.appendChild(p2El)
        p1El.textContent = `University: ${university}`
        p2El.textContent = `Score: ${score}`
        p1El.setAttribute("data-university", university)
        p2El.setAttribute("data-score", score)
        h4El.setAttribute("data-name", name)
        const editButton = document.createElement("button")
        editButton.classList.add("action-btn", "edit")
        editButton.textContent = "edit"
        const applyButton = document.createElement("button")
        applyButton.textContent = "apply"
        applyButton.classList.add("action-btn", "apply")
        liContainer.appendChild(editButton)
        liContainer.appendChild(applyButton)
        previewElement.appendChild(liContainer)
    }

    applicationContainer.addEventListener("click",e=>{
        if (e.target.tagName !== "BUTTON") return
        console.log("here")
        if(e.target.classList.contains("edit")){
            edit(e)
        }else {
            apply(e)
        }
    })

    function apply(e){
        const main = e.target.parentElement
        main.remove()
        Array.from(main.querySelectorAll("button")).forEach(el=>el.remove())
        candidatesElement.appendChild(main)
        nextButton.removeAttribute("disabled")
    }
    function edit(e){
        const [name,university,score] = Array.from(e.target.parentElement.querySelectorAll("h4,p"))
        nameInput.value = name.getAttribute("data-name")
        universityInput.value = university.getAttribute("data-university")
        scoreInput.value = score.getAttribute("data-score")
        e.target.parentElement.remove()
        nextButton.removeAttribute("disabled")
    }


}
  