/*
8. This is a fruit array , ['banana', 'orange', 'mango', 'lemon'] reverse the order using
loop without using a reverse method.
*/

let fruit = ['banana', 'orange', 'mango', 'lemon'];
let reversedArray = [];
for(let i = fruit.length-1; i >= 0; i--){
    reversedArray.push(fruit[i]);
}
console.log(reversedArray);

