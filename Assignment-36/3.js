/*
3. Develop a small script which generate any number of characters random id.
Example:
fe3jo1gl124g
xkqci4utda1lmbelpkm03rba
*/

var text = "";
var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz";
for( var i=0; i <= Math.floor(Math.random() * 100); i++ ){
  text += possible.charAt(Math.floor(Math.random() * possible.length));
}
console.log(text);