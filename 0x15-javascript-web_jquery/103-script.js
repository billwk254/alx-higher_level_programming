$(document).ready(function () {
  function translateHello () {
    const languageCode = $('#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    $.get(url, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(translateHello);

  $('#language_code').keydown(function (event) {
    if (event.keyCode === 13) {
      translateHello();
    }
  });
});
