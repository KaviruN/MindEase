// Example function to set the checked attribute
function setCheckedInput(value) {
    // Select the input element based on the value
    const inputElement = document.querySelector(`input[name="usermode"][value="${value}"]`);
    if (inputElement) {
        inputElement.checked = true;
    }
}

$(document).ready(function () {
    setInterval(function () {

        $.ajax({
            url: '/get-mode/',
            type: 'GET',
            success: function (response) {

                setCheckedInput(response.usermode);

            },
            error: function (response) {
                // alert('Error');
            }
        });

    }, 1000);

});
