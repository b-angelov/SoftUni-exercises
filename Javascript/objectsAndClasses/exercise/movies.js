/*Creating function for task name: solve*/

function solve(parameters) {
    const movies = []
    const checks = ["addMovie","directedBy","onDate"]

    const splitConditions = {
        "addMovie": param => [param.split("addMovie ")[1]],
        "directedBy": param => param.split(" directedBy "),
        "onDate": param => param.split(" onDate "),
    }

    const actions = {
        "addMovie": movie => movies.push({"name": movie}),
        "directedBy": (movie,director) => {
            movie = movies.find(mov => mov.name === movie)
            if (movie){
                movie.director = director
            }
        },
        "onDate": (movie,date) =>{
            movie = movies.find(mov => mov.name === movie)
            if (movie){
                movie.date = date
            }
        }
    }

    for (const param of parameters){
        for (let check of checks){

            if (param.includes(check)){
                let values = splitConditions[check](param)
                actions[check](...values)
                break
            }
        }
    }

    movies.forEach(movie => {
        if (Object.keys(movie).length === 3) console.log(JSON.stringify(movie))
    })

}

solve([
        'addMovie Fast and Furious',
        'addMovie Godfather',
        'Inception directedBy Christopher Nolan',
        'Godfather directedBy Francis Ford Coppola',
        'Godfather onDate 29.07.2018',
        'Fast and Furious onDate 30.07.2018',
        'Batman onDate 01.08.2018',
        'Fast and Furious directedBy Rob Cohen'
    ]
)

solve([
        'addMovie The Avengers',
        'addMovie Superman',
        'The Avengers directedBy Anthony Russo',
        'The Avengers onDate 30.07.2010',
        'Captain America onDate 30.07.2010',
        'Captain America directedBy Joe Russo'
    ]
)