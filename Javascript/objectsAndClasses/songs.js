/*Creating function for task name: solve*/

function solve(songList) {

    let songs = songList.slice(1,songList.length - 1)
    let type = songList.slice(songList.length - 1)
    let songObj = {}

    class Song{

        constructor(typeList, name, time) {
            this.typeList = typeList;
            this.name = name;
            this.time = time;

        }

    }
    songs.forEach(
        element =>{
            let [type,song,time] = element.split("_")
            if (!songObj[type]) songObj[type] = []
            songObj[type].push(new Song(type, song, time))
        }
    )

    if(type == 'all'){
        Object.entries(songObj).forEach(element=> element[1].forEach(el=>console.log(el.name)))
    }else{
        songObj[type].forEach(el => console.log(el.name))
    }
}

// console.log(solve([3,
//     'favourite_DownTown_3:14',
//     'favourite_Kiss_4:16',
//     'favourite_Smooth Criminal_4:01',
//     'favourite']
// ))
// console.log(solve([4,
//     'favourite_DownTown_3:14',
//     'listenLater_Andalouse_3:24',
//     'favourite_In To The Night_3:58',
//     'favourite_Live It Up_3:48',
//     'listenLater']
// ))
console.log(solve([2,
    'like_Replay_3:15',
    'ban_Photoshop_3:48',
    'all'])
)
console.log(solve([1,"0_0_0",0]))