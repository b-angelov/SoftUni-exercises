function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      const textElement = document.getElementById("searchField")
      const trElements = document.querySelectorAll("table.container tbody tr")
      const set = element => element.classList.add("select")
      const clear = element => element.classList.remove("select")

      Array.from(trElements).forEach(element=> {
         Array.from(element.children).every(li=>{
            if (li.textContent.toLowerCase().includes(textElement.value.toLowerCase())){
               set(element)
               return false
            }else{
               clear(element)
               return true
            }
         })
      })

   }
}