/*2. In the webTechs array check if Sass exists in the array and if it exists print 'Sass is a
CSS preprocess'. If it does not exist add Sass to the array and print the array. */

let webTech = [
    "HTML", 
    "CSS", 
    "Tailwind", 
    "JavaScript", 
    "ReactJs", 
    "Nodejs", 
    "Express", 
    "MongoDB",
];
let isPresent;
for(let i = 0; i <= webTech.length; i++){
    if(webTech[i]=="Sass"){
        isPresent = true;
    }
    else{
        isPresent = false;
    }
}

if(isPresent == true){
    console.log("Sass is CSS preprocess.");
}
else{
        newlist = webTech.push('Sass');
        console.log(webTech);
}

