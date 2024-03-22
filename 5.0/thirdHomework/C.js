const { createInterface } = require("readline");

function solveTestCase(test) {
    let a = test[1].split(' ').map(Number);
    a = a.sort((a, b) => a - b);
    let res = 0;
    console.log(a);
    for (let i = 0; i < a.length; i++){
        let currentNum = a[i];
        let diffCnt = 1;
        for(let j = i + 1; j < a.length; j++){
            let diffNum = a[j];
            if (diffNum - currentNum <= 1){
                diffCnt += 1;
            }
        }
        res = Math.max(diffCnt, res);
    }
    console.log(a.length - res);
}

const lines = [];
createInterface({
    input: process.stdin,
    output: process.stdout,
}).on("line", (line) => {
    lines.push(line.toString().trim());
}).on("close", () => {
    solveTestCase(lines);
});