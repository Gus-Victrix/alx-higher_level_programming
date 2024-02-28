$('document').ready(function () {
  $('#btn_translate').click(translate);
  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      translate();
    }
  });
});

function translate () {
  const language = $('#language_code').val();
  $.get(
    `https://fourtonfish.com/hellosalut/?lang=${language}`,
    function (data) {
      $('#hello').html(data.hello);
    }
  );
}
