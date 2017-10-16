***Description***
This is a web application which takes in user input through a form and sends that information to Flask through a request. It then uses that data to find information for the nearest deputy head for a given administrative area through Google's Civic Information API. We then use a combination of this representative's data and the form data to generate a letter through Lob's API.

***To Run:***
* FYI: This was run on a Windows machine.
* Have Python 3 and pip installed (always preferable to have this in a virtualenv/Anaconda environment)
* Clone this repository and navigate to the project directory
* In terminal, type ```pip install -r requirements.txt``` to install all the necessary modules
* Input the necessary API keys in the api_keys.py file
* In terminal, type ```python api.py```
* Go to localhost:5000

After you submit a form, you will see a link to the PDF file appear below the title if all operations are completed successfully.