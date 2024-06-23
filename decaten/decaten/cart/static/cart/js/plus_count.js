$(document).ready(function() {

    $(".plus").click(function(e){
        e.preventDefault()
        $.ajax({
            url: 'plus_count/',
            type: "POST",
            data: {
                product_id: $(this).val(),
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function(data){
                console.log(".card_"+`${data.product_id}`+'_'+`${data.flavour_id}`)
                $('.product_count_'+`${data.product_id}`+'_'+`${data.flavour_id}`).html('Кількість: '+data.count)
            }
        })
    })
})
