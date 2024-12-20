$(document).on('submit', '#chat_form', function(e) {
    e.preventDefault();
    $('#loading').show();
    $.ajax({
        url: '/chat/',
        type: 'POST',
        data: {
            prompt: $('#prompt').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(response) {
            $('#prompt').val('');
            $('#loading').hide();
        },
        error: function(response) {
            alert('Error');
        }
    });
});