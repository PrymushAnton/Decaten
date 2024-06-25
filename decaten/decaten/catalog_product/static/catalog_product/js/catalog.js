$(document).ready(function(){
    $('.send_filters').click(function(e){
        e.preventDefault();
        var filters = document.querySelectorAll('.form-check-input')
        var filter_categories = document.querySelectorAll('#filter_category_phone')
        var filters_true = []
        var filter_true_phone = []
        // for (let filter_category of filter_categories){
        //     console.log(123)
        //     var temp_list = []
        //     var second_div = first_div.querySelectorAll('.form-check')
        //     var input = second_div.querySelectorAll('input')
        //     console.log(input)
        //     for (let filter of filters){
        //         // console.log(321)
        //         if (filter.checked) {
        //             temp_list.push(
        //                 filter.value,
        //             )
        //         }
                
        //     }
        //     filters_true.push(temp_list)
        // }
        var count = 0
        var count_old = count


        var divs = document.querySelectorAll('.filter_category_pc')
        
        for (let div of divs){
            var temp_list = []
            var div_check = div.querySelectorAll('.check_pc')
            for (let div_obj of div_check){
                var input = div_obj.querySelector('input')
                if (input.checked){
                    temp_list.push(parseInt(input.value))
                }
                
            }
            filters_true.push(temp_list)
        }
        // console.log(filters_true)
        // console.log(JSON.stringify(filters_true))
        var divs_phone = document.querySelectorAll('.filter_category_phone')
        
        for (let div_phone of divs_phone){
            var temp_list = []
            var div_check = div_phone.querySelectorAll('.check_phone')
            for (let div_obj of div_check){
                var input = div_obj.querySelector('input')
                if (input.checked){
                    temp_list.push(parseInt(input.value))
                }
                
            }
            filter_true_phone.push(temp_list)
        }

        var all_inputs = document.querySelectorAll('.product_id_image')

        // var name_of_filters = document.querySelectorAll('.form-check-input')
        // var ids_of_name_of_filters = []
        // for (let filter of name_of_filters){
        //     if (filter.checked) {
        //         ids_of_name_of_filters.push(filter.dataset.names)
        //     }
        // }
        // console.log(ids_of_name_of_filters)
        // console.log(filters_true)

        var max_price = null
        var min_price = null
        var filters = null

        if ($('.filters').css('display') == 'none'){
            max_price = $('.input-max-phone').val()
            min_price = $('.input-min-phone').val()
            filters = filter_true_phone
        } else {
            max_price = $('.input-max').val()
            min_price = $('.input-min').val()
            filters = filters_true
        }

        $.ajax({
            url: 'filter_products/',
            type: "POST",
            data: {
                filters_true: JSON.stringify(filters),
                // name_of_filters: ids_of_name_of_filters.toString(),
                max_price: max_price,
                min_price: min_price,
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function(data){
                // for (let el of $('.card_of_product')){
                //     $('.card_of_product').removeClass('filtered')
                //     $('.card_of_product').css('display', 'flex')
                //     // $('.card_of_product').addClass('d-flex')
                //     // $('.card_of_product').removeClass('d-none')
                // }

                
                // for (let product of data.products){
                //     console.log(product.id)
                //     $(".product_"+product.id).addClass('filtered')
                    
                // }

                // for (let el of $('.card_of_product')){
                //     console.log(el)
                //     if (!el.hasClass('filtered')){
                //         $('.card_of_product').removeClass('filtered')
                //         $('.card_of_product').css('display', 'none')
                //     }
                    
                // }
                // console.log(data.products)
                // console.log(data.error)
                // console.log(123)
                if (data.products.length != 0){
                    // console.log(data.products.length)
                    $('#error').css('display', 'none')
                    $('.card_of_product').css('display', 'none')
                    for (let product of data.products){
                        // console.log(product)
                        // console.log(product)
                        $('.product_'+product.id).css('display', 'flex')
                    }

                } else if (data.error != 1){
                    $('.card_of_product').css('display', 'flex')
                    $('#error').css('display', 'none')
                } else if (data.error == 1){
                    $('.card_of_product').css('display', 'none')
                    $('#error').css('display', 'block')
                }
                




                // for (let product of data.products){
                //     for (let input of all_inputs) { 
   
                //         if (input.value == product.id){
                //             if (!($(".product_"+input.value).hasClass('filtered'))) {
                //                 $(".product_"+input.value).addClass('filtered')
                //             }
                            
                //         }

                //     }
                // }
                // for (let product of data.products){
                //     for (let input of all_inputs) { 
                //             if (input.value != product.id) {
                //                 if (!($(".product_"+input.value).hasClass('filtered'))){
                //                     $(".product_"+input.value).removeClass('d-flex')
                //                     $(".product_"+input.value).addClass('d-none')
                                    
                //                 }

                //             }
                //     }
                // }



            }
        })  
    })
})

