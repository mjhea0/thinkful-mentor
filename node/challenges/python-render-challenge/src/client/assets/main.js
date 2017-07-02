/*
event handlers
 */

$('form').on('submit', (e) => {
  event.preventDefault();
  return evaluateCode($('form').serialize())
  .then((res) => {
    $('#eval-output').html(res.data[0]);
  })
  .catch((err) => { console.log(err); });
});

// helpers

function evaluateCode(data) {
  return $.ajax({
    method: 'POST',
    data: data,
    url: `http://localhost:8081/api/v1/eval`,
  });
}
