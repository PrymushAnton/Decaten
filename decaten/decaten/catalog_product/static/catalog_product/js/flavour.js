
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
                    try{
                        // if (data.flavour.count_of_product)
                        console.log(obj.count_of_product)
                        if (obj.count_of_product > 0){
                            class_image = '.image_flavour' + obj.for_product_id
                            $(class_image).attr('src', '../../media/' + obj.image)
                            $('.add_to_cart').prop('disabled', false)
                            $(".no_product_error").css('display', 'none')
                        } else {
                            class_image = '.image_flavour' + obj.for_product_id
                            $(class_image).attr('src', '../../media/' + obj.image)
                            $('.add_to_cart').prop('disabled', true)
                            $(".no_product_error").css('display', 'block')
                        }
                        

                    } catch {
                        class_image = '.image_flavour' + obj.for_product_id
                        $(class_image).attr('src', '../../media/' + obj.image)
                    }
                    
                }
            }
        })
    })
})

