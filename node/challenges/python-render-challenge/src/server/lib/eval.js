const path = require('path');
const fs = require('fs');
const PythonShell = require('python-shell');

const options = {
  scriptPath: path.join(__dirname)
};
const fileName = 'sample.py';

function run(code, callback) {
  // add code to file
  fs.writeFile(path.join(__dirname, 'sample.py'), code, (err) => {
      if(err) callback(err);
      // eval
      PythonShell.run(fileName, options, (error, results) => {
        if (error) callback(error);
        callback(null, results);
      });
  });
}

module.exports = {
  run
};
