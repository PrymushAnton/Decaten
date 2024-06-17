
$(document).ready(function() {

    $(".add_to_cart").click(function(e){
        e.preventDefault()
        $.ajax({
            url: 'add_to_cart/',
            type: "POST",
            data: {
                product_id: $('.id_product').val(),
                selector: $('select').val(),
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function(data){
                console.log(data)
            }
        })
    })
})
