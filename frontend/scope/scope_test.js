// Global scope
var num1 = 1;
var num2 = 2;

function test() {
    num3 = 3; // Global scope (no var)
    var num4 = 4; // Local scope
    var num5 = num1+num2+num3; // Local scope
    return num5
}

console.log(num1)
console.log(num2)
// console.log(num3)
// console.log(num4)
// console.log(num5)
console.log(test())