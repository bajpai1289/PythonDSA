import requests
from bs4 import BeautifulSoup
response = requests.get("https://stackoverflow.com/questions")
# response.text  # it returns the html content of the web page

soup = BeautifulSoup(response.text, "html.parser")
questions = soup.select(".question-summary") # get using the css selector
print(questions[0].attrs)
print(questions[0].get("id", 0))
print(questions[0].select_one(".question-hyperlink"))
print(questions[0].select_one(".question-hyperlink").getText())
# iterate over all queesion 
for question in questions:
    print(questions.select_one(".question-hyperlink").getText())
    print(questions.select_one(".vote-count-post").getText())
    



