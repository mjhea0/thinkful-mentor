const express = require('express');

const router = express.Router();

const eval = require('../lib/eval');

/*
sanity check
 */
router.get('/ping', (req, res, next) => {
  res.json({
    status: 'success',
    data: 'pong!',
  });
});

/*
eval
 */
router.post('/', (req, res, next) => {
  const code = req.body.code;
  eval.run(code, (err, response) => {
    if (err) return next(err);
    res.json({
      status: 'success',
      data: response,
    });
  });
});


module.exports = router;
