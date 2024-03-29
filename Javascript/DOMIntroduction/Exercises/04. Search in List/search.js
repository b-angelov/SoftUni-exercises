function search() {
    const clear = element => {
        element.style.textDecoration = 'none';
        element.style.fontWeight = 'normal'
    }
    const set = element => {
        element.style.textDecoration = 'underline';
        element.style.fontWeight = 'bold'
    }
    const searchText  = document.getElementById("searchText")
    const elements = document.querySelectorAll("#towns li")
    const result = document.getElementById("result")
    let matches = 0

    Array.from(elements).forEach(element=> {
        if(element.textContent.toLowerCase().includes(searchText.value.toLowerCase())) {
            set(element)
            matches++
        }else{
            clear(element)
        }
    })
    result.textContent = `${matches} matches found`

}
