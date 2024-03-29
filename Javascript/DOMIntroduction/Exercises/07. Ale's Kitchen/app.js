function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   function onClick () {
      const inputFieldElement = document.querySelector("#inputs textarea")
      const [firstOutputElement, secondOutputElement] = document.querySelectorAll("#outputs div p:last-of-type")
      let data = {}
      firstOutputElement.textContent = ''
      secondOutputElement.textContent = ''

      const input = JSON.parse(inputFieldElement.value)
      input.forEach(element=>{
         const [name,dat] = element.split(" - ")
         if (!data.hasOwnProperty(name)) data[name] = []
         const workers = dat.split(", ")
         workers.forEach(el=>{
            let [worker,salary] = el.split(" ")
            salary = Number(salary)
            data[name].push({worker:worker,salary:salary})
         })
      })
      data = Object.entries(data).sort(([nameA,dataA],[nameB,dataB])=>{
         let salariesA = dataA.reduce((a,b)=> {a.push(b.salary); return a},[]).reduce((a,b)=>a+b) / dataA.length
         let salariesB = dataB.reduce((a,b)=> {a.push(b.salary); return a},[]).reduce((a,b)=>a+b) / dataB.length
         return salariesB - salariesA
      })

      const bestRestaurant = data[0]
      const salaries = bestRestaurant[1].reduce((a,b)=> {a.push(b.salary); return a},[]).sort((a,b)=>b-a)
      const [bestSalary, averageSalary] = [salaries[0],salaries.reduce((a,b)=>a+b) / salaries.length]
      firstOutputElement.textContent = `Name: ${bestRestaurant[0]} Average Salary: ${averageSalary.toFixed(2)} Best Salary: ${bestSalary.toFixed(2)}`
      bestRestaurant[1]
          .sort((a,b)=>b.salary-a.salary)
          .forEach(data=>{
         secondOutputElement.textContent += `Name: ${data.worker} With Salary: ${data.salary} `
      })

      
   }
}