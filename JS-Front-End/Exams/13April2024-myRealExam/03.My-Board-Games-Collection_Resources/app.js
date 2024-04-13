
function logicHandler(){
    const baseUrl = "http://localhost:3030/jsonstore/games"
    const [gameNameEl, typeEl, playersEl, addGameButton, editGameButton] = document.querySelectorAll("#form input, #form button")
    const loadGamesButton = document.querySelector("#load-games")
    const boardGameEl = document.querySelector("#games-list")
    const templateItem = boardGameEl.querySelector(":scope > .board-game")
    templateItem.remove()

    loadGamesButton.addEventListener("click",loadItems)
    addGameButton.addEventListener("click",e=>addGame())

    function createItem(title,player,type,itemId){
        const item = templateItem.cloneNode(true)
        const [titleEl,playersEl,typeEl,addButton,editButton] = item.querySelectorAll("p,button")
        titleEl.textContent = title
        playersEl.textContent = player
        typeEl.textContent = type
        addButton.addEventListener("click",e=>{change(e,title,player,type,itemId)})
        editButton.addEventListener("click",e=>{del(e,itemId)})
        boardGameEl.appendChild(item)
    }

    async function loadItems(){
        boardGameEl.innerHTML = ""
        let items = await fetch(baseUrl)
        items =  await items.json()
        Object.values(items).forEach(item=>{
            createItem(
                item.name,
                item.players,
                item.type,
                item._id
            )
        })
    }

    async function addGame(gameId){
        let url = baseUrl
        const body = {}
        let method = "POST"
        if (gameId){
            url = `${url}/${gameId}`
            body._id = gameId
            method = "PUT"
        }
        body.name = gameNameEl.value
        body.type = typeEl.value
        body.players = playersEl.value
        await fetch(url,{
            method,
            "content-type":"application/json",
            body:JSON.stringify(body)
        })
        loadItems()
        setFields()
    }

    function setFields(name="",type="",players=""){
        gameNameEl.value = name
        typeEl.value = type
        playersEl.value = players
    }

    function change(e,title,player,type,itemId){
        setFields(title,type,player)
        e.target.parentElement.parentElement.remove()
        addGameButton.setAttribute("disabled","disabled")
        editGameButton.removeAttribute("disabled")
        editGameButton.addEventListener("click",async e=>{
            await addGame(itemId)
            editGameButton.setAttribute("disabled","disabled")
            addGameButton.removeAttribute("disabled")
        },{once:true})
    }
    async function del(e,gameId){
        await fetch(`${baseUrl}/${gameId}`,{
            method: "DELETE"
        })
        loadItems()
    }
}

logicHandler()