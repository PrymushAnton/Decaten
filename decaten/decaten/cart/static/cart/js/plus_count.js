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
                console.log(data)
                $('.product_count_'+`${data.product_id}`).html('Кількість: '+data.count)
            }
        })
    })
})
