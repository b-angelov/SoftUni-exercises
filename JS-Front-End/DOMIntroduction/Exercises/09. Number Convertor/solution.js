function solve() {

    const convertors = {
        "decimal": {
            "binary": number => Number(number).toString(2),
            "hexadecimal": number => Number(number).toString(16).toUpperCase(),
            "octal": number => Number(number).toString(8).toUpperCase(),
        },
        "binary":{
            "decimal": string => parseInt(string,2),
            "hexadecimal": string => parseInt(string,2).toString(16).toUpperCase(),
            "octal": string => parseInt(string,2).toString(8),
        },
        "hexadecimal":{
            "decimal": string => parseInt(string,16),
            "binary": string => parseInt(string,16).toString(2),
            "octal": string => parseInt(string,16).toString(8),
        },
        "octal":{
            "decimal": string => parseInt(string,8),
            "binary": string => parseInt(string,8).toString(2),
            "hexadecimal": string => parseInt(string,8).toString(16),
        }
    }

    const createOptions = (nameArray,selectElement)=>{
        selectElement.length = 0
        nameArray.forEach(name=>{
            const el = document.createElement("option")
            el.textContent = name[0].toUpperCase() + name.slice(1)
            el.value = name.toLowerCase()
            selectElement.add(el)
        })
    }

    const value = document.querySelector("#input")
    value.type = "text"
    const convertToElement = document.querySelector("#selectMenuTo")
    const convertFromElement = document.querySelector("#selectMenuFrom")
    const outputElement = document.querySelector("footer input")
    convertToElement.remove(0)
    convertFromElement.remove(0)

    const updateFromList = () => createOptions(Object.keys(convertors),convertFromElement)
    const updateToList = () => createOptions(Object.keys(convertors[convertFromElement.value]),convertToElement)
    updateFromList()
    updateToList()

    function convert() {
        outputElement.value = convertors[convertFromElement.value][convertToElement.value](value.value)
    }

    document.querySelector("#container button").addEventListener("click", convert)
    document.querySelector("#selectMenuFrom").addEventListener("change", updateToList)

}