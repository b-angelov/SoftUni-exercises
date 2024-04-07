function lockedProfile() {
    const profileTemplate = document.querySelector("div.profile")
    const mainElement = document.querySelector("main#main")
    const baseUrl = "http://localhost:3030/jsonstore/advanced/profiles"
    window.addEventListener("load",loadProfiles)
    profileTemplate.remove()
    mainElement.addEventListener("click",e=>{
        if(e.target.tagName !== "BUTTON") return
        const parent = e.target.parentElement
        const locked = parent.querySelector("input[type=radio]:checked").value === "lock"
        if(!locked){
            e.target.textContent = e.target.textContent === "Show more"?"Hide it":"Show more"
            const hiddenContent = parent.querySelector("div")
            hiddenContent.style.display = e.target.textContent === "Show more"?"none":"block"
        }
    })

    function loadProfiles(){
        fetch(baseUrl)
            .then(response=>response.json())
            .then(response=>{
                const profiles = Object.values(response).map((item,idx)=>{
                    idx++
                    const newProfile = profileTemplate.cloneNode(true)
                    newProfile.querySelector("div").style.display = "none"
                    const [usernameEl,emailEl,ageEl] = newProfile.querySelectorAll("input[type=text],input[type=email]")
                    Array.from(newProfile.querySelectorAll("input[type=radio]")).forEach(el=>el.name = `user${idx}Locked`)
                    newProfile.querySelector("input[name=user1Username]").name = `user${idx}Username`
                    newProfile.querySelector("div[class=user1Username]").id = `user${idx}HiddenFields`
                    newProfile.querySelector("input[type=email]").name = `user${idx}Email`
                    const age = newProfile.querySelector("input[name=user1Age]")
                    age.name = `user${idx}Age`
                    age.type = `email`
                    usernameEl.value = item.username
                    emailEl.value = item.email
                    ageEl.value = item.age
                    mainElement.appendChild(newProfile)
                })
            })
    }
}