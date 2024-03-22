const { createInterface } = require("readline");

function solveTestCase(test) {
    const [str1, str2] = test;
    console.log(str1.split("").sort().join() === str2.split("").sort().join() ? "YES" : "NO");
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