/*1. In the following shopping cart add, remove, edit itemsconst shoppingCart = ['Milk',
'Coffee', 'Tea', 'Honey']
a. add 'Meat' in the beginning of your shopping cart if it has not been already
added
b. add Sugar at the end of you shopping cart if it has not been already added
c. remove 'Honey' if you are allergic to honey
d. modify Tea to 'Green Tea'  */

const shoppingCart = ['Milk', 'Coffee', 'Tea', 'Honey'];

// Adding 'Meat' in the begining

addedItem = shoppingCart.unshift('Meat');
console.log(shoppingCart);

// Adding 'Sugar' at the end

addedItem = shoppingCart.push('Sugar');
console.log(shoppingCart);

// Removing 'Honey' because I am allergic to Honey
const index = shoppingCart.indexOf('Honey');
if(index > -1){
    shoppingCart.splice(index, 1)
}
console.log(shoppingCart);

// Modifying 'Tea' to 'Green Tea'
const i = shoppingCart.indexOf('Tea');
if(i > -1){
    shoppingCart.splice(i,1,'Green Tea');
}
console.log(shoppingCart);














