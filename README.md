#Git hub profile tracker

basically just pulls names from the github api and stores them in a json file. Mightn't work all that well but im still learning so feedback is appreciated :)

New changes:
-Fixed a line where I accidentally called requests.get twice and once was outside of the try loop.
- This means the http or time out errors might not have ran.
-Added a part where if the data is not found it returns the user back to the main menu.
- Before this would have led to it storing the values as not found rather than not letting them store this data.
-Deletion function now actually saves.
- deletion was firing but not storing itself.
-When viewing or changing a user if you type an incorrect username it now lets you retry rather than simply ending.
- Can attempt to add/remove or view a user more easily.
-Added a .lower to the names input.
- avoids any duplicate values where one might be spelt with capitilisation rather than solely lowercase.
-Changed the change function
- it now deletes the result after it adds a new one to avoid a bug where you could input an incorrect user and it would only delete the current user and not add a new one.
   -hopefully this version is a tiny bit better :)
