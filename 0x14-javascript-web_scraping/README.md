# JavaScript Web Scraping
This project is a collection of JavaScript scripts that perform various web scraping tasks using the request module and different APIs.


-  0-readme.js: Reads and prints the content of a file in UTF-8 encoding. The first argument is the file path. If an error occurred during the reading, prints the error object.

-  1-writeme.js: Writes a string to a file in UTF-8 encoding. The first argument is the file path and the second argument is the string to write. If an error occurred during the writing, prints the error object.

-  2-statuscode.js: Displays the status code of a GET request. The first argument is the URL to request. The status code is printed like this: code: <status code>.

-  3-starwars_title.js: Prints the title of a Star Wars movie where the episode number matches a given integer. The first argument is the movie ID. Uses the Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id.

-  4-starwars_count.js: Prints the number of movies where the character “Wedge Antilles” is present. The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/. Wedge Antilles is character ID 18.

-  5-request_store.js: Gets the contents of a webpage and stores it in a file. The first argument is the URL to request and the second argument is the file path to store the body response. The file is UTF-8 encoded.

-  6-completed_tasks.js: Computes the number of tasks completed by user id. The first argument is the API URL: https://jsonplaceholder.typicode.com/todos. Only prints users with completed tasks.

-  100-starwars_characters.js: Prints all characters of a Star Wars movie. The first argument is the Movie ID. Displays one character name by line. Uses the Star wars API.

-  101-starwars_characters.js: Prints all characters of a Star Wars movie in the same order of the list “characters” in the /films/ response. The first argument is the Movie ID. Displays one character name by line. Uses the Star wars API.