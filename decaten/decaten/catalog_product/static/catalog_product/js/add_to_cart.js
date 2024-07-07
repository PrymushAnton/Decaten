
$(document).ready(function() {
    $(".add_to_cart").click(function(e){
        e.preventDefault()
        $.ajax({
            url: '../../add_to_cart/',
            type: "POST",
            data: {
                product_id: $('.id_product').val(),
                selector: $('select').val(),
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
                count_of_product: $(this).val(),
            },
            success: function(data){
                if ($('.cart').css('display') == 'none'){
                    $('.cart_phone').empty()
                    $('.cart_phone').append(`Кошик<span id="count_cart_phone">${data.count_cart}</span>`)
                } else {
                    $('.cart').empty()
                    $('.cart').append(`<span id="count_cart">${data.count_cart}</span>`)
                    $('.cart').append('Кошик')
                }
                $("#count_cart").css('display', 'inline !important')
                $('#count_cart').html(data.count_cart)

                if (parseInt(data.count_of_product) > parseInt(data.count_of_product_in_cart)){
                    const toast = document.getElementById('success_toast')
                    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toast)
                    
                    const toast_danger = document.getElementById('danger_toast')
                    const toastDangerBootstrap = bootstrap.Toast.getOrCreateInstance(toast_danger)
                    
                    toastDangerBootstrap.hide()
                    toastBootstrap.show()
                } else {
                    const toast = document.getElementById('danger_toast')
                    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toast)

                    const toast_success = document.getElementById('success_toast')
                    const toastSuccessBootstrap = bootstrap.Toast.getOrCreateInstance(toast_success)
                    
                    toastSuccessBootstrap.hide()
                    toastBootstrap.show()
                }

            }
        })
    })
})
