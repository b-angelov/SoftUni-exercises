function logicHandler(){
    const baseUrl = "http://localhost:3030/jsonstore/grocery"
    const [productField,countField,priceField,addProductButton,updateProductButton,loadProductButton] = document.querySelectorAll("#signup input,#signup button")
    const containerElement = document.querySelector(".tbl-content table tbody")

    loadProductButton.addEventListener("click",e=>{
        e.preventDefault()
        loadProducts()
    })

    addProductButton.addEventListener("click", async e=>{
        e.preventDefault()
        const fields = [productField.value,countField.value,priceField.value]
        if(!fields.every(el=>el))return
        const [product,count,price] = fields
        await fetch(baseUrl,{
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({
                product,
                count,
                price
            })
        })
        loadProducts()
        setFields()
    })

    async function loadProducts(){
        containerElement.innerHTML = ""
        let products = await fetch(baseUrl)
        products = await products.json()
        Object.values(products).forEach(product=>createProductItem(product.product,product.count,product.price,product._id))
    }

    function createProductItem(product,count,price,id){
        const elements = Object.entries({
            main:{tag:"tr",options:{}},
            name:{tag:"td",options:{className:"name",textContent:product}},
            count:{tag:"td",options:{className:"count-product",textContent:count}},
            price:{tag:"td",options:{className:"product-price",textContent:price}},
            buttons:{tag:"td",options:{className:"btn"}},
            updateButton:{tag:"button",options:{className:"update",textContent:"Update"}},
            deleteButton:{tag:"button",options:{className:"delete",textContent:"Delete"}},
        }).reduce((prev,[name,{tag,options}])=>{
            prev[name] = Object.assign(document.createElement(tag),options)
            return prev
        },{})
        elements.main.appendChild(elements.name)
        elements.main.appendChild(elements.count)
        elements.main.appendChild(elements.price)
        elements.main.appendChild(elements.buttons)
        elements.buttons.appendChild(elements.updateButton)
        elements.buttons.appendChild(elements.deleteButton)
        containerElement.appendChild(elements.main)
        elements.deleteButton.addEventListener("click",async e=>{
            await fetch(`${baseUrl}/${id}`,{method:"DELETE"})
            loadProducts()
        })
        elements.updateButton.addEventListener("click", async e=>{
            setFields(product,count,price)
            addProductButton.setAttribute("disabled","disabled")
            updateProductButton.removeAttribute("disabled")
            updateProductButton.addEventListener("click", async e=>{
                updateProductButton.setAttribute("disabled","disabled")
                addProductButton.removeAttribute("disabled")
                await fetch(`${baseUrl}/${id}`,{
                    method:"PATCH",
                    headers:{"Content-Type":"applications/json"},
                    body:JSON.stringify(Object.entries({
                        product:productField.value,
                        count:countField.value,
                        price:priceField.value,
                    }).reduce((prev,[name,value])=>{
                        if(value) prev[name] = value
                        return prev
                    },{}))
                })
                setFields()
                loadProducts()
            },{once:true})
        })
    }

    function setFields(product="",count="",price=""){
        [productField.value,countField.value,priceField.value] = [product,count,price]
    }
}

logicHandler()