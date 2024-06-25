$(document).ready(function(){
    $('.burger_icon').click(function(){
        // let height = $('.carousel_el').height()

        // $('.carousel_container').css('height', height)
        
        $('.header_list').attr('id', 'open')
        $(".burger_close").attr('id', 'burger_open_icon')
        $('.burger_icon').attr('id', 'burger_close_icon')
        // $(".carousel_el").attr('id', 'carousel_close')

        // $('#carouselExample').css('display', 'none')
    })

    $('.burger_close').click(function(){
        // $('.carousel_container').css('height', 'none')

        // $('.carousel_container').removeAttr('style')
        $('.header_list').removeAttr('id')
        $(".burger_close").attr('id', 'burger_close_icon')
        $('.burger_icon').attr('id', 'burger_open_icon')
        // $(".carousel_el").removeAttr('id')
        // $('#carouselExample').css('display', 'block')
    })

})

