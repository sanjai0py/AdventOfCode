const fs = require("fs");

fs.readFile("./input.txt", "utf8", (err, data) => {
  if (err) throw err;
  const vals = data.split("\n");

  let part1 = vals.map((val) => {
    const vals_split = [...val].map((v) => Number(v)).filter(Boolean);
    return +`${vals_split[0]}${vals_split.slice(-1)}`;
  }).reduce((a, b) => a + b, 0)

  console.log(part1);
});
