/*
	Filter Functionality
*/
 
$('.single-filter-option').click(function() {
	console.log($(this).html())
	$(this).toggleClass('selected')

	displayListings();
});

function displayListings() {
	var selectedClasses = []

	var $selectedFilters = $('.selected').each(function () {
		selectedClasses.push($(this).html())
	}); 

	console.log("selectedClasses: " + selectedClasses)

	if ($selectedFilters.length == 0) {
		$('.single-filter-option').css('color', 'black')
		$('.listing').fadeIn( "fast" )
	}
	else {
		console.log('$selectedFilters is not empty')
		$('.single-filter-option').css('color', '#777777')
		$('.selected').css('color', 'black')
		// console.log($selectedFilters)
		$('.listing').each(function( i ) {
			console.log($(this))
			if (shouldListingDisplay(selectedClasses, this.classList)) {
				$(this).fadeIn('fast')
				this.style.display = 'inline'
			} else {
				console.log(shouldListingDisplay(selectedClasses, this.classList))
				$(this).fadeOut('fast')
			}
		});
	}
}

function shouldListingDisplay(selectedClasses, classList) {
	for (let i = 0; i < selectedClasses.length; i++) {
		if (classList.contains(selectedClasses[i])) {
			return true;
		}
	}
	return false;
}