function logics() {
    const repositoryApiUrl = "https://api.github.com/repos/b-angelov/softuni-exercises/contents"
    const navigationElement = document.querySelector("article.navigation .main-nav")
    let mainDir = []

    const availableLanguages = {
        python: {
            fontIconGlyph: "",
            fontIconClass:"fa-brands fa-python"
        },
        js: {
            fontIconGlyph: "",
            fontIconClass:"fa-brands fa-js"
        },
        javascript: ["js"],
        html: {
            fontIconGlyph: "",
            fontIconClass:"fa-brands fa-html5"
        },
        css: {
            fontIconGlyph: "",
            fontIconClass:"fa-brands fa-css3-alt"
        },
        db: {
            fontIconGlyph: "",
            fontIconClass:"fa-solid fa-database"
        },
        sql: {
            fontIconGlyph: "",
            fontIconClass:"fa-solid fa-database"
        },
        postgre: {
            fontIconGlyph: "",
            fontIconClass:"fa-solid fa-database"
        }
    }

    async function getDirectoryTree(subPath = "") {
        dirTree = await fetch(`${repositoryApiUrl}/${subPath}`)
        dirTree = await dirTree.json()
        return dirTree
    }

    function mainNavItem(language){
        console.log(language)
        const elements = Object.entries({
            item:{tag:"li",options:{className:`language ${language.toLowerCase()}`}},
            figure:{tag:"figure",options:{}},
            img:{tag:"i",options:{className:`language-icon ${language}-icon ${availableLanguages[language].fontIconClass}`}}
        }).reduce((prev,[name,{tag,options}])=>{
            prev[name] = Object.assign(document.createElement(tag),options)
            return prev
        },{})

        elements.item.append(elements.figure)
        elements.figure.append(elements.img)
        navigationElement.append(elements.item)
        elements.item.addEventListener("mouseenter",e=>elements.figure.classList.add("hover-zoom"))
        elements.item.addEventListener("mouseleave",e=>elements.figure.classList.remove("hover-zoom"))
    }

    async function loadMainNav(){
        mainDir = await getDirectoryTree()
        const menuObj = {}
        mainDir.forEach(item=>{
            const itemType = item.name.match(/python|js|javascript|css|sql/gmi)
            console.log(itemType)
            if (itemType && itemType.length){
                const type = itemType[0].toLowerCase()
                if(!menuObj.hasOwnProperty(type)) menuObj[type] = []
                menuObj[type].push(item)
            }
        })
        mainDir = menuObj
        Object.keys(mainDir).forEach(language=>mainNavItem(language))
    }

    console.log(mainDir)
    loadMainNav()
}

logics()