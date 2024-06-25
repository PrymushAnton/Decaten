$(document).ready(function() {
    // $("#gpay-button-online-api-id").prop('type', 'submit');
    // $("#gpay-button-online-api-id").prop('value', '1');
    $("#gpay-button-online-api-id").prop('name', 'pay_btn');
    $('#card_select').on('change', function() {
        if ($('#card_select').val() == 'GP'){
            $("#btn_pay").prop('hidden', false)
            $("#subPayBtn").prop('hidden', true)
            $(".not_GP").each((index, elem) => {
                $(elem).prop('hidden', true)
            })
            $(".not_GP input").each((index, elem) => {
                $(elem).prop('required', false)
            })
            
        } else {
            $("#btn_pay").prop('hidden', true)
            $("#subPayBtn").prop('hidden', false)
            $(".not_GP").each((index, elem) => {
                $(elem).prop('hidden', false)
            })
            $(".not_GP input").each((index, elem) => {
                $(elem).prop('required', true)
            })
        }
    });
});



$(document).ready(function() {
    const forms = $("form");
    const buttons = $("button[type='button'].btn");
    forms.each((index, element) => {
        $(element).on('submit', function(event) {
            event.preventDefault();
            var formData = $(this).serialize();
            if (this.checkValidity()) {
                $.ajax({
                    url: '#',
                    type: 'POST',
                    data: formData,
                    success: function(response) {
                        if (response){
                            var regex = /\('(.*?)',/g;
                            var fieldNames = [];
                            var match;
                            while ((match = regex.exec(response)) !== null) {
                                fieldNames.push(match[1]); // Захватываем первую группу (имя поля)
                            }
                            $("#surename").removeClass('is-invalid');
                            $("#name").removeClass('is-invalid');
                            $("#number").removeClass('is-invalid');
                            $("#invalidCheck").removeClass('is-invalid');
                            $('#postCheck').removeClass('is-invalid');
                            $('#post_index').removeClass('is-invalid');
                            $('#address').removeClass('is-invalid');
                            $('#sending_option').removeClass('is-invalid');
                            $('#post_select').removeClass('is-invalid');
                            fieldNames.forEach((element) => {
                                if (['name', 'surename', 'number', 'sUser', 'terms_conditions'].includes(element)){
                                    if (element == 'sUser'){
                                        $("form#postInfo").prop('hidden', false)
                                    } else {
                                        $("form#postInfo").prop('hidden', true)
                                        $("form#payInfo").prop('hidden', true)
                                        if (element == 'terms_conditions'){
                                            $("#invalidCheck").addClass('is-invalid');
                                        }else if (element == 'number'){
                                            $("#number").addClass('is-invalid');
                                        } else if (element == 'surename'){
                                            $("#surename").addClass('is-invalid');
                                        } else if (element =='name'){
                                            $("#name").addClass('is-invalid');
                                        }
                                    }
                                } else if (['post', 'sending_option', 'address', 'post_index', 'check_post', 'sPost'].includes(element)){
                                    if (element == 'sPost'){
                                        $("form#payInfo").prop('hidden', false)
                                    } else if (element == 'check_post'){
                                        $('#postCheck').addClass('is-invalid');
                                    } else if (element == 'post_index'){
                                        $('#post_index').addClass('is-invalid');
                                    } else if (element == 'address'){
                                        $('#address').addClass('is-invalid');
                                    } else if (element == 'sending_option'){
                                        $('#sending_option').addClass('is-invalid');
                                    } else if (element == 'post'){
                                        $('#post_select').addClass('is-invalid');
                                    }
                                }
                            })
                            
                        }
                    },
                    error: function(xhr, status, error) {
                        console.error('Error:', error);
                    }
                })
                    
                };
            });
        });
    });
