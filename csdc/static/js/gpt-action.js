$(document).ready(function() {
    var submitButton = $('#submitButton'); 
    var loadingSpinner = $('#loadingSpinner'); 

    $('form').on('submit', function(event) {
        event.preventDefault();
        submitButton.hide(); 
        loadingSpinner.show(); 

        var csrftoken = Cookies.get('csrftoken');
        $.ajaxSetup({
            headers: { 'X-CSRFToken': csrftoken }
        });

        var prompt = $('#prompt').val();
        var dateTime = new Date();
        var time = dateTime.toLocaleTimeString();

        var userMessageContainer = appendMessage(time, prompt, 'user');

        $('#prompt').val('');
        $.ajax({
            url: '/chat/', 
            type: 'POST',
            data: {prompt: prompt},
            dataType: 'json',
            success: function(data) {
                appendMessage(time, data.response, 'system', userMessageContainer);
                loadingSpinner.hide();
                submitButton.show(); 
            },
            error: function() {
                var errorMessage = '응답을 받는 데 문제가 발생했습니다.';
                appendMessage(time, errorMessage, 'system', userMessageContainer);
                loadingSpinner.hide();
                submitButton.show(); 
            }
        });
    });
});


function appendMessage(time, message, sender, previousMessage) {
    var iconClass = sender === 'user' ? 'bi-person' : 'bi-robot';
    var messageClass = sender === 'user' ? 'user-message' : 'system-message';
    var messageContainer = $('<div></div><br>').addClass('chat-bubble ' + messageClass);
    $('#response').append(messageContainer);
    typeMessage(message, messageContainer);
    return messageContainer; // 메시지 컨테이너 반환
}

function typeMessage(message, container) {
    var i = 0;
    var interval = setInterval(function() {
        if (i < message.length) {
            container.append(message.charAt(i));
            i++;
        } else {
            clearInterval(interval);
        }
    }, 50); // 타이핑 속도 조절
}