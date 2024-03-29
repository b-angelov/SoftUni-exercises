/*Creating function for task name: solve*/

function solve(gradeScored) {
    let grades = {"Fail":[-Infinity,2.999],"Poor":[3,3.499],"Good":[3.5,4.499],"Very good":[4.5,5.499],"Excellent":[5.5,Infinity]}
    let evaluate = function(a,b,value){return a <= value && value <= b}
    for (let grade in grades){
        [a,b] = grades[grade]

        if(evaluate(a,b,gradeScored)){
            return `${grade} (${grade!=="Fail"?gradeScored.toFixed(2):2})`;
        }
    }
}

console.log(solve(3.33))
console.log(solve(4.5))
console.log(solve(2.99))