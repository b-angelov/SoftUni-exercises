function loadRepos() {
   const uri = `https://api.github.com/users/testnakov/repos`
   const resultElement = document.querySelector("#res")
   fetch(uri)
       .then((response=>response.json()))
       .then(display)
       .catch(error)

   function display(response){
      res.textContent = JSON.stringify(response)
   }

   function error(error){
      console.log(error)
   }
}