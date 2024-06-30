$(document).ready(function() {

    $(".plus").click(function(e){
        e.preventDefault()
        $.ajax({
            url: 'plus_count/',
            type: "POST",
            data: {
                product_id: $(this).val(),
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function(data){
                if (data.plus == 1){
                    $('.product_count_'+`${data.product_id}`+'_'+`${data.flavour_id}`).html('Кількість: '+data.count)
                    $('#price_'+`${data.product_id}`+'_'+`${data.flavour_id}`).html(data.price+' грн')
                    if (data.count_cart > '99'){
                        if ($('.cart').css('display') == 'none'){
                            $('#count_cart_phone').html('99+')
                        } else {
                            $('#count_cart').html('99+')
                        }
                    } else {
                        if ($('.cart').css('display') == 'none'){
                            $('#count_cart_phone').html(data.count_cart)
                        } else {
                            $('#count_cart').html(data.count_cart)
                        }
                    }
                }
                
            }
        })
    })
})
