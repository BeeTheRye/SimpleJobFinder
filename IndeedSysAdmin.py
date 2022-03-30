# Find Sys Admin Jobs on indeed
import requests
from bs4 import BeautifulSoup
import pandas as pd
def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
    url = f'https://www.indeed.com/jobs?q=system administrator&l=Remote&remotejob=032b3046-06a3-4876-8dfd-474eb5e7ed11&start={page}'
    r=requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup
def transform(soup):
    divs= soup.find_all('div', class_ = 'slider_container')
    for item in divs:
        title=item.find('h2').text.strip()
        company = item.find('span', class_ ='companyName').text.strip()
        try:
            salary = item.find('div', class_ = "attribute_snippet").text.strip()
        except:
            salary = ''
        summary = item.find('div', class_ ='job-snippet').text.strip().replace('\n','')
        job = {
            'title' : title,
            'company': company,
            'salary': salary,
            'summary': summary,
        }
        joblist.append(job)
    return
joblist=[]
for i in range(0,100, 10):
    print (f"getting page,{i}")
    c = extract(0)
    transform(c)
df = pd.DataFrame(joblist)
print (df.head())
df.to_html('JobResults.html')
