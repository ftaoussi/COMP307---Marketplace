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

	console.log('here are the selected filters')
	var $selectedFilters = $('.selected').each(function () {
		console.log($(this).html())
		selectedClasses.push($(this).html())
	}); 

	console.log("selectedClasses: " + selectedClasses)

	if ($selectedFilters.length == 0) {
		console.log('$selectedFilters is empty')
		$('.single-filter-option').css('color', 'black')
		$('.listing').fadeIn( "fast" )
	}
	else {
		console.log('$selectedFilters is not empty')
		$('.single-filter-option').css('color', '#777777')
		$('.selected').css('color', 'black')
		console.log(typeof selectedClasses)
		// console.log($selectedFilters)
		$('.listing').each(function( i ) {
			console.log($(this))
			if (shouldListingDisplay(selectedClasses, this.classList)) {
				console.log(shouldListingDisplay(selectedClasses, this.classList))
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