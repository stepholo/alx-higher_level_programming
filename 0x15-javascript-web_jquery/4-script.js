// toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header
// The <header> element must always have one class: red or green,
// never both in the same time and never empty.
// If the current class is red, when the user click on DIV#toggle_header,
// the class must be updated to green ; and the reverse.

$('div#toggle_header').click(function () {
  if ($('header').attr('class') === 'green') {
    $('header').attr('class', 'red');
  } else {
    ($('header').attr('class', 'green'));
  }
});
