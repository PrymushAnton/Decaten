$(document).ready(function(){
    $('.send_filters').click(function(e){
        e.preventDefault();
        var filters = document.querySelectorAll('.form-check-input')
        var filters_true = []
        for (let filter of filters){
            if (filter.checked) {
                filters_true.push(filter.value)
                // console.log(filter.value)
                // console.log(1)
            }
        }

        var all_inputs = document.querySelectorAll('.product_id_image')

        // console.log(filters_true)
        // console.log(filters_true.toString())
        $.ajax({
            url: 'filter_products/',
            type: "POST",
            data: {
                filters_true: filters_true.toString(),
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function(data){
                // console.log($('.card'))
                for (let el of $('.card')){
                    $('.card').removeClass('filtered')
                    $('.card').addClass('d-flex')
                    $('.card').removeAttr('style')
                }
                
                // $('.card').addClass('d-flex')
                // $(".card").css('display', 'flex')
                for (let product of data.products){
                    for (let input of all_inputs) { 
                        for (let obj of product) {
                            if (input.value == obj.id){
                                if (!($(".product_"+input.value).hasClass('filtered'))) {
                                    $(".product_"+input.value).addClass('filtered')
                                    // console.log(".product_"+input.value)
                                    // console.log($(".product_"+input.value).hasClass('filtered'))
                                    // console.log(!($(".product_"+input.value).hasClass('filtered')))
                                }
                                
                            }
                        }
                    }
                }
                for (let product of data.products){
                    for (let input of all_inputs) { 
                        for (let obj of product) {
                            // console.log(input.value)
                            // console.log(obj.id)
                            // console.log('---------------')
                            if (input.value != obj.id) {
                                // console.log(123)
                                // console.log('^^^^^^^^^')
                                // console.log($(".product_"+product.id).prop('tagName'))
                                // console.log(".product_"+input.value)
                                // console.log(input.value)
                                if (!($(".product_"+input.value).hasClass('filtered'))){
                                    // console.log('display', '.product_'+input.value)
                                    $(".product_"+input.value).removeClass('d-flex')
                                    $(".product_"+input.value).css('display', 'none')
                                }
                                
                                
                                // console.log(123)
                            }
                        }
                    }
                }




                // $(".products").empty()
                // for (let product of data.products){
                //     for (let obj of product){
                //         for (let flavour of data.flavours){
                //             for (let obj_flavour of flavour) {
                //                 if (obj_flavour.for_product_id == obj.id){
                //                     console.log("True")
                //                     let option
                //                     let product_el = `
                //                         <input type="hidden" value="{{product.id}}" class="product_id_image">
                //                         <a href="#" class="card d-flex justify-content-around align-items-center shadow" style="width: 18rem; height: 24rem;">
                //                             <img class="w-75 m-2 image_flavour${obj.id}" src="../media/${obj_flavour.image}" alt="">
                //                             <h4>${obj.name}</h4>
                //                             <p>${obj.price} грн.</p>
                //                             <select name="${product.name}" id="${product.name}" class="form-select w-75 mb-3">
                                                
                //                             </select>
                //                         </a>
                //                     `
                //                     $(".products").append(product_el)
                //                     // <option value="${obj_flavour.id}">${obj_flavour.name}</option>
                //                     for (let flavour of data.flavours) {
                //                         for (let obj of flavour) {
                //                             console.log(obj.name)
                //                             option = `<option value="${obj.id}">${obj.name}</option>`
                                            
                //                             $('#'+product.name).append(option)
                //                         }
                                        
                //                     }
                                    
                //                     break
                //                 } else {
                //                     console.log('error')
                //                     continue
                //                 }
                                
                //             }

                //         }

                //     }
                    
                    

                // }
            }
        })  
    })
})

