import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title = []
company_name = []
location_name = []
job_skill = []
result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")
src = result.content
soup = BeautifulSoup(src, "lxml")

# the step find a elements containing info i need **
# --job tittle, job skills, company names, location name
job_titles = soup.find_all("h2", {"class": "css-m604qf"})
company_names = soup.find_all("a", "css-17s97q8")
location_names = soup.find_all("span", "css-5wys0k")
job_Skills = soup.find_all("div", "css-y4udm8")

for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    company_name.append(company_names[i].text)
    location_name.append(location_names[i].text)
    job_skill.append(job_Skills[i].text)
# print(company_name)
# print(location_name)
# print(job_skill)
# csv file
file_list = [job_title, company_name, location_name, job_skill]
exported = zip_longest(*file_list)
with open("/users/islam/desktop/isla_test.csv", "w") as myfile:
    wr = csv.writer(myfile, delimiter=';')
    wr.writerow(["Job Title", "Company Name", "Location", "Skills"])
    wr.writerows(exported)
