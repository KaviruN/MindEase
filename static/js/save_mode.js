$(document).on('change', '#usermode', function(e) {
    e.preventDefault();
    $.ajax({
        url: '/save-mode/',
        type: 'POST',
        data: {
            usermode: $('input[name=usermode]:checked').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(response) {
            const msg = document.querySelector('#msg');
            msg.textContent = response;
        },
        error: function(response) {
            alert('Error');
        }
    });
});