

function solve(x1,y1,x2,y2){
    function correctDistance(firstPoint, secondPoint){
        let [fx,fy] = firstPoint;
        let [sx,sy] = secondPoint;
        let res = ((sx - fx) ** 2 + (sy - fy) ** 2) ** 0.5;
        return Math.trunc(res) == res ? 'valid' : 'invalid';
    }
    console.log(`{${x1}, ${y1}} to {0, 0} is ${correctDistance([x1,y1],[0,0])}`);
    console.log(`{${x2}, ${y2}} to {0, 0} is ${correctDistance([x2,y2],[0,0])}`);
    console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is ${correctDistance([x1,y1],[x2,y2])}`);
}

solve(2, 1, 1, 1)