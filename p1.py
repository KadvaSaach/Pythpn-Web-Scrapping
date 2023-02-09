import time
from bs4 import BeautifulSoup
import requests

# html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
# # print(html_text)

# soup = BeautifulSoup(html_text, 'lxml')

# ------------------------------Version 1.0 ------------------------------
# job = soup.find('li', class_='clearfix job-bx wht-shd-bx')
# jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
# # print(job)
# # print(jobs)
# company = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
# skills = job.find('span', class_='srp-skills').text.replace(' ','')
# published_date = job.find('span', class_='sim-posted').span.text
# # print(company)
# # print(skills)
# print(published_date)

# # print(f'''
# # Company Name : {company}
# # Required Skill : {skills}
# # ''')
# ------------------------------Version 1.0 ------------------------------


print("Put some skills that you are not familiar with")
unfamiliar_skills = input('>')
print(f"Filtering out {unfamiliar_skills}")

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_='srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skills not in skills:
                with open(f'poss/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More info: {more_info}")
                print(f"File Saved: {index}")


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting  {time_wait} min....')
        time.sleep(time_wait * 1)