
$(function () {

    var synth = window.speechSynthesis;
    var msg = new SpeechSynthesisUtterance();
    var voices = synth.getVoices();

    msg.voice = voices[0];
    msg.rate = 1;
    msg.pitch = 1;

    $('#chatbot-form-btn').click(function (e) {
        e.preventDefault();
        $('#chatbot-form').submit();
    });

    $('#chatbot-form-btn-clear').click(function (e) {
        e.preventDefault();
        $('#chatPanel').find('.media-list').html('');
    });

    $('#chatbot-form').submit(function (e) {
        e.preventDefault();
        var message = $('#msg').val();
        $(".media-list").append('<li class="media"><div class="media-body"><div class="media"><div style = "text-align:right; color : #31b0d5" class="media-body">' + message + '<hr/></div></div></div></li>');

        $.ajax({
            type: "POST",
            url: "/",
            data: $(this).serialize(),
            success: function (response) {
                $('#msg').val('');
                var answer = response.answer;

                $(".media-list").append('<li class="media"><div class="media-body"><div class="media"><div style = "color : white" class="media-body">' + answer + '<hr/></div></div></div></li>');
                $(".fixed-panel").stop().animate({ scrollTop: $(".fixed-panel")[0].scrollHeight }, 1000);

                msg.text = answer;
                speechSynthesis.speak(msg);
            },
            error: function (error) {
                console.log(error);
            }
        });
    });

});
