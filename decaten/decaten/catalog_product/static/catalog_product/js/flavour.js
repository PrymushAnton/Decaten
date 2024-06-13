
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
                    class_image = '.image_flavour' + obj.for_product_id
                    console.log(obj.image)
                    $(class_image).attr('src', '')
                    $(class_image).attr('src', '../media/' + obj.image)
                    console.log(123)
                }
                

                // var product_id_image = document.querySelectorAll('.product_id_image')
                // for (product_id of product_id_image) {
                //     let product_id_value = product_id.value
                //     if ($('.image_flavour'+product_id_value).attr('src') == '') {
                        
                //         for (let obj of data.flavours){
                            
                //             if (obj.for_product_id == product_id.value){
                //                 let src = '../media/' + obj.image
                //                 $('.image_flavour'+product_id_value).attr('src', src)
                //                 break
                //             }
                //         }
                //     }
                // }


            }
        })
    })
})

