/*
	List Item Form Styling
*/
 
$('form').addClass('form-group')
$('tr').addClass('form-row col-12 form-group')
$('th').addClass('row form-row col-12 info-label').css('font-weight', 'normal')
$('label').css('margin', '0px')
$('td').addClass('row form-row col-12').css('padding-top', '.2rem')
$('input').addClass('form-control col-12').css('padding', '0px')
$("input[name='image']").removeClass('form-control').addClass('form-control-file d-none').attr('id', 'image').after( "<label id='image-label' for='image'>Select Image</label>" );
$('#image-label').css('background-color', 'white').css('border-radius', '1rem').css('padding', '.4rem 1rem').css('cursor', 'pointer')
$('input[type="submit"]').removeClass('col-12').addClass('col-2 row').css('margin-left', '1rem').css('border-radius', '1rem')