const {createInterface} = require("readline");

function solveTestCase(test) {
    const n = +test[0];
    const [, ...a] = test;
    const tests = readTests(n, a).map(([n, tracks]) => [+n, tracks.trim().split(' ')]);
    let objOfSongs = {};
    for (let i = 0; i < tests.length; i++) {
        let songsCnt = tests[i][0]
        let songs = tests[i][1];
        for (let j = 0; j < songsCnt; j++) {
            if (!objOfSongs[songs[j]]) {
                objOfSongs[songs[j]] = 1;
            } else {
                objOfSongs[songs[j]] += 1;
            }
        }
    }
    let arr = [];
    for (key in objOfSongs){
      if(objOfSongs[key] == n) arr.push(key);
    }
    console.log(arr.length)
    console.log(arr.sort().join(" "));
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

function readTests(n, a) {
    const C = a.length / n;
    return Array.from({length: n}, (_, i) => a.slice(i * C, i * C + C));
}