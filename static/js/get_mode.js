// Example function to set the checked attribute
function setCheckedInput(value) {
    // Select the input element based on the value
    const inputElement = document.querySelector(`input[name="usermode"][value="${value}"]`);
    if (inputElement) {
        inputElement.checked = true;
    }
}
function displayVideos(value) {
    const displayVideo = document.querySelector('.videos');
    displayVideo.innerHTML = '';
    if (value == "Angry") {
        displayVideo.innerHTML += '<iframe src="https://www.youtube.com/embed/tV2Ecd7m6Tc?si=kI1eRVcYWX7IbDeE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>';
    }
    if (value == "Sad") {
        displayVideo.innerHTML += '<iframe src="https://www.youtube.com/embed/BloutcYWbJg?si=A3_7i9U3L-eYO-02" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>';
    }
    if (value == "Ok") {
        displayVideo.innerHTML += '<iframe src="https://www.youtube.com/embed/sm0i1Y4g_zA?si=NRKUfcWVbfFofFfB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>';
    }
    if (value == "Good") {
        displayVideo.innerHTML += '<iframe src="https://www.youtube.com/embed/B5u-SGDfS_s?si=cYl3TX7-PkyqvXPX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>';
    }
    if (value == "Happy") {
        displayVideo.innerHTML += '<iframe src="https://www.youtube.com/embed/JJ9GD0SiwEc?si=sUJ0AJqWWR8KnEhd" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>';
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

$(document).ready(function () {
    $.ajax({
        url: '/get-mode/',
        type: 'GET',
        success: function(response) {

            displayVideos(response.usermode);
            

        },

    });
    $('input[name="usermode"]').change(function () {
        const selectedValue = $(this).val();
        displayVideos(selectedValue);
    });
});
