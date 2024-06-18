$(document).ready(function() {

    $(".minus").click(function(e){
        e.preventDefault()
        $.ajax({
            url: 'minus_count/',
            type: "POST",
            data: {
                product_id: $(this).val(),
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function(data){
                console.log(data)
                if (data.count > 0) {
                    $('.product_count_'+`${data.product_id}`).html(data.count)
                } 
                if (data.count < 1) {
                    $(".card_"+`${data.product_id}`).remove()
                    $('.content').append(
                        `<div class="d-flex flex-column align-items-center">
                            <h2>Кошик порожній!</h2>
                            <img src="{% static 'cart/icons/cart.svg' %}" alt="" style="width: 200px;">
                        </div>`
                    )
                }
                
            }
        })
    })
})
