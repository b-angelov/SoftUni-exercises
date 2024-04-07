function solution() {

    const baseUrl = "http://localhost:3030/jsonstore/advanced/articles"
    const mainElement = document.querySelector("section#main")
    let mainTemplate = document.createElement("p")
    mainTemplate.innerHTML = mainElement.childNodes[1].textContent.replace(/<!--\s*|\s*-->|^\s*|\s*$|\n*/gm,"")
    mainTemplate = mainTemplate.querySelector(":scope > div")
    loadArticles()

    mainElement.addEventListener("click",e=>{
        if(e.target.tagName !== "BUTTON") return
        const mainParent = e.target.parentElement.parentElement
        const extraEl = mainParent.querySelector("div.extra")
        e.target.textContent = e.target.textContent === "More"?"Less":"More"
        extraEl.style.display = e.target.textContent === "More"?"none":"block"
    })

    async function articlesListing() {
        let res = await fetch(`${baseUrl}/list`)
        return await res.json()
    }

    async function loadArticles(){
        mainElement.innerHTML = ""
        const articles = await articlesListing()
        articles.forEach(article=>{
            const newArticle = mainTemplate.cloneNode(true)
            const [titleEl,buttonEl,extraEl] = newArticle.querySelectorAll("span,button,div.extra")
            titleEl.textContent = article.title
            buttonEl.id = article._id
            mainElement.appendChild(newArticle)
            const articleContent = async () => {
                let articleIn = await fetch(`${baseUrl}/details/${article._id}`)
                articleIn = await articleIn.json()
                const paragraph = extraEl.querySelector("p")
                paragraph.textContent = articleIn.content
            }
            articleContent()
        })
    }





}

solution()