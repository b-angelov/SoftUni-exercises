window.addEventListener("load", solve);

function solve() {
    const [typeElement, ageElement, genderElement, adoptButton] = document.querySelectorAll("#adopt-pet form input, #adopt-pet form select,#adopt-pet form button")
    const [adoptionInfoElement,adoptedListElement] = document.querySelectorAll("#pet-info #adoption-info,#pet-info #adopted-list")
    adoptButton.addEventListener("click", e=>{
        e.preventDefault()
        createElement()
    })

    function createElement(){
        const fields = [typeElement,ageElement,genderElement].map(el=>el.value)
        if (!fields.every(el=>el)) return
        const [type,age,gender] = fields

        const elements = Object.entries({
            main:{tag:"li",options:{}},
            article:{tag:"article",options:{}},
            type:{tag:"p",options:{textContent:`Pet:${type}`}},
            age:{tag:"p",options:{textContent:`Age:${age}`}},
            gender:{tag:"p",options:{textContent:`Gender:${gender}`}},
            buttons:{tag:"div",options:{className:"buttons"}},
            editButton:{tag:"button",options:{textContent:"Edit",className:"edit-btn"}},
            doneButton:{tag:"button",options:{textContent:"Done",className:"done-btn"}},
            clearButton:{tag:"button",options:{textContent:"Clear",className:"clear-btn"}},
        }).reduce((prev,[name,{tag,options}])=>{
            prev[name] = Object.assign(document.createElement(tag),options)
            return prev
        },{})
        elements.main.appendChild(elements.article)
        elements.main.appendChild(elements.buttons)
        elements.article.appendChild(elements.type)
        elements.article.appendChild(elements.gender)
        elements.article.appendChild(elements.age)
        elements.buttons.appendChild(elements.editButton)
        elements.buttons.appendChild(elements.doneButton)
        adoptionInfoElement.appendChild(elements.main)
        setFields()
        elements.editButton.addEventListener("click",e=>{
            elements.main.remove()
            setFields(type,age,gender)
        })
        elements.doneButton.addEventListener("click",e=>{
            elements.buttons.remove()
            elements.main.appendChild(elements.clearButton)
            adoptedListElement.appendChild(elements.main)
            elements.clearButton.addEventListener("click",e=>{
                elements.main.remove()
            })
        })
    }

    function setFields(type="",age="",gender=""){
        [typeElement.value, ageElement.value, genderElement.value] = [type,age,gender]
    }
}
  