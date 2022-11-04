/*
7.Write a function called sumOfArrayItems, it takes an array parameter and return the sum of all the items.
Check if all the array items are number types. If not give return reasonable feedback.
*/
let givenArray = [13, 25, 39, 47];

function sumOfArrayItems(Array){ 

    const sum = Array.reduce((acc, current)=> acc + current)
    return sum;
   }
  

console.log(sumOfArrayItems(givenArray));

