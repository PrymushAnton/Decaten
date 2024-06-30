$(document).ready(function() {
    $(".delete").click(function(e){
        e.preventDefault()
        $.ajax({
            url: 'delete_product/',
            type: "POST",
            data: {
                product_id: $(this).val(),
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function(data){
                $(".card_"+`${data.product_id}`+'_'+`${data.flavour_id}`).remove()
                if (data.count_cart == '0'){
                    $('.error_empty').css('display', 'flex')
                    if ($('.cart').css('display') == 'none'){
                        $('#count_cart_phone').css('display', 'none')
                    } else {
                        $('#count_cart').css('display', 'none')
                    }

                } else {
                    if ($('.cart').css('display') == 'none'){
                        $('#count_cart_phone').html(data.count_cart)
                    } else {
                        $('#count_cart').html(data.count_cart)
                    }
                }
                if ($('.error_empty').css('display') == 'flex') {
                    $(".make_order").css('display', 'none')
                }
            }
        })
    })
})
