import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title = []
company_name = []
location_name = []
job_skill = []
links = []
salary = []
responsibilities = []
job_date = []
page_num = 0
#while True:
#    try:
result = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q=python&start={page_num}")
src = result.content
soup = BeautifulSoup(src, "lxml")
#page_limit = int(soup.find("strong").text)
#if page_num > page_limit // 15:
#    print("pages ended, terminate")
 #           break
        # the step find a elements containing info i need **
        # --job tittle, job skills, company names, location name
job_titles = soup.find_all("h2", {"class": "css-m604qf"})
company_names = soup.find_all("a", "css-17s97q8")
location_names = soup.find_all("span", "css-5wys0k")
job_Skills = soup.find_all("div", "css-y4udm8")
jobTempletes = soup.find_all("div", {"class": "css-1gatmva e1v1l3u10"})
for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    links.append("https://wuzzuf.net"+job_titles[i].find("a").attrs['href'])
    company_name.append(company_names[i].text)
    location_name.append(location_names[i].text)
    job_skill.append(job_Skills[i].text)
for jopTemplete in jobTempletes:
    if jopTemplete.find("div", {"class": "css-do6t5g"}):
        date = jopTemplete.find("div", {"class": "css-do6t5g"})
        dateText = date.text.replace("-", "").strip()
        job_date.append(dateText)
    elif jopTemplete.find("div", {"class": "css-4c4ojb"}):
        date = jopTemplete.find("div", {"class": "css-4c4ojb"})
        dateText = date.text.replace("-", "").strip()
        job_date.append(dateText)
#page_num += 1
#print("page switched")
#    except:
#        print("Errur occurred")
#        break
for link in links:
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src, "lxml")
    requirements = soup.find("div", {"class": "css-1t5f0fr"})
    responsibilities.append(requirements.text)
# print(company_name)
# print(location_name)
# print(job_skill)
# csv file
file_list = [job_title, company_name, job_date, location_name, job_skill, links, responsibilities]
exported = zip_longest(*file_list)
with open("/users/islam/desktop/isla_test.csv", "w") as myfile:
    wr = csv.writer(myfile, delimiter=';')
    wr.writerow(["Job Title", "Company Name", "date", "Location", "Skills", "links", "responsibilities"])
    wr.writerows(exported)
