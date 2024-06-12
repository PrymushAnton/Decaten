$(document).ready(function(){
    $('.send_filters').click(function(e){
        e.preventDefault();
        var filters = document.querySelectorAll('.form-check-input')
        var filters_true = []
        for (var filter of filters){
            if (filter.checked) {
                filters_true.push(filter.value)
                // console.log(1)
            }
        }
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
                console.log(data.products)
                $(".products").empty()
                for (let product of data.products){
                    for (let obj of product){
                        
                        let product_el = `
                            <a href="">
                                <div class="product">
                                    <img src="../media/${obj.image}" alt="">
                                    <h3>${obj.name}</h3>
                                    <p>${obj.price} грн.</p>
                                </div>
                            </a>
                        `
                        $(".products").append(product_el)
                    }
                    

                }
            }
        })    
    })
})

