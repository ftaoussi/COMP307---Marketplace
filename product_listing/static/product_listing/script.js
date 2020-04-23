

$('.single-filter-option').click(function() {
	console.log($(this).html())
	$(this).toggleClass('selected')

	displayListings();
});

function displayListings() {
	var selectedFilters = $('.selected');

	if (selectedFilters.length == 0) {
		console.log('selectedFilters is empty')
		$('.single-filter-option').css('color', 'black')
		$('.listing').css('display', 'inline')
	}
	else {
		console.log('entering else block')
		$('.single-filter-option').css('color', '#777777')
		selectedFilters.css('color', 'black')
		$('.listing').each(function( i ) {
			if ( $(this).is(selectedFilters)) {
				console.log($(this))
				$(this).css('display', 'inline');
			} else {
				$(this).css('display', 'none');
			}
			if ($(this).hasClass('test')) {
				$(this).css('display', 'inline');
			}
		});
	}
}