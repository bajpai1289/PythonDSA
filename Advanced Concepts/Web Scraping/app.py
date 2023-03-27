import requests
from bs4 import BeautifulSoup
response = requests.get("https://realpython.github.io/fake-jobs/")
# response.text  # it returns the html content of the web page

soup = BeautifulSoup(response.content, "html.parser")
results = soup.find(id="ResultsContainer")
# print(soup)
jobs = results.find_all("div", class_="card-content")
for job in jobs:
    print(job, end="\n"*2)
