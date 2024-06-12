$(document).ready(function() {
	$('#add_item').click(function() {
		const newItem = $('<li>Item</li>');
		$('ul.mylist').append(newItem);
	});
});
