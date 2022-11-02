/*
3. The following is an array of 10 students ages:
const ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
    Sort the array and find the min and max age
    Find the median age(one middle item or two middle items divided by two)
    Find the average age(all items divided by number of items)
    Find the range of the ages(max minus min)
    Compare the value of (min - average) and (max - average), use abs() method
*/

const ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

// Sorting the array and finding the minimum and maximum age
console.log(ages.sort());
console.log("Minimum age = " + Math.min.apply(Math, ages));
console.log("Maximum age = " + Math.max.apply(Math, ages));

// Finding the median age

// First I have to sort the elements?
// find the lenght of the array
// if length is even then index of (length + 1)/2 else length / 2
sortedArray = ages.sort();
lengthOfArray = sortedArray.length;
let medianAge = 0;
for(let i = 0; i < lengthOfArray; i++){
    if(lengthOfArray % 2 == 0){
        medianAge = sortedArray[(lengthOfArray + 1)/2];
    }
    else{
        medianAge = sortedArray[lengthOfArray/2];
    }
}
console.log("Median Age = " + medianAge);


// Finding the average age

var sum = 0;
let Average;
for(let i = 0; i < ages.length; i++){
    sum = sum + ages[i];
    Average = sum / ages.length
}
console.log("Average = " + Average);


// Finding the range of the age

Max = Math.max.apply(Math, ages);
Min = Math.min.apply(Math, ages);
findingRange = Max - Min;
console.log("Range of Ages = " + findingRange );


// Comparing the value
console.log("Comparing the value between minimum and average : " + Math.abs(Min - Average));
console.log("Comparing the value between maximum and average : " + Math.abs(Max - Average));





