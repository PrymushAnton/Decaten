// $(document).ready(function(){
//     $('.burger_icon').click(function(){
//         $('.header_list').attr('id', 'open')
//         $(".burger_close").attr('id', 'burger_open_icon')
//         $('.burger_icon').attr('id', 'burger_close_icon')
//     })

//     $('.burger_close').click(function(){
//         $('.header_list').removeAttr('id')
//         $(".burger_close").attr('id', 'burger_close_icon')
//         $('.burger_icon').attr('id', 'burger_open_icon')
//     })

// })


$(document).ready(function() {
    $('.burger_icon').on('click', function() {
        var offcanvasElement = $('#BurgerOffcanvas');
        var bsOffcanvas = new bootstrap.Offcanvas(offcanvasElement[0]);
        bsOffcanvas.show();
    });
  });