
$(document).ready(function() {
    $.ajax({
        url: 'error_empty/',
        type: 'GET',
        data: {
            // csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
        },
        success: function(data) {
            console.log(data)
            if (data.products.length == 0){
                $('.error_empty').css('display', 'flex')
            }
            // for (let obj of data.flavour){
            //     class_image = '.image_flavour' + obj.for_product_id
            //     $(class_image).attr('src', '')
            //     $(class_image).attr('src', '../media/' + obj.image)
            //     $('select').attr('data-previous', obj.id)
            // }
        }
    })
})

