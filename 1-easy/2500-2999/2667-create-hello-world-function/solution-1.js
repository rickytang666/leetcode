/**
 * @return {Function}
 */
var createHelloWorld = function() {
    return () => "Hello World";
};


const f = createHelloWorld();
console.log(f({}, null, 42)); // expected output: "Hello World"