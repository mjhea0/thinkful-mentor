$(function() {

    // scope test 1
    // function test() {
    //     var nonTest = "hi";
    //     console.log(nonTest);
    // };


    // function test2() {
    //     console.log(nonTest);
    // };

    // test();
    // test2();
    // console.log(nonTest);

    // scope test2

    function ping() {
        var pong = "pong!";
        console.log(pong);

        function table() {
            console.log(pong);
        };
        table();
    };

    ping();

});



// 1. Scope is your current location
// 2. Global scope is the entire world; you are everywhere, touching everything (susceptible)
// 3. Within a function, you are bound by that function; you are boxed in (safe)

// Then show a quick example -

// var globalScope = "global";

// function scopeTest() {
//   var localScope = "local";
//   console.log(localScope); // outputs correctly
// }

// scopeTest(); // outputs correctly
// console.log(globalScope); // outputs correctly
// console.log(localScope); // reference error
