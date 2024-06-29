$('document').ready(function() {
    $('.sent_button').click(function(e) {
        var id = $(this).attr('id')
        e.preventDefault();
        $.ajax({
            url: '/sent_order/',
            type: "POST",
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                id: id,
            },
            success: function() {
                // console.log($('.cancel_button').attr('id'))
                $('.order_status_'+id).remove()
                $(".header_of_order_"+id).append(`<h4 class='order_status sent'>Статус: Відправлено</h4>`)
                // $('.form_cancel_'+id).css('display', 'none');
                $('.div_buttons_form_'+id).empty()
                console.log($('.div_buttons_form_'+id))
                $('.div_buttons_form_'+id).append(`
                    <button class="btn btn-danger cancel_button" id="{{order.id}}">Відмінити</button>
                    <button class="btn btn-primary arrived_button" id="{{order.id}}">Доставлено</button>
                `)
            }
        })
    })
    
})