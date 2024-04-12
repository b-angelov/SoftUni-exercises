/*Creating function for task name: logic handler*/

function logicHandler() {
    const baseUrl = "http://localhost:3030/jsonstore/tasks"
    const [courseNameInp,courseTypeInp,courseDescriptionInp,teacherNameInp,addCourseBtn,editCourseBtn] = document.querySelectorAll("#form input,#form button, #form textarea")
    const loadCourseButton = document.querySelector("#progress-course #load-course")
    const previewListEl = document.querySelector("#list")
    previewListEl.innerHTML = ""

    loadCourseButton.addEventListener("click", e=>{
        loadItems()
    })

    addCourseBtn.addEventListener("click",e=>{
        e.preventDefault()
        addCourse()
    })

    async function loadItems(){
        previewListEl.innerHTML = ""
        let data = await fetch(baseUrl)
        data = await data.json()
        Object.values(data).forEach(item=>{
            createElement(item.title,item.type,item.description,item.teacher,item._id)
        })
    }

    function createElement(title,type,description,teacher,id){
        const containerDiv = document.createElement("div")
        containerDiv.className = "container"
        const titleElement = document.createElement("h2")
        titleElement.textContent = title
        const typeElement = document.createElement("h3")
        typeElement.textContent = type
        const descriptionElement = document.createElement("h4")
        descriptionElement.textContent = description
        const teacherElement = document.createElement("h3")
        teacherElement.textContent = teacher
        const editButton = document.createElement("button")
        editButton.classList.add("edit-btn")
        editButton.textContent = "Edit Course"
        const finishButton = document.createElement("button")
        finishButton.textContent = "Finish Course"
        finishButton.classList.add("finish-btn")

        containerDiv.appendChild(titleElement)
        containerDiv.appendChild(teacherElement)
        containerDiv.appendChild(typeElement)
        containerDiv.appendChild(descriptionElement)
        containerDiv.appendChild(editButton)
        containerDiv.appendChild(finishButton)
        previewListEl.appendChild(containerDiv)

        editButton.addEventListener("click",e=>{
            addCourseBtn.setAttribute("disabled","disabled")
            editCourseBtn.removeAttribute("disabled")
            containerDiv.remove()
            setFields(title,type,description,teacher)
            editCourseBtn.addEventListener("click",e=>{
                addCourseBtn.removeAttribute("disabled")
                editCourseBtn.setAttribute("disabled","disabled")
                addCourse(id)
                loadItems()
            },{once:true})
        })
        finishButton.addEventListener("click",e=>{
            finish(id)
        })

    }

    async function addCourse(courseId){
        let url = baseUrl
        const body = {}
        let method = "POST"
        if(courseId){
            method = "PUT"
            body._id = courseId
            url = `${baseUrl}/${courseId}`
        }
        body.title = courseNameInp.value
        body.type = courseTypeInp.value
        body.description = courseDescriptionInp.value
        body.teacher = teacherNameInp.value
        await fetch(url,{
            method,
            "Content-Type":"application/json",
            body:JSON.stringify(body)
        })
        setFields()
        loadItems()
    }

    function edit(id){
        addCourse(id)
        setFields()
    }
    async function finish(id){
        await fetch(`${baseUrl}/${id}`,{
            method: "DELETE"
        })
        loadItems()
    }
    function setFields(title="",type="",description="",teacher=""){
        courseNameInp.value =  title
        courseTypeInp.value = type
        courseDescriptionInp.value = description
        teacherNameInp.value = teacher
    }
}

logicHandler()