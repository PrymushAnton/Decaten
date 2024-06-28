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
                console.log(data.product_id)
                console.log(".card_"+`${data.product_id}`+'_'+`${data.flavour_id}`)
                $(".card_"+`${data.product_id}`+'_'+`${data.flavour_id}`).remove()
                // $('.content').append(
                //     `<div class="d-flex flex-column align-items-center">
                //         <h2>Кошик порожній!</h2>
                //         <img src="" alt="" style="width: 200px;">
                //     </div>`
                // )
                // console.log($('.products').contents().length)
                // if ($('.products').contents().length == 0){
                    
                //     console.log(123)
                // }
                if (data.count_cart == '0'){
                    $('.error_empty').css('display', 'flex')
                    $('#count_cart').css('display', 'none')

                } else {
                    $('#count_cart').css('display', 'inline')
                    $('#count_cart').html(data.count_cart)
                }
                console.log($('.error_empty').css('display'))
                if ($('.error_empty').css('display') == 'flex') {
                    $(".make_order").css('display', 'none')
                }
            }
        })
    })
})
