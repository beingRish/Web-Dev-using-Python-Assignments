// 9. Write a function which checks if all the items of the array are the same data type.

let givenArray = [13, 25, 39, 46, 78];

function sameTypeArray(Array){ 
    for (let i = 0; i < Array.length; i++) {
        if(typeof(Array[i]) != typeof(Array[i+1])){
            return "All Items are same type";
        }
        else{
            return "All Items are not same type";
        }
    }
    
}
  

console.log(sameTypeArray(givenArray));
