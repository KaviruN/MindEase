$(document).ready(function () {
    setInterval(function () {

        $.ajax({
            url: '/get-chat-data/',
            type: 'GET',
            success: function (response) {
                $(".flex__chat").empty();
                for (let key in response.chat_data) {
                    let chat_respons = response.chat_data[key].response;
                    let chat_promt = response.chat_data[key].prompt;
                    let chat_html = `
                        <div class="flex__chat--response">
                            <p>${chat_respons}</p>
                        </div>                   
                        <div class="flex__chat--promt">
                            <p>${chat_promt}</p>
                        </div>                        
                    `
                    $(".flex__chat").append(chat_html);
                }
                

            },
            error: function (response) {
                // alert('Error');
            }
        });

    }, 1000);

});
