function logics(){
    const repositoryApiUrl = "https://api.github.com.repos/b-angelov/softuni-exercises/contents"

    async function getDirectoryTree(subPath=""){
        dirTree = await fetch(`${repositoryApiUrl}/${subPath}`)
        dirTree = await dirTree.json()
        console.log(dirTree)
    }
}
logics()