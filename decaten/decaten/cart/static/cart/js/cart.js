
$(document).ready(function() {
    $.ajax({
        url: 'error_empty/',
        type: 'GET',
        data: {},
        success: function(data) {
            if (data.products.length == 0){
                $('.error_empty').css('display', 'flex')
            }
        }
    })
})

