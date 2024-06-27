$(document).ready(function() {
    $(".send").click(function(e) {
        e.preventDefault();
        // console.log($("#area-select").val())
        var data = null
        if ($("#payment_now").prop('checked')){
            data = {
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
                area: $("#area-select").val(),
                city: $("#city-select").val(),
                location: $("#location-select").val(),
                number_of_card: $("#credit_card").val(),
                month: $("#month").val(),
                year: $("#year").val(),
                cvv: $("#cvv").val(),
                last_name: $("#last_name").val(),
                first_name: $("#first_name").val(),
                middle_name: $("#middle_name").val(),
                number: $("#number").val(),
                payment_by_card: true,
            }
        } else {
            data = {
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
                area: $("#area-select").val(),
                city: $("#city-select").val(),
                location: $("#location-select").val(),

                last_name: $("#last_name").val(),
                first_name: $("#first_name").val(),
                middle_name: $("#middle_name").val(),
                number: $("#number").val(),
                payment_by_card: false,
            }
        }

        // console.log($("#payment_now").prop('checked'))
        
        $.ajax({
            url: '/validation/',
            type: "POST",
            data: data,
            success: function(data){
                if (data == '100'){
                    console.log(100)
                } else if (data == '1'){
                    console.log("Заповніть всі поля!")
                } else if (data == '2'){
                    console.log('Введіть коректний номер картки!')
                } else if (data == '3'){
                    console.log('Ввежіть коректний місяць!')
                } else if (data == '4'){
                    console.log('Введіть коректний рік!')
                } else if (data == '5'){
                    console.log('Введіть коректний cvv код!')
                } else if (data == '6'){
                    console.log('Введіть прізвище коректно!')
                } else if (data == '7'){
                    console.log("Введіть ім'я коректно!")
                } else if (data == '8'){
                    console.log("Введіть по батькові коректно!")
                } else if (data == '9'){
                    console.log("Введіть телефон коректно!")
                }  
            }
        })
    })
})