/*
6. Develop a small script which generate any number of characters random id 
*/

var text = "";
var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz";
for( var i=0; i <= Math.floor(Math.random() * 100); i++ ){
  text += possible.charAt(Math.floor(Math.random() * possible.length));
}
console.log(text);
