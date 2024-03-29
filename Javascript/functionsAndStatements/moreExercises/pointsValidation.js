/*Creating function for task name: solve*/

function solve(points) {
    function pointsDistance(points){
        let [x1,y1,x2,y2] = points
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    }
    const validPoints = (p) => pointsDistance(p) === Math.trunc(pointsDistance(p))
    const [x1,y1,x2,y2] = points
    const comparisons = [[x1,y1,0,0],[x2,y2,0,0],[x1,y1,x2,y2]]
    comparisons.forEach((p) => console.log(`{${p[0]}, ${p[1]}} to {${p[2]}, ${p[3]}} is ${validPoints(p)?'':'in'}valid`))
}

console.log(solve([3, 0, 0, 4]))
console.log(solve([2, 1, 1, 1]))