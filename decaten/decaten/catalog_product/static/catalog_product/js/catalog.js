$(document).ready(function(){
    $('.send_filters').click(function(e){
        e.preventDefault();
        var filters = document.querySelectorAll('.form-check-input')
        var filters_true = []
        for (let filter of filters){
            console.log(filter.checked)
            if (filter.checked) {
                filters_true.push(filter.value)
            }
        }
        // console.log(filters_true)
        var all_inputs = document.querySelectorAll('.product_id_image')


        $.ajax({
            url: 'filter_products/',
            type: "POST",
            data: {
                filters_true: filters_true.toString(),
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function(data){
                for (let el of $('.card')){
                    $('.card').removeClass('filtered')
                    $('.card').addClass('d-flex')
                    $('.card').removeClass('d-none')
                }

                for (let product of data.products){
                    for (let input of all_inputs) { 
                        for (let obj of product) {
                            if (input.value == obj.id){
                                if (!($(".product_"+input.value).hasClass('filtered'))) {
                                    $(".product_"+input.value).addClass('filtered')
                                }
                                
                            }
                        }
                    }
                }
                for (let product of data.products){
                    for (let input of all_inputs) { 
                        for (let obj of product) {
                            if (input.value != obj.id) {
                                if (!($(".product_"+input.value).hasClass('filtered'))){
                                    $(".product_"+input.value).removeClass('d-flex')
                                    $(".product_"+input.value).addClass('d-none')
                                    
                                }

                            }
                        }
                    }
                }

            }
        })  
    })
})

