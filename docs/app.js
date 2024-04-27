function logics() {
    const repositoryApiUrl = "https://api.github.com/repos/b-angelov/softuni-exercises/contents"
    navigation
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
        console.log(dirTree)
    }

    getDirectoryTree()
}

logics()