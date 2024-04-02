function loadRepos() {
    const user = document.querySelector("#username").value
    const uri = `https://api.github.com/users/${user}/repos`
	const resultUl = document.getElementById("repos")
	const templateLi = resultUl.querySelector("li")
	templateLi.remove()
    fetch(uri)
        .then((response => {
			if(response.status !== 200) throw new Error(response.status)
			return response.json()
		}))
        .then(display)
        .catch(error)

    function display(response) {
		resultUl.innerHTML = ""
		response.forEach(repo=>{
			const newLi = templateLi.cloneNode()
			const aEl = document.createElement("a")
			newLi.appendChild(aEl)
			aEl.href = repo.html_url
			aEl.textContent = repo.full_name
			resultUl.append(newLi)
		})
    }

    function error(error) {
		resultUl.innerHTML = ""
		const li = templateLi.cloneNode()
		li.style.display = "block"
		li.textContent = error
		resultUl.appendChild(li)
    }
}