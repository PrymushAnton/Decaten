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
                first_name: $('.first_name').val(),
                last_name: $('.last_name').val(),
                email: $('.email').val(),
                number: $('.number').val(),
                password: $('.password').val(),
                password_confirmation: $('.password_confirmation').val(),
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function (success){
                if (success == '10'){
                    console.log(10)
                    window.location.href = '/'
                    window.location.reload()
                }
                if (success == '1') {
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
                } else if (success == '2') {
                    $("input").removeClass('is-invalid')
                    $(".first_name").addClass('is-invalid')
                    $(".invalid-feedback").html('В імені не повинні бути цифри або спец. символи!')
                    console.log(2)
                } else if (success == '11') {
                    $("input").removeClass('is-invalid')
                    $(".last_name").addClass('is-invalid')
                    $(".invalid-feedback").html('В прізвищі не повинні бути цифри або спец. символи!')
                    console.log(11)
                } else if (success == '3') {
                    $("input").removeClass('is-invalid')
                    $(".email").addClass('is-invalid')
                    $(".invalid-feedback").html('Введіть коректну пошту!')
                    console.log(3)
                } else if (success == '4') {
                    console.log(4)
                    $("input").removeClass('is-invalid')
                    $(".email").addClass('is-invalid')
                    $(".invalid-feedback").html('Дана пошта вже використовується!')
                } else if (success == '5') {
                    console.log(5)
                    $("input").removeClass('is-invalid')
                    $(".number").addClass('is-invalid')
                    $(".invalid-feedback").html('Не вірно введений номер телефону!')
                } else if (success == '6') {
                    console.log(6)
                    $("input").removeClass('is-invalid')
                    $(".number").addClass('is-invalid')
                    $(".invalid-feedback").html('Даний номер телефону вже використовується!')
                } else if (success == '7') {
                    console.log(7)
                    $("input").removeClass('is-invalid')
                    $(".password").addClass('is-invalid')
                    $(".invalid-feedback").html('У паролі повинно бути 8 або більше символів!')
                    $('.password').val('')
                } else if (success == '8') {
                    console.log(8)
                    $("input").removeClass('is-invalid')
                    $(".password_confirmation").addClass('is-invalid')
                    $(".invalid-feedback").html('Паролі не співпадають!')
                    $('.password_confirmation').val('')
                } else if (success == '9') {
                    $('.ajax_text').html("Помилка! Спробуйте пізніше!")
                    console.log(9)
                } else if (success == '12') {
                    $('.ajax_text').html("Ім'я не повинно бути більше 12 символів!")
                    console.log(12)
                } else if (success == '13'){
                    $('.ajax_text').html("Прізвище не повинно бути більше 15 символів!")
                    console.log(13)
                }
                
            },
        })
    })
)