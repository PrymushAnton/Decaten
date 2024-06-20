
$(document).ready(function() {
    $('select').on('input', function() {
        $.ajax({
            url: 'get_flavour_image/',
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                value_of_selector: $(this).val(),
            },
            success: function(data) {
                for (let obj of data.flavour){
                    try{
                        class_image = '.image_flavour' + obj.for_product_id
                        // $(class_image).attr('src', '')
                        $(class_image).attr('src', '../media/' + obj.image)
                    } catch {
                        class_image = '.image_flavour' + obj.for_product_id
                        // $(class_image).attr('src', '')
                        $(class_image).attr('src', '../../media/' + obj.image)
                    }
                    
                }
            }
        })
    })
})

