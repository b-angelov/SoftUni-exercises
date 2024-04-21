window.addEventListener("load", solve);

function solve() {
    const [firstNameField, lastNameField, AgeField, titleField, genreField, storyField, publishButton] = document.querySelectorAll("#main form input, #main form select, #main form textarea");
    const previewList = document.getElementById("preview-list")
    const mainElement = document.getElementById("main")

    publishButton.addEventListener("click",createPublication)

    function createPublication(){
        const fields = [firstNameField, lastNameField, AgeField, titleField, genreField, storyField].map(el=>el.value)
        if(!fields.every(el=>el)) return
        const [firstName,lastName,age,title,genre,story] = fields
        publishButton.setAttribute("disabled","disabled")

        const elements = Object.entries({
            main:{tag:"li",options:{className:"story-info"}},
            article:{tag:"article",options:{}},
            name:{tag:"h4",options:{textContent:`Name: ${firstName} ${lastName}`}},
            age:{tag:"p",options:{textContent: `Age: ${age}`}},
            title:{tag:"p",options:{textContent: `Title: ${title}`}},
            genre:{tag:"p",options:{textContent: `Genre: ${genre}`}},
            text:{tag:"p",options:{textContent: story}},
            saveButton:{tag:"button",options:{textContent: "Save Story", className:"save-btn"}},
            editButton:{tag:"button",options:{textContent: "Edit Story", className:"edit-btn"}},
            deleteButton:{tag:"button",options:{textContent: "Delete Story", className:"delete-btn"}},
        }).reduce((prev,[el,{tag,options}])=>{
            prev[el] = Object.assign(document.createElement(tag),options)
            return prev
        },{})

        elements.main.appendChild(elements.article)
        elements.main.appendChild(elements.saveButton)
        elements.main.appendChild(elements.editButton)
        elements.main.appendChild(elements.deleteButton)
        elements.article.appendChild(elements.name)
        elements.article.appendChild(elements.age)
        elements.article.appendChild(elements.title)
        elements.article.appendChild(elements.genre)
        elements.article.appendChild(elements.text)
        previewList.appendChild(elements.main)
        setFields()

        elements.saveButton.addEventListener("click",e=>{mainElement.innerHTML = "<h1>Your scary story is saved!</h1>"})
        elements.editButton.addEventListener("click",e=>{
            publishButton.removeAttribute("disabled")
            elements.main.remove()
            setFields(firstName,lastName,age,title,genre,story)
        })
        elements.deleteButton.addEventListener("click",e=>{
            publishButton.removeAttribute("disabled")
            elements.main.remove()
        })

    }

    function setFields(firstName="",lastName="",age="",title="",genre="",story=""){
        [firstNameField.value, lastNameField.value, AgeField.value, titleField.value, genreField.value, storyField.value] = [firstName,lastName,age,title,genre,story]
    }

}
