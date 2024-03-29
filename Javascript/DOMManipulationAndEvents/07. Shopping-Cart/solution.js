function solve() {
    const shoppingCartElement = document.querySelector("body > .shopping-cart")
    const resultElement= document.querySelector(".shopping-cart textarea")
    const checkOutElement = document.querySelector(".shopping-cart button.checkout")
    let cart = []
    shoppingCartElement.addEventListener("click",handleCart)
    checkOutElement.addEventListener("click", handleCheckout)

    function handleCart(event){
        if (event.target.tagName !== "BUTTON") return
        const price = event.target.parentElement.parentElement.querySelector(".product-line-price")
        const name = event.target.parentElement.parentElement.querySelector(".product-details .product-title")
        cart.push({price:Number(price.textContent),type:name.textContent})
        resultElement.textContent += `Added ${name.textContent} for ${Number(price.textContent).toFixed(2)} to the cart.\n`
    }

    function handleCheckout(event){
        const products = Array.from(new Set(cart.reduce((prev,prod)=> {
            prev.push(prod.type)
            return prev
        },[]))).join(", ")
        const totalPrice =  cart.reduce((prev,{price,type})=> prev + price,0)
        resultElement.textContent += `You bought ${products} for ${totalPrice.toFixed(2)}.`
        Array.from(document.querySelectorAll("button")).forEach(element=>element.setAttribute("disabled","disabled"))
        event.stopPropagation()
    }


}