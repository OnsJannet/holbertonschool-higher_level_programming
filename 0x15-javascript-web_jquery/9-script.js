/* fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value
of hello from that fetch in the HTML’s tag DIV#hello. */

/* text(): IGet the combined text contents of each element in the set of matched elements,
including their descendants, or set the text contents of the matched elements. */

// https://api.jquery.com/text/

const $ = window.$;
$(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
