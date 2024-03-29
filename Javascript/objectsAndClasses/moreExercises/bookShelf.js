/*Creating function for task name: book shelf*/

function bookShelf(data) {
    const shelf = {}
    const actions = {
        "->":value => {
            const [id,genre] = value.split(" -> ")
            if(!shelf.hasOwnProperty(id)) shelf[id] = {genre:genre,books:{}}
        },
        ":": value => {
            const [title,rest] = value.split(": ")
            const [author,genre] = rest.split(", ")
            Object.entries(shelf).forEach(([id,shelf])=>{
                if (shelf.genre === genre) shelf.books[title] = author
            })
        }
    }
    for (let command of data){
        for (let action of Object.keys(actions)){
            if (command.includes(action)){
                actions[action](command)
            }
        }
    }

    Object.entries(shelf)
        .sort(([genre,books],[genreB,booksB])=>Object.keys(booksB.books).length - Object.keys(books.books).length)
        .forEach(([id,books])=>{
            console.log(`${id} ${books.genre}: ${Object.keys(books.books).length}`)
            Object.entries(books.books)
                .sort(([title,author],[titleB,authorB])=>title.localeCompare(titleB))
                .forEach(([title,author])=>{
                    console.log(`--> ${title}: ${author}`)
                })
        })
}

bookShelf(['1 -> history', '1 -> action', 'Death in Time: Criss Bell, mystery', '2 -> mystery', '3 -> sci-fi', 'Child of Silver: Bruce Rich, mystery', 'Hurting Secrets: Dustin Bolt, action', 'Future of Dawn: Aiden Rose, sci-fi', 'Lions and Rats: Gabe Roads, history', '2 -> romance', 'Effect of the Void: Shay B, romance', 'Losing Dreams: Gail Starr, sci-fi', 'Name of Earth: Jo Bell, sci-fi', 'Pilots of Stone: Brook Jay, history'])
bookShelf(['1 -> mystery', '2 -> sci-fi',
    'Child of Silver: Bruce Rich, mystery',
    'Lions and Rats: Gabe Roads, history',
    'Effect of the Void: Shay B, romance',
    'Losing Dreams: Gail Starr, sci-fi',
    'Name of Earth: Jo Bell, sci-fi']
)