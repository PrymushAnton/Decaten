$(document).ready(function() {
    $.ajax({
        url: 'product_image_main/',
        type: 'GET',
        data: {
        },
        success: function(data) {
            var product_id_image = document.querySelectorAll('.product_id_image')
            for (product_id of product_id_image) {
                let product_id_value = product_id.value
                if ($('.image_flavour'+product_id_value).attr('src') == '') {
                    
                    for (let obj of data.flavours){
                        
                        if (obj.for_product_id == product_id.value){
                            let src = '../media/' + obj.image
                            $('.image_flavour'+product_id_value).attr('src', src)
                            break
                        }
                    }
                }
            }
        }
    })
})