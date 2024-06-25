$(document).ready(function() {
    $(".delete").click(function(e){
        e.preventDefault()
        $.ajax({
            url: 'delete_product/',
            type: "POST",
            data: {
                product_id: $(this).val(),
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function(data){
                console.log(".card_"+`${data.product_id}`+'_'+`${data.flavour_id}`)
                $(".card_"+`${data.product_id}`+'_'+`${data.flavour_id}`).remove()
                // $('.content').append(
                //     `<div class="d-flex flex-column align-items-center">
                //         <h2>Кошик порожній!</h2>
                //         <img src="" alt="" style="width: 200px;">
                //     </div>`
                // )
                $('.error_empty').css('display', 'flex')
            }
        })
    })
})
