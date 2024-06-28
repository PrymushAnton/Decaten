
$(document).ready(function() {

    $(".add_to_cart").click(function(e){
        console.log($('.id_product').val(),)
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
                console.log(data)
                $("#count_cart").css('display', 'inline')
                $('#count_cart').html(data.count_cart)
            }
        })
    })
})
