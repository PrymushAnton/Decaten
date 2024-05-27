// $('.btn-outline-secondary').attr('name')
$("li button[name='ua']").click(function()
{
    $('.btn-outline-secondary').html('+380');
    $('input[name="region"]').attr('name', 'ua');
});

$("li button[name='usa']").click(function()
{
    $('.btn-outline-secondary').html('+(1)415');
    $('input[name="region"]').attr('name', 'usa');
});