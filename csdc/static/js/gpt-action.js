$(document).ready(function() {
    var submitButton = $('#submitButton'); 
    var loadingSpinner = $('#loadingSpinner'); 
    var promptInput = $('#prompt');
    
    promptInput.keyup(function() {
        // 입력된 값이 있다면 버튼을 활성화, 그렇지 않다면 비활성화합니다.
        submitButton.prop('disabled', this.value.trim() === "");
    });

    // 페이지가 로드되었을 때 초기 상태를 비활성화로 설정합니다.
    submitButton.prop('disabled', true);

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
    // 타이핑 시작 시 입력 필드와 버튼 비활성화
    $('#prompt').prop('disabled', true);
    $('#submitButton').prop('disabled', true);

    var interval = setInterval(function() {
        if (i < message.length) {
            container.append(message.charAt(i));
            i++;
        } else {
            clearInterval(interval);
            // 타이핑이 끝나면 입력 필드와 버튼 다시 활성화
            $('#prompt').prop('disabled', false);
            // 입력 필드에 텍스트가 있을 경우만 제출 버튼 활성화
            $('#submitButton').prop('disabled', $('#prompt').val().trim() === "");
            $('#prompt').focus(); // 사용자가 바로 입력할 수 있도록 입력 필드에 포커스
        }
    }, 50); // 타이핑 속도 조절
}
