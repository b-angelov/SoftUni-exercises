window.addEventListener('load', solve);

function solve() {
    const [genreField,nameField,authorField,dateField,addButton] = document.querySelectorAll("#append-song form input,#append-song form button")
    const [allHitsContainer, savedHitsContainer, totalLikesElement] = document.querySelectorAll("#all-hits .all-hits-container,#saved-hits .saved-container,#total-likes p")

    addButton.addEventListener("click", e=>{e.preventDefault(); collectSong()})

    function updateLikes(){
        const likes = totalLikesElement.textContent.match(/\d+/)
        totalLikesElement.textContent = totalLikesElement.textContent.replace(/\d+/,Number(likes)+1)
    }

    function collectSong(){
        const fields = [genreField,nameField,authorField,dateField].map(field=>field.value)
        if(!fields.every(el=>el)) return
        setFields()
        const [genre,name,author,date] = fields
        const elements = Object.entries({
            main:{tag:"div",options:{className:"hits-info"}},
            image:{tag:"img",options:{src:"./static/img/img.png"}},
            genre:{tag:"h2",options:{textContent:`Genre: ${genre}`}},
            name:{tag:"h2",options:{textContent:`Name: ${name}`}},
            author:{tag:"h2",options:{textContent:`Author: ${author}`}},
            date:{tag:"h3",options:{textContent:`Date: ${date}`}},
            saveButton:{tag:"button",options:{className:"save-btn",textContent:"Save song"}},
            likeButton:{tag:"button",options:{className:"like-btn",textContent:"Like song"}},
            deleteButton:{tag:"button",options:{className:"delete-btn",textContent:"Delete"}},
        }).reduce((prev,[name,{tag,options}])=>{
            prev[name] = Object.assign(document.createElement(tag),options)
            return prev
        },{})
        elements.main.appendChild(elements.image)
        elements.main.appendChild(elements.genre)
        elements.main.appendChild(elements.name)
        elements.main.appendChild(elements.author)
        elements.main.appendChild(elements.date)
        elements.main.appendChild(elements.saveButton)
        elements.main.appendChild(elements.likeButton)
        elements.main.appendChild(elements.deleteButton)
        allHitsContainer.appendChild(elements.main)
        elements.likeButton.addEventListener("click",e=> {
            updateLikes()
            elements.likeButton.setAttribute("disabled","disabled")
        })
        elements.saveButton.addEventListener("click",e=>{
            savedHitsContainer.appendChild(elements.main)
            elements.saveButton.remove()
            elements.likeButton.remove()
        })
        elements.deleteButton.addEventListener("click",e=>{elements.main.remove()})
    }

    function setFields(genre="",name="",author="",date=""){
        [genreField.value,nameField.value,authorField.value,dateField.value] = [genre,name,author,date]
    }
}