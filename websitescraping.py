from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=&cboWorkExp1=-1").text
    # print(html_text)
    print('Put some skills that you are not familiar with')
    unfamiliar_skill = input('>')
    print(f'Filtering out {unfamiliar_skill}')

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company Name : {company_name.strip()} \n')
                    f.write(f'Skills : {skills.strip()} \n')
                    f.write(f'More Info : {more_info} \n')
                print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} seconds... ')
        time.sleep(time_wait = 60)


                         # "https://www.yelp.com/search?find_desc=Restaurants&find_loc=Atlanta%2C+GA&start=0").text
# https://www.yelp.com/search?find_desc=Restaurants&find_loc=Atlanta%2C+GA&start=10
# https://www.yelp.com/search?find_desc=Restaurants&find_loc=Atlanta%2C+GA&start=20
