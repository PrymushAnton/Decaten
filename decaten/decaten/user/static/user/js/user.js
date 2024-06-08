// $('.btn-outline-secondary').attr('name')
// $("li button[name='ua']").click(function()
// {
//     $('.btn-outline-secondary').html('+380');
//     $('input[name="region"]').attr('name', '380');
// });

// $("li button[name='usa']").click(function()
// {
//     $('.btn-outline-secondary').html('+(1)415');
//     $('input[name="region"]').attr('name', '415');
// });

$(document).ready(
    $("#send").click(function(e){
        e.preventDefault()
        $.ajax({ 
            url: '/validate_account/',
            type: "POST",
            data: {
                username: $('.username').val(),
                email: $('.email').val(),
                number: $('.number').val(),
                password: $('.password').val(),
                password_confirmation: $('.password_confirmation').val(),
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function (success){
                if (success == '1') {
                    var inputs = document.querySelectorAll('input')
                    for (var input of inputs) {
                        if (input.classList.contains('is-invalid')) {
                            input.classList.remove('is-invalid')
                        }
                        if (input.value == ''){
                            input.classList.add('is-invalid')
                            $(".invalid-feedback").html('Заповніть це поле!')
                        }
                    }
                    $(".invalid-feedback").html('Заповніть це поле!')
                    console.log(1)
                } else if (success == '2') {
                    $("input").removeClass('is-invalid')
                    $(".email").addClass('is-invalid')
                    $(".invalid-feedback").html('Дана пошта вже використовується!')
                    console.log(2)
                } else if (success == '3') {
                    $("input").removeClass('is-invalid')
                    $(".password_confirmation").addClass('is-invalid')
                    $(".invalid-feedback").html('Паролі не співпадають!')
                    $('.password_confirmation').val('')
                    console.log(3)
                }
                if (success == '5'){
                    console.log(4)
                    window.location.href = '/'                    
                    window.location.reload()
                }
            },
        })
    })
)