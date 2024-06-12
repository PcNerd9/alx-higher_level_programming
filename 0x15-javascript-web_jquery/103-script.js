$(document).ready(function() {
	function fetchTranslation() {
		const langCode = $('#language_code').val();
		const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`;

		$.get(url, function(data) {
			$('#hello').text(data.hello);
		});
	}

	$('#btn_translate').click(function() {
		fetchTranslation();
	});

	$('#language_code').keypress(function(event) {
		if (event.which == 13) {
			fetchTranslation();
		}
	})
});
