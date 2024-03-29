function lockedProfile() {
    const mainElement = document.querySelector("main#main")
    mainElement.addEventListener("click",showMore)

    function showMore(event){
        if(event.target.tagName !== "BUTTON") return
        let locked = event.target.parentElement.querySelector("input[type='radio']:checked").value
        locked = locked === "lock"
        if(locked) return
        event.target.textContent = event.target.textContent === "Show more"?"Hide it":"Show more"
        const hiddenContentElement = event.target.previousElementSibling
        hiddenContentElement.style.display = event.target.textContent === "Hide it"?"block":"none"
    }
}