// crypt(3) module.
var crypt3 = require('../build/Release/crypt3');

// Exporting function.
module.exports = function(password, salt) {
    return salt ? crypt3.crypt(password, salt) : crypt3.crypt(password);
};
