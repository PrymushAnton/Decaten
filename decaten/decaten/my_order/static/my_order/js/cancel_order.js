$('document').ready(function() {
    $('.cancel_button').click(function(e) {
        var id = $(this).attr('id')
        e.preventDefault();
        $.ajax({
            url: '/cancel_order/',
            type: "POST",
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                id: id,
            },
            success: function() {
                // console.log($('.cancel_button').attr('id'))
                $('.order_status_'+id).remove()
                $(".header_of_order_"+id).append(`<h4 class='order_status canceled'>Статус: Скасовано</h4>`)
                $('.div_buttons_form_'+id).empty()
            }
        })
    })
    
})