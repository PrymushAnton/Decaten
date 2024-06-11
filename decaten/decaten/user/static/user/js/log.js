$(document).ready(function() {
    $('.send').click(function(e){
        e.preventDefault()
        $.ajax({
            url: '/log_in_account/',
            type: 'POST',
            data: {
                email: $('.email').val(),
                password: $('.password').val(),
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function(data){
                if (data == '1') {
                    var inputs = document.querySelectorAll('input')
                    for (var input of inputs) {
                        if (input.classList.contains('is-invalid')) {
                            input.classList.remove('is-invalid')
                        }
                        if (input.value == ''){
                            input.classList.add('is-invalid')
                            // $(".invalid-feedback").html('Заповніть це поле!')
                        }
                    }
                    $(".invalid-feedback").html('Заповніть це поле!')
                    console.log(1)
                } else if (data == '2') {
                    $("input").removeClass('is-invalid')
                    $(".email").addClass('is-invalid')
                    $(".invalid-feedback").html('Пошта не зареєстрована!')
                    console.log(2)
                    
                } else if (data == '3') {
                    $("input").removeClass('is-invalid')
                    $(".password").addClass('is-invalid')
                    $(".invalid-feedback").html('Неправильний пароль!')
                    $('.password').val('')
                    
                    console.log(3)
                } else if (data == '4') {
                    console.log(5)
                    $('.ajax_text').html('Ви зареєстровані!')
                    window.location.href = '/'                    
                    window.location.reload()
                }
            }
        })
    })
})