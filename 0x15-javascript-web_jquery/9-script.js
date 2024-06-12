$(document).ready(function() {
	$.get('https://hellsalut.stefanbohacek.dev/?lang=fr', function(data) {
		$('#hello').text(data.hello);
	});
});
