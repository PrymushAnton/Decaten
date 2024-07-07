
$(document).ready(function() {
    $('select').on('input', function() {
        $.ajax({
            url: '../../get_flavour_image/',
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                value_of_selector: $(this).val(),
            },
            success: function(data) {
                for (let obj of data.flavour){
                    if (obj.count_of_product > 0){
                        class_image = '.image_flavour' + obj.for_product_id
                        $(class_image).attr('src', '../../media/' + obj.image)
                        $('.add_to_cart').prop('disabled', false)
                        $('.add_to_cart').removeAttr('value')
                        $('.add_to_cart').attr('value', obj.count_of_product)
                        $(".no_product_error").css('display', 'none')
                        $(".amount_on_base").html("Кількість на складі: "+obj.count_of_product+ " шт.")
                    } else {
                        class_image = '.image_flavour' + obj.for_product_id
                        $(class_image).attr('src', '../../media/' + obj.image)
                        $('.add_to_cart').prop('disabled', true)
                        $('.add_to_cart').removeAttr('value')
                        $(".no_product_error").css('display', 'block')
                        $(".amount_on_base").html("")
                    }
                    
                }
            }
        })
    })
})

