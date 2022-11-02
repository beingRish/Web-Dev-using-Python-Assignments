// 7. Write a script which generates a random hexadecimal number.

let items = ["a", "b", "c", "d", "e", "f"];
let item = items[Math.floor(Math.random()*items.length)];
let random = Math.random().toString().slice(2, 6);
console.log (`
    ${item}${random}${item}
`);