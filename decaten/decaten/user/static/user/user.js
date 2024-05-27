// $('.btn-outline-secondary').attr('name')
$("li button[name='ua']").click(function()
{
    $('.btn-outline-secondary').html('+380');
    $('.btn-outline-secondary').attr('name', 'ua');
});

$("li button[name='usa']").click(function()
{
    $('.btn-outline-secondary').html('+(1)415');
    $('.btn-outline-secondary').attr('name', 'usa');
});