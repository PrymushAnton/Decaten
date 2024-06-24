$(document).ready(function() {
    const forms = $("form");
    const buttons = $("button[type='button'].btn");
    console.log(buttons)
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
                            console.log(fieldNames)
                            $("#surename").removeClass('is-invalid');
                            $("#name").removeClass('is-invalid');
                            $("#number").removeClass('is-invalid');
                            $("#invalidCheck").removeClass('is-invalid');
                            fieldNames.forEach((element) => {
                                if (['name', 'surename', 'number', 'sUser', 'terms_conditions'].includes(element)){
                                    if (element == 'sUser'){
                                        $("form#postInfo").prop('hidden', false)
                                    } else {
                                        $("form#postInfo").prop('hidden', true)
                                        $("form#payInfo").prop('hidden', true)
                                        if (element == 'terms_conditions'){
                                            console.log(1)
                                            $("#invalidCheck").addClass('is-invalid');
                                        }else if (element == 'number'){
                                            $("#number").addClass('is-invalid');
                                        } else if (element == 'surename'){
                                            $("#surename").addClass('is-invalid');
                                        } else if (element =='name'){
                                            $("#name").addClass('is-invalid');
                                        }
                                        
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
