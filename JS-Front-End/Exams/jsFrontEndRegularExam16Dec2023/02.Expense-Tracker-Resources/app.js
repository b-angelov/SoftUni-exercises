window.addEventListener("load", solve);

function solve(){
    const [expense,amount,date,addButton] = document.querySelectorAll("#form-container .expense-content input,#form-container .expense-content button")
    const previewList = document.querySelector("#right-container #preview ul")
    const expenseList = document.querySelector("#expenses #expenses-list")
    const deleteButton = document.querySelector("#expenses button.delete")

    addButton.addEventListener("click",(event)=>{
        const options = [expense, amount, date]
        if(options.map(value=>value.value).every(option=>option)){
            createPreview(options)
        }
    })

    function resetFields(options){
        options.forEach(option=>option.value = '')
    }

    function createPreview(fields){
        const li = document.createElement("li")
        const article = document.createElement("article")
        const buttonsDiv = document.createElement("div")

        li.appendChild(article)
        li.appendChild(buttonsDiv)

        li.classList.add("expense-item")
        buttonsDiv.className = "buttons"

        fields.forEach(field=>{
            const paragraph = document.createElement("p")
            let value = field.id === "expense"?"type":field.id
            value = value[0].toUpperCase() + value.slice(1)
            paragraph.textContent = `${value}: ${field.value}${field.id === "amount"?"$":""}`
            article.appendChild(paragraph)
        });

        (["edit", "ok"]).forEach(name=>{
            const button = document.createElement("button")
            button.classList.add("btn",name)
            button.textContent = name
            button.addEventListener("click",actions[name])
            buttonsDiv.appendChild(button)
        })

        previewList.appendChild(li)
        resetFields(fields)
        addButton.disabled = 'disabled'

    }

    const actions = {
        "edit":(event)=>{
            const main = event.target.parentElement.parentElement
            const fields = Array.from(main.querySelectorAll("article p"))
            const options = [expense, amount, date]
            amount.value = 5
            fields.forEach((field,idx)=>{
                options[idx].value = field.textContent.split(": ")[1].replace(/\$$/,"")
            })
            addButton.removeAttribute("disabled")
            main.remove()
        },
        "ok":(event)=>{
            const main = event.target.parentElement.parentElement
            main.querySelector("div").remove()
            expenseList.appendChild(main)
            addButton.removeAttribute("disabled")
        },
    }

    deleteButton.addEventListener("click",(event)=>{
        let el = event.target.parentElement.querySelector("ul")
        while(el.children.length){
            el.removeChild(el.lastChild)
        }
        resetFields([expense, amount, date])
        el = document.querySelector("#preview-list")
        while(el.children.length){
            el.removeChild(el.lastChild)
        }
    })

}