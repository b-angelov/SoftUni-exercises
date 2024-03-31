/*Creating function for task name: JS Front-End Retake Exam -22 December 2023*/

function jsFrontEndRetakeExam22December2023(input) {
    let [string,...commands] = input
    const actions ={
        "TakeEven":()=>{
            let str = ''
            for (let i = 0; i < string.length; i+=2) {
                str += string[i]
            }
            console.log(str)
            string = str
        },
        "ChangeAll":(substr,rep)=>{
            string = string.replace(new RegExp(substr,"g"),rep)
            console.log(string)
        },
        "Reverse":(substr)=>{
            const sub = string.indexOf(substr)
            if(sub > -1){
                string = string.replace(substr,"") + substr.split("").reverse().join("")
                console.log(string)
            }else{
                console.log("error")
            }
        },
        Buy(){
            console.log(`The cryptocurrency is: ${string}`)
        }

    }

    for (const command of commands) {
        [action,...options] = command.split("?")
        actions[action](...options)
    }
}

console.log(jsFrontEndRetakeExam22December2023((["z2tdsfndoctsB6z7tjc8ojzdngzhtjsyVjek!snfzsafhscs",
    "TakeEven",
    "Reverse?!nzahc",
    "ChangeAll?m?g",
    "Reverse?adshk",
    "ChangeAll?z?i",
    "Buy"])
))