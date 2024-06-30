
$(document).ready(function() {
    $(".add_to_cart").click(function(e){
        e.preventDefault()
        $.ajax({
            url: '../../add_to_cart/',
            type: "POST",
            data: {
                product_id: $('.id_product').val(),
                selector: $('select').val(),
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
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
            }
        })
    })
})
