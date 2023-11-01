// Get from an api

$.get('https://swapi.co/api/people/5/?format=json', function (body) {
   $('DIV#character').text(body['name']);
 });
