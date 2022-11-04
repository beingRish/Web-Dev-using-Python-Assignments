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

let arg1 = countries.filter((arg)=> arg.includes("and"));
if(arg1.length==0){
    console.log("All these countries are withou and.");
}
else{
    console.log(arg1);
}
