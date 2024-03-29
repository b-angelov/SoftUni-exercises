/*Creating function for task name: solve*/

function solve(towns) {
    towns = towns
        .map(data => {
        const [town, latitude, longitude] = data.split(" | ");
        return ({"town":town, "latitude":Number(latitude).toFixed(2), "longitude":Number(longitude).toFixed(2)});
    })
        .forEach(obj=>console.log(obj))

}

console.log(solve(['Sofia | 42.696552 | 23.32601',
    'Beijing | 39.913818 | 116.363625']
))