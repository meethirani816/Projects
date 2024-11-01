function nice(name) {
    console.log("Hey " + name + " you are nice");
    console.log("Hey " + name + " you are good");
    console.log("Hey " + name + " your tshirt is nice");
    console.log("Hey " + name + " your course is good");
}

nice("harry");

function sum(a , b , c=3) {
   // console.log( a + b );
    return a + b + c;
}

result = sum(5,5);

console.log("the sum of this no. is " , result);

const funct1 = (x)=>{
    console.log("i am an arrow function", x);
}

funct1(22);
funct1(54);