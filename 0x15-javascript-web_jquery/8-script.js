$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data, textStatus) {
	$.each(data.results, function(index, data) {
		$('UL#list_movies').append('<li>'+${data.title}+'</li>');
	});
})
