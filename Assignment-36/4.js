/*
4. Create a countries array, check if there is a country or countries containing the word
'and'. If there are countries containing 'and', print it as array. If there is no country
containing the word 'and', print 'All these countries are without and'.
*/

let countries = [
    "Afghanistan", "Argentina", "Australia",
    "Canada", "China", "Colombia",
    "Iceland", "India", "Indonesia", "Ireland", 
    "Nepal", "Netherlands", "New Zealand", "Namibia",
    "Pakistan", "Poland", 
    "Singapore", "Solomon Islands", "South Africa", "Sri Lanka", "Switzerland",
    "Tajikistan", "Thailand", "Turkey"
]

let arr = [];
for(let i = 0; i < countries.length; i++){
    if(countries[i].includes('land'))
    arr.push(countries[i])
}

if(arr.length > 0 ){
    console.log(arr);
}
else{
    console.log('All these are countries without land')
}
  

