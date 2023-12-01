const fs = require("fs");

fs.readFile("./input.txt", "utf8", (err, data) => {
  if (err) throw err;
  const vals = data.split("\n");

  // part 1
  let part1 = vals
    .map((val) => {
      const vals_split = [...val].map((v) => Number(v)).filter(Boolean);
      return +`${vals_split[0]}${vals_split.slice(-1)}`;
    })
    .reduce((a, b) => a + b, 0);

  let words = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];

  // part 2
  let part2 = vals.map((val) => {
    let numbers = [...val]
      .map((v, i) => ({ val: Number(v), idx: i }))
      .filter(({ val }) => !isNaN(val)); // filter out only numbers. isNaN('a') => true

    // we only care about the num words starting and ending index not anything in between
    let num_words = words
      .map((word, i) => [
        { val: i, idx: val.indexOf(word) },
        { val: i, idx: val.lastIndexOf(word) },
      ])
      .flat()
      .filter(({ idx }) => idx !== -1);

    let all = [...numbers, ...num_words].sort((a, b) => a.idx - b.idx);
    return +`${all[0].val}${all.slice(-1)[0].val}`;
  })
  .reduce((a,b) => a+b, 0)

  console.log(part2)

});
