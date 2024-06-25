
$(document).ready(function() {
    $('select').on('input', function() {
        $.ajax({
            url: 'product_flavour_main/',
            type: 'GET',
            data: {
                // csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                value_of_selector: $(this).val(),
            },
            success: function(data) {
                for (let obj of data.flavour){
                    class_image = '.image_flavour' + obj.for_product_id
                    // $(class_image).attr('src', '')
                    $(class_image).attr('src', '../media/' + obj.image)
                }

            }
        })
    })
})