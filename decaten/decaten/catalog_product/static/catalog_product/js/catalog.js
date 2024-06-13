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
                            <a href="#" class="card d-flex justify-content-around align-items-center shadow" style="width: 18rem; height: 24rem;">
                                <img class="img-fluid m-2" src="../media/${obj.image}" alt="">
                                <h4>${obj.name}</h4>
                                <p>${obj.price} грн.</p>
                            </a>
                        `
                        $(".products").append(product_el)
                    }
                    

                }
            }
        })    
    })
})

