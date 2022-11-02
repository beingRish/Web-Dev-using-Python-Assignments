/*
2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all
odds. Print sum of evens and sum of odds as array.
*/
let sum1 = 0;
let sum2 = 0;
for(let i = 1; i <= 100; i++){
    if(i %2 == 0){
        sum1 = sum1 + i;
    }
    else{
        sum2 = sum2 + i;
    }
}
let EvenOddSum = [];
let Array1 = EvenOddSum.push(sum1, sum2)
console.log(EvenOddSum);