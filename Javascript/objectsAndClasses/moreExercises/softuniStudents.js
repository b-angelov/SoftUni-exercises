/*Creating function for task name: SoftUni Students*/

function softUniStudents(data) {
    const courses = {}

    const actions = {

        ":": value =>{
            const [name,capacity] = value.split(": ")
            if(!courses.hasOwnProperty(name)) courses[name] = {capacity:0,students:{}}
            courses[name]['capacity'] += Number(capacity)
        },
        "[": value =>{
            const [studentName,credits,email,course] = value.match(/^([^\[]+)|(?<=\[)\d+|(?<=email )(\S+)|(?<=joins )(.+)/gm)
            if(courses.hasOwnProperty(course) && courses[course].capacity > Object.keys(courses[course].students).length){
                courses[course].students[studentName] = {credits:Number(credits),email:email}
            }

        },

    }

    for (let command of data){
        for (let action of Object.keys(actions)){
            if (command.includes(action)){
                actions[action](command)
                break
            }
        }
    }
    Object.entries(courses)
        .sort(([name,data],[nameB,dataB])=>Object.entries(dataB.students).length - Object.entries(data.students).length)
        .forEach(([courseName,data])=>{
            console.log(`${courseName}: ${data.capacity - Object.keys(data.students).length} places left`)
            Object.entries(data.students)
                .sort(([name,dat],[nameB,datB])=>datB.credits - dat.credits)
                .forEach(([name,dat])=>{
                    console.log(`--- ${dat.credits}: ${name}, ${dat.email}`)
                })
        })

}

softUniStudents(['JavaBasics: 2', 'user1[25] with email user1@user.com joins C#Basics', 'C#Advanced: 3', 'JSCore: 4', 'user2[30] with email user2@user.com joins C#Basics', 'user13[50] with email user13@user.com joins JSCore', 'user1[25] with email user1@user.com joins JSCore', 'user8[18] with email user8@user.com joins C#Advanced', 'user6[85] with email user6@user.com joins JSCore', 'JSCore: 2', 'user11[3] with email user11@user.com joins JavaBasics', 'user45[105] with email user45@user.com joins JSCore', 'user007[20] with email user007@user.com joins JSCore', 'user700[29] with email user700@user.com joins JSCore', 'user900[88] with email user900@user.com joins JSCore'])
console.log('\n\n\n\n\n\n')
// softUniStudents(['JavaBasics: 15',
//     'user1[26] with email user1@user.com joins JavaBasics',
//     'user2[36] with email user11@user.com joins JavaBasics',
//     'JavaBasics: 5',
//     'C#Advanced: 5',
//     'user1[26] with email user1@user.com joins C#Advanced',
//     'user2[36] with email user11@user.com joins C#Advanced',
//     'user3[6] with email user3@user.com joins C#Advanced',
//     'C#Advanced: 1',
//     'JSCore: 8',
//     'user23[62] with email user23@user.com joins JSCore']
// )