function logics() {
    const repositoryApiUrl = "https://api.github.com/repos/b-angelov/softuni-exercises/contents"
    const navigationElement = document.querySelector("article.navigation .navigation-main")
    const mainDir = getDirectoryTree()

    const availableLanguages = {
        python: {
            fontIcon: "",
        },
        js: {
            fontIcon: ""
        },
        javascript: ["js"],
        html: {
            fontIcon: ""
        },
        css: {
            fontIcon: ""
        },
        db: {
            fontIcon: ""
        },
        sql: {
            fontIcon: ""
        },
        postgre: {
            fontIcon: ""
        }
    }

    async function getDirectoryTree(subPath = "") {
        dirTree = await fetch(`${repositoryApiUrl}/${subPath}`)
        dirTree = await dirTree.json()
    }

    function mainNav(language){
        const elements = Object.entries({
            item:{tag:"li",options:{className:`language ${language.toLowerCase()}`}},
            img:{tag:"i",options:{className:`language-icon ${language}-icon`,textContent:availableLanguages[language].fontIcon}}
        }).reduce((prev,[name,{tag,options}])=>{
            prev[name] = Object.assign(document.createElement(tag),options)
            return prev
        },{})

        elements.item.append(elements.img)
        navigationElement.append(elements.item)
    }

    function loadMainNav(){
        mainDir.forEach(item=>{
            const itemType = item.name.match(/python|js|javascript|css|sql/gmi)
            console.log(itemType)
        })
    }

    console.log(mainDir)
    loadMainNav()
}

logics()