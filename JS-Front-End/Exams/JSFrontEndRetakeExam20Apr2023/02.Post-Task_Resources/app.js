window.addEventListener("load", solve);

function solve() {
    const [titleEl,categoryEl,contentEl,publishButton] = document.querySelectorAll("#left-container form input, #left-container form textarea,#left-container form button")
    const reviewListEl = document.querySelector("#review-list")
    const publishListEl = document.querySelector("#published-list")
    publishButton.addEventListener("click",e=>{
        e.preventDefault()
        if(![titleEl.value,categoryEl.value,contentEl.value].every(val=>val)) return
        createItem(titleEl.value,categoryEl.value,contentEl.value)
        setFields()
    })

    function createItem(title,category,content){
        const liEl = document.createElement("li")
        const articleEl = document.createElement("article")
        const titleEl = document.createElement("h4")
        const categoryEl = document.createElement("p")
        const contentEl = document.createElement("p")
        const editButton = document.createElement("button")
        const postButton = document.createElement("button")
        liEl.appendChild(articleEl)
        articleEl.appendChild(titleEl)
        articleEl.appendChild(categoryEl)
        articleEl.appendChild(contentEl)
        liEl.appendChild(editButton)
        liEl.appendChild(editButton)
        liEl.appendChild(postButton)
        contentEl.setAttribute("data-value", content)
        titleEl.setAttribute("data-value",title)
        categoryEl.setAttribute("data-value",category)
        categoryEl.style.content = "Category: "
        titleEl.textContent = title
        categoryEl.textContent = `Category: ${category}`
        contentEl.textContent = `Content: ${content}`
        editButton.textContent = "Edit"
        editButton.classList.add("action-btn","edit")
        postButton.classList.add("action-btn","post")
        editButton.addEventListener("click",e=>{
            liEl.remove()
            setFields(title,category,content)
        })
        postButton.addEventListener("click",e=>{
            publishListEl.appendChild(liEl)
            editButton.remove()
            postButton.remove()
        })
        postButton.textContent = "Post"
        liEl.className = "rpost"
        reviewListEl.appendChild(liEl)
    }

    function setFields(title="",category="",content=""){
        titleEl.value = title
        categoryEl.value = category
        contentEl.value = content
    }
  
}