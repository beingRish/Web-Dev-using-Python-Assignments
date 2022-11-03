/*6. Declare a function name capitalizeArray. It takes array as a parameter and it returns
the - capitalizedarray.
*/
var array = ['Rishabh', 'Singh', 'a', 'hardworking', 'person'];
let capitalizeArray = (arr) => {
    let newArray = arr.map(arr => arr.toUpperCase());
    return newArray;             
}   

console.log(capitalizeArray(array));

