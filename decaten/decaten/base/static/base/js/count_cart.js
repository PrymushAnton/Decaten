$('.document').ready(function(){
    $.ajax({
        url: '../count_cart/',
        type: "GET",
        data: {},
        success: function(data){
            if (data.count_cart > '99'){
                $("#count_cart").html('99+')
            }
            if (data.count_cart == '0'){
                $('#count_cart').css('display', 'none');
            } else{
                $('#count_cart').css('display', 'inline');
            }
            
            
            // if ($('#count_cart').text() == '0'){
            //     $("#count_cart").css('display', 'none');
            // } else {
            //     $("#count_cart").css('display', 'block');
            //     $("#count_cart").html(data.count_cart)
            // }
        }
    })
})