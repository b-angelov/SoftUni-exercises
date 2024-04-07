function attachEvents() {
    const [loadPostsButton, postsSelectElement,viewPostButton,commentsUl] = Array.from(document.querySelectorAll('button,select,ul'));
    const baseUrl = "http://localhost:3030/jsonstore/blog"
    let articlesData ={}

    loadPostsButton.addEventListener('click', (e) => {
        fetch(`${baseUrl}/posts`)
            .then(response=>response.json())
            .then(response=> {
                articlesData = response
                loadOptions(response)
            })
            .catch(error)
    })

    viewPostButton.addEventListener("click",(element)=>{
        const titleEl = document.querySelector("#post-title")
        const contentEl = document.querySelector("#post-body");
        const {body,title} = articlesData[postsSelectElement.value]
        titleEl.textContent = title
        titleEl.className = "post-title"
        contentEl.textContent = body
        contentEl.className = "post-body"
        Array.from(commentsUl.querySelectorAll("li")).forEach(el=>el.remove())
        fetch(`${baseUrl}/comments`)
            .then(response=>response.json())
            .then(response=>Object.entries(response).filter(([id,data])=>data.postId === postsSelectElement.value))
            .then(response=> {
                viewPost(response,response[0][1].postId)
            })
            .catch(error)
    })

    function loadOptions(data){
        Array.from(postsSelectElement.querySelectorAll("option")).forEach(el=>el.remove())
        const fragment = document.createDocumentFragment()
        Object.entries(data).forEach(([id,dat])=>{
            const newOpt = document.createElement("option")
            fragment.appendChild(newOpt)
            newOpt.value = id
            newOpt.textContent = dat.title
        })
        postsSelectElement.appendChild(fragment)
    }

    function viewPost(data,postId){


        data.forEach(([id,item])=>{
            const newLi = document.createElement("li")
            commentsUl.appendChild(newLi)
            newLi.id = id
            newLi.textContent = item.text
        })
    }

    function error(err){console.log(err)}
}

attachEvents();