// Adds a LI element to UL.my_list when div#add_item is clicked

$('div#add_item').click(function () {
	$('ul.my_list').append('<li>Item</li>');
});
