/*
event handlers
 */

// $('form').on('submit', (e) => {
//   e.preventDefault();
//   const text = $('#markdown-input').val();
//   $('#html-output').html(marked(text));
// });

$('#markdown-input').on('keyup', function() {
  // debounce vs throttle
  const text = $(this).val();
  $('#html-output').html(marked($(this).val()));
});


/*
helpers
 */

function post() {
  // add to localstorage
}

function get() {
  // get from localstorage
}
