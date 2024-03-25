const { createInterface } = require("readline");

function solveTestCase(test) {
  let [[n, k], a] = test.map(l => l.split(' ').map(Number));

  function findDubl(n, k, array){
    if(k > n) k = n;

    let queue = [];
    let buffer = {};

    for(let i = 0; i < k; i++){
      const currentNum = array[i];
      if(buffer[currentNum] != 0 && buffer[currentNum] != undefined){
        return "YES";
      }
      queue.push(currentNum);
      buffer[currentNum] = 1;
    }

    for (let i = k; i < n; i++){
      const currentNum = array[i];
      if(buffer[currentNum] != 0 && buffer[currentNum] != undefined){
        return "YES";
      }
      buffer[queue[0]]--;
      queue.shift();
      queue.push(currentNum);
      buffer[currentNum] = (buffer[currentNum] || 0) + 1;
    }
    return "NO";

  }

  console.log(findDubl(n, k, a));
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