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