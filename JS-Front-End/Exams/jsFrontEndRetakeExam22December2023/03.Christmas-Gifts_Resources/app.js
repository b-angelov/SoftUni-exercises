function solutionHandler() {
    const baseUrl = "http://localhost:3030/jsonstore/gifts"
    const [giftInput, personInput, priceInput, addPresentButton, editPresentButton] = document.querySelectorAll("#form-section #form form input, #form-section #btn-container button")
    const giftsStock = document.querySelector("#gift-list")
    const presentTemplate = giftsStock.querySelector(".gift-sock")
    giftsStock.innerHTML = ""
    const presentsContainer = document.querySelector("#presents")
    const loadPresentsButton = presentsContainer.querySelector(":scope > button")
    const [templateGift, templatePersonName, templatePrice] = presentTemplate.querySelectorAll(".content p")

    loadPresentsButton.addEventListener("click", loadPresents)
    addPresentButton.addEventListener("click",addPresent)
    editPresentButton.addEventListener("click",editPresent)

    async function addPresent(){
        if (![giftInput.value,personInput.value,priceInput.value].every(val=>val)) return
        await fetch(baseUrl,{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({
              gift:giftInput.value,
              for:personInput.value,
              price:priceInput.value,
            })
        })

        giftInput.value = ""
        personInput.value = ""
        priceInput.value = ""
        loadPresents()
    }

    async function editPresent(){}

    async function loadPresents(){
        giftsStock.innerHTML = ""
        let presentsObj = await fetch(baseUrl)
        presentsObj = await presentsObj.json()
        Object.entries(presentsObj).forEach(([id,present])=>{
            templateGift.textContent = present.gift
            templatePersonName.textContent = present.for
            templatePrice.textContent = present.price
            const presentId = present._id
            const newPresent = presentTemplate.cloneNode(true)
            const [templateChangeButton, templateDeleteButton] = newPresent.querySelectorAll(".buttons-container button")
            templateChangeButton.addEventListener("click", (e) => changePresent(e,presentId))
            templateDeleteButton.addEventListener("click", (e) => deletePresent(e,presentId))
            giftsStock.appendChild(newPresent)
        })
    }


    function changePresent(e,presentId){
        editPresentButton.removeAttribute("disabled")
        addPresentButton.setAttribute("disabled","disabled")
        const containerElement = e.target.parentElement.parentElement
        containerElement.remove()
        const [gift,person,price] = Array.from(containerElement.querySelectorAll(".content p")).map(element=>element.textContent)
        giftInput.value = gift
        personInput.value = person
        priceInput.value = price
        editPresentButton.addEventListener("click",async (e)=>{
            // e.target.removeEventListener("click",ev)
            addPresentButton.removeAttribute("disabled")
            editPresentButton.setAttribute("disabled","disabled")
            await fetch(`${baseUrl}/${presentId}`,{
                method:"PUT",
                headers:{
                    "Content-Type":"application/json"
                },
                body:JSON.stringify({
                    gift:giftInput.value,
                    for:personInput.value,
                    price:priceInput.value,
                    _id:presentId
                })
            })
            giftInput.value = ""
            personInput.value = ""
            priceInput.value = ""
            loadPresents()

        },{once:true})

    }

    async function deletePresent(e,presentId){
        e.target.parentElement.parentElement.remove()
        await fetch(`${baseUrl}/${presentId}`,{
            method:"DELETE"
        })
        loadPresents()
    }
}

solutionHandler()