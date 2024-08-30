//print to console
//console.log(`message`)
//variables
//let, const
//let var_name = value
//mentioning var in console
//console.log(`this message is for ${var_name}`)

//how to select an element by id
let myParagraph = document.getElementById("bio");
console.log("found this element by id");
console.log(myParagraph);

//how to select an element by tag type
let allP = document.getElementsByTagName("p");
console.log("found all p elements");
console.log(allP);

//how to select an element by class name
let allTextWrappers = document.getElementsByClassName("text-wrapper");
console.log("found all elements with class text-wrapper");
console.log(allTextWrappers);
for (let i = 0; i < allP.length; i++) {
    console.log(`Text in paragraph ${i+1}: ${allP[i].innerText}`);
    allP[i].style.backgroundColor = `rgb(${Math.random() * 255},${Math.random() * 255},${Math.random() * 255})`;
}