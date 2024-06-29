$('document').ready(function() {
    $('.success_button').click(function(e) {
        var id = $(this).attr('id')
        e.preventDefault();
        $.ajax({
            url: '/success_order/',
            type: "POST",
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                id: id,
            },
            success: function() {
                // console.log($('.cancel_button').attr('id'))
                $('.order_status_'+id).remove()
                $(".header_of_order_"+id).append(`<h4 class='order_status completed'>Статус: Виконано</h4>`)
                // $('.form_cancel_'+id).css('display', 'none');
                $('.div_buttons_form_'+id).empty()
                
            }
        })
    })
    
})