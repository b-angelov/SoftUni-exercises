function logicHandler(){
    const baseUrl = "http://localhost:3030/jsonstore/tasks"
    const [foodInput,timeInput,caloriesInput,addMealButton,editMealButton] = document.querySelectorAll("#form-container #form input,#form-container #form button")
    const loadMealsButton = document.querySelector("#wrapper #meals #load-meals")
    const mealContainer = document.querySelector("#wrapper #meals #list")
    const mealTemplate = mealContainer.querySelector(":scope > div.meal")
    mealTemplate.remove()


    loadMealsButton.addEventListener("click",loadMeals)

    async function loadMeals(){
        mealContainer.innerHTML = ""
        let meals = await fetch(baseUrl)
        editMealButton.setAttribute("disabled","disabled")
        meals = await meals.json()
        Object.values(meals).forEach(meal=>{
            serveMeal(
                meal.food,
                meal.calories,
                meal.time,
                (e)=>changeFunction(e,meal._id,meal.food,meal.time,meal.calories),
                (e)=>deleteFunction(meal._id)
            )
        })
    }

    addMealButton.addEventListener("click",async (e)=>{
        await addMeal()
        loadMeals()
    })



    function changeFunction(e,id,food,time,calories) {
        foodInput.value = food
        timeInput.value = time
        caloriesInput.value = calories
        e.target.parentElement.parentElement.remove()
        addMealButton.setAttribute("disabled","disabled")
        editMealButton.removeAttribute("disabled")
        editMealButton.addEventListener("click",async (e)=> {
            await addMeal(id)
            loadMeals()
            editMealButton.setAttribute("disabled","disabled")
            addMealButton.removeAttribute("disabled")
        },{once:true})
    }

    async function deleteFunction(id) {
        await fetch(`${baseUrl}/${id}`,{
            method : "DELETE"
        })
        loadMeals()
    }

    function serveMeal(food,time,calories,changeFunc,delFunc){
        const meal = mealTemplate.cloneNode(true)
        const [foodP,timeP,caloriesP,changeMealButton,deleteMealButton] = meal.querySelectorAll("h2,h3,h4,button")
        foodP.textContent = food
        timeP.textContent = time
        caloriesP.textContent = calories
        changeMealButton.addEventListener("click", changeFunc)
        deleteMealButton.addEventListener("click",delFunc)
        mealContainer.appendChild(meal)
    }

    async function addMeal(mealId=false){
        const [food,time,calories] = [foodInput.value,timeInput.value,caloriesInput.value]
        if (![food,time,calories].every(meal=>meal)) return
        const method = mealId ? "PUT" : "POST"
        let url = baseUrl
        if(method === "PUT") url = `${baseUrl}/${mealId}`
        const body = {
            food,
            time,
            calories
        }
        if (mealId) body._id = mealId
        await fetch(url, {
            method,
            headers: {"Content-Type": "application/json"},
            body:JSON.stringify(body)
        })
        clearFields()
    }

    function clearFields(){
        foodInput.value = ""
        timeInput.value = ""
        caloriesInput.value = ""
    }

    function loadMeal(food,time,calories){
        foodInput.value = food
        timeInput.value = time
        caloriesInput.value = calories
    }
}

logicHandler()