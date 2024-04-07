function attachEvents() {
    const [authorElement,contentElement,submitButton,refreshButton] = Array.from(document.querySelectorAll("input"))
    const resultTextArea = document.querySelector("textarea")
    const url = "http://localhost:3030/jsonstore/messenger"

    submitButton.addEventListener("click",element=>{
        fetch(url,{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({
                author:authorElement.value,
                content:contentElement.value
            })
        })
            .then(response=>{
                authorElement.value = ""
                contentElement.value = ""
            })
            .catch(error)
    })

    refreshButton.addEventListener("click",event=>{
        fetch(url)
            .then(response=>response.json())
            .then(response=>{
                resultTextArea.value = ""
                const elements = []
                Object.values(response).forEach(element=>{
                    elements.push(`${element.author}: ${element.content}`)
                })
                resultTextArea.value += elements.join("\n")
            })
            .catch(error)
    })

    const error = error=> console.log(error);
}

attachEvents();