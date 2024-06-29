$(document).ready(function() {
    $(".send").click(function(e) {
        e.preventDefault();
        // console.log($("#area-select").val())
        var data = null
        // if ($("#payment_now").prop('checked')){
        //     console.log(true)
        // }
        console.log(data)
        // console.log($("#payment_now").prop('checked'))
        
        $.ajax({
            url: '/validation/',
            type: "POST",
            data: {
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
                area: $("#area-select option:selected").text(),
                city: $("#city-select option:selected").text(),
                location: $("#location-select option:selected").text(),
                number_of_card: $("#credit_card").val(),
                month: $("#month").val(),
                year: $("#year").val(),
                cvv: $("#cvv").val(),
                last_name: $("#last_name").val(),
                first_name: $("#first_name").val(),
                middle_name: $("#middle_name").val(),
                number: $("#number").val(),
            },
            success: function(data){
                if (data == '321') {
                    $('.modal').modal('show');
                }

                if (data == '100'){
                    console.log(100)
                    window.location.replace('/')
                    // window.location.href = '/'
                    // window.location.reload()
                } else if (data == '1'){
                    console.log("Заповніть всі поля!")
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
                } else if (data == '2'){
                    console.log('Введіть коректний номер картки!')
                    credit_card
                    $("input").removeClass('is-invalid')
                    $("select").removeClass('is-invalid')
                    $("#credit_card").addClass('is-invalid')
                    $(".invalid-feedback").html('Введіть коректний номер картки!')
                } else if (data == '3'){
                    console.log('Введіть коректний місяць!')
                    $("input").removeClass('is-invalid')
                    $("select").removeClass('is-invalid')
                    $("#month").addClass('is-invalid')
                    $(".invalid-feedback").html('Введіть коректний місяць!')
                } else if (data == '4'){
                    console.log('Введіть коректний рік!')
                    $("input").removeClass('is-invalid')
                    $("select").removeClass('is-invalid')
                    $("#year").addClass('is-invalid')
                    $(".invalid-feedback").html('Введіть коректний рік!')
                } else if (data == '5'){
                    console.log('Введіть коректний cvv код!')
                    $("input").removeClass('is-invalid')
                    $("select").removeClass('is-invalid')
                    $("#cvv").addClass('is-invalid')
                    $(".invalid-feedback").html('Введіть коректний cvv код!')
                } else if (data == '6'){
                    console.log('Введіть прізвище коректно!')
                    $("input").removeClass('is-invalid')
                    $("select").removeClass('is-invalid')
                    $("#last_name").addClass('is-invalid')
                    $(".invalid-feedback").html('Введіть прізвище коректно!')
                } else if (data == '7'){
                    console.log("Введіть ім'я коректно!")
                    $("input").removeClass('is-invalid')
                    $("select").removeClass('is-invalid')
                    $("#first_name").addClass('is-invalid')
                    $(".invalid-feedback").html("Введіть ім'я коректно!")
                } else if (data == '8'){
                    console.log("Введіть по батькові коректно!")
                    $("input").removeClass('is-invalid')
                    $("select").removeClass('is-invalid')
                    $("#middle_name").addClass('is-invalid')
                    $(".invalid-feedback").html('Введіть по батькові коректно!')
                } else if (data == '9'){
                    console.log("Введіть телефон коректно!")
                    $("input").removeClass('is-invalid')
                    $("select").removeClass('is-invalid')
                    $("#number").addClass('is-invalid')
                    $(".invalid-feedback").html('Введіть телефон коректно!')
                } else if (data == '10'){
                    // console.log("Введіть телефон коректно!")
                    $("input").removeClass('is-invalid')
                    $("select").removeClass('is-invalid')
                    $("#area-select").addClass('is-invalid')
                    $(".invalid-feedback").html('Оберіть область!')
                } else if (data == '11'){
                    // console.log("Введіть телефон коректно!")
                    $("input").removeClass('is-invalid')
                    $("select").removeClass('is-invalid')
                    $("#city-select").addClass('is-invalid')
                    $(".invalid-feedback").html('Оберіть місто!')
                } else if (data == '12'){
                    // console.log("Введіть телефон коректно!")
                    $("input").removeClass('is-invalid')
                    $("select").removeClass('is-invalid')
                    $("#location-select").addClass('is-invalid')
                    $(".invalid-feedback").html('Оберіть відділення!')
                } 
            }
        })
    })
})