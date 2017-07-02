# Python Render Challenge

1. Python text area on the left, that you can write in.
1. When you click on run, the python code is executed and the output is shown on the right side.

Notes:

1. The code is executed locally on a backend.
1. For the code execution you can use libraries like
https://www.npmjs.com/package/python-shell
http://stackoverflow.com/questions/20972788/how-to-invoke-external-scripts-programs-from-node-js
1. This is not easy, so keep it simple and try to get as far as you can.

### Steps

1. Create boilerplate (30 mins)
1. Wire up POST, client and server (5 mins)
1. Add code eval (20 mins)
1. Update code eval (todo - write new file each time)

### To Use

1. `npm i`
1. Run server - `npm start` (http://localhost:8081/api/v1/eval/ping)
1. Run client - `http-server src/client` (http://localhost:8080/)

### Tests

1. Server - `npm test`
