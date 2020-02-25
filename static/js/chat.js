var synth = window.speechSynthesis
var msg = new SpeechSynthesisUtterance()
var voices = synth.getVoices()

msg.voice = voices[0]
msg.rate = 1
msg.pitch = 1

$('#chatbot-form-btn').click(function (e) {
    e.preventDefault()
    $('#chatbot-form').submit()
})

$('#chatbot-form-btn-clear').click(function (e) {
    e.preventDefault()
    $('#chatPanel').find('.media-list').html('')
})

$('#chatbot-form').submit(function (e) {
    e.preventDefault()

    $(".media-list")
        .append(`<li class="media-user">${$('#msg').val()}<hr/></li>`)

    $.ajax({
        type: "POST",
        url: "/",
        data: $(this).serialize(),
        success: function (response) {
            $('#msg').val('')

            $(".media-list")
                .append(`<li class="media-bot">${response.answer}<hr/></li>`);

            $(".fixed-panel")
                .stop()
                .animate({ scrollTop: $(".fixed-panel")[0].scrollHeight }, 1000)

            msg.text = answer
            speechSynthesis.speak(msg)

        }, error: error => console.log(error)
    })
}) 