from django.shortcuts import render, HttpResponse
from bs4 import BeautifulSoup
import requests

linkedin_url = 'https://ke.linkedin.com/jobs/python-jobs?position=1&pageNum=0'
page1 = requests.get(linkedin_url)
soup = BeautifulSoup(page1.content, 'html.parser')
results = soup.find_all('ul', class_='jobs-search__results-list')

# print(title.text.strip())
# print(sub_title.text.strip())
# print(location.text.strip())
# print(time.text.strip())
# print('#################################################################################')
jobs = []
for x in results:
    info = x.find_all('li')
    for y in info:
        title = y.find('h3', class_='base-search-card__title')
        sub_title = y.find('h4', class_='base-search-card__subtitle')
        location = y.find('span', class_='job-search-card__location')
        time = y.find('time', class_='job-search-card__listdate')
        job_list = {
            'job': title.text,
            'subtitle': sub_title.text,
            'location': location.text,
        }
        jobs.append(job_list)


def homepage(request):
    return render(request, 'home.html', {'items': jobs})

