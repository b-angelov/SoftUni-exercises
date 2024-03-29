function create(words) {

   const divContainer = document.getElementById("content")
   divContainer.addEventListener("click",reveal)
   words.forEach(createDiv)

   const toggleVisibility = (element)=> element.style.display = element.style.display === "none"?"block":"none"

   function createDiv(string){
      const divElement = document.createElement("div")
      const innerParagraph = document.createElement("p")
      divElement.appendChild(innerParagraph)
      innerParagraph.textContent = string
      innerParagraph.style.display = "none"
      divContainer.appendChild(divElement)
   }

   function reveal(event){
      let target = event.target
      while (target.tagName !== "DIV") {
         target = target.parentElement
      }
      toggleVisibility(target.querySelector("p"))
   }


}