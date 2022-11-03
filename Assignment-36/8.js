/* 8. Write a function called modifyArray takes array as parameter and modifies the fifth
item of the array and return the array. If the array length is less than five it return 'item
not found'.
*/

var array = ['Rishabh', 'Singh', 'is', 'a', 'hardworking', 'person'];
let modifyArray = (arr) => {
    if(arr.length < 5){
        return "Item not found";
    }
    else{
        arr[4] = 'Lazy';
        return arr;
    }         
}   

console.log(modifyArray(array));
