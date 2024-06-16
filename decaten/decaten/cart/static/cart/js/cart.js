
// $(document).ready(function() {
//     $('select').on('input', function() {
//         $.ajax({
//             url: 'get_flavour_image/',
//             type: 'POST',
//             data: {
//                 csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
//                 value_of_selector: $(this).val(),
//                 previous_value_of_selector: $(this).attr('data-previous'),
//             },
//             success: function(data) {
//                 console.log(123)
//                 for (let obj of data.flavour){
//                     class_image = '.image_flavour' + obj.for_product_id
//                     $(class_image).attr('src', '')
//                     $(class_image).attr('src', '../media/' + obj.image)
//                     $('select').attr('data-previous', obj.id)
//                 }
//             }
//         })
//     })
// })

