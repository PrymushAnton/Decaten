$(document).ready(function(){
    $('.send_filters').click(function(e){
        e.preventDefault();

        var filters_true = []
        var filter_true_phone = []

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
                max_price: max_price,
                min_price: min_price,
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function(data){
                if (data.products.length != 0){
                    $('#error').css('display', 'none')
                    $('.card_of_product').css('display', 'none')
                    for (let product of data.products){
                        $('.product_'+product.id).css('display', 'flex')
                    }

                // } else if (data.error != 1){
                //     $('.card_of_product').css('display', 'flex')
                //     $('#error').css('display', 'none')
                } else if (data.error == 1){
                    $('.card_of_product').css('display', 'none')
                    $('#error').css('display', 'block')
                }
            }
        })  
    })
})

