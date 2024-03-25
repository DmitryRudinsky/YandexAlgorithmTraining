const { createInterface } = require("readline");

function solveTestCase(test) {
    const n = test[0];
    const a = test[1].split(' ').map(Number);
    let sequences = {};
    let keys = [];
    for(elem of a){
        //console.log(elem, sequences.hasOwnProperty(elem));
        if(!sequences.hasOwnProperty(elem)){
            sequences[elem] = 0;
            keys.push(elem);
        }
        sequences[elem] += 1;
    }
    if(keys.length === 1){
        console.log(0);
    }else{
        let answ = Number.MAX_SAFE_INTEGER;
        let current = Number.MAX_SAFE_INTEGER;
        keys.sort((a, b) => a - b);
        for (let i = 1; i < keys.length; i++){
            if(keys[i] - keys[i - 1] === 1){
                current = n - (sequences[keys[i - 1]] + sequences[keys[i]]);
            }
            if (current < answ){
                answ = current;
            }
        }

        if(answ === Number.MAX_SAFE_INTEGER){
            console.log(n - 1);
        }else{
            console.log(answ);
        }

    }


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