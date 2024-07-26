$(document).ready(function() {
    $(".minus").click(function(e){
        e.preventDefault()
        $.ajax({
            url: 'minus_count/',
            type: "POST",
            data: {
                product_id: $(this).val(),
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function(data){
                if (data.count > 0) {
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
                if (data.count < 1) {
                    $(".card_"+`${data.product_id}`+'_'+`${data.flavour_id}`).remove()

                    
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
                if (data.count_cart < 1){
                    $('.error_empty').css('display', 'flex')
                    if ($('.cart').css('display') == 'none'){
                        $('#count_cart_phone').css('display', 'none')
                    } else {
                        $('#count_cart').css('display', 'none')
                    }
                    
                }

                if ($('.error_empty').css('display') == 'flex') {
                    $(".make_order").css('display', 'none')
                }
                const toast_danger = document.getElementById('danger_toast')
                const toastDangerBootstrap = bootstrap.Toast.getOrCreateInstance(toast_danger)
                toastDangerBootstrap.hide()
                
            }
        })
    })
})
