from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
  print("Can't request website")
else:
  soup = BeautifulSoup(response.text,"html.parser")
  jobs = soup.find_all('section', class_="jobs")
  for job_section  in jobs:
    # job posts 란 section안에 있는 모든 li들 이다
    job_posts = job_section.find_all('li')
    # li안의 코드를 실행하기 위해 for loop를 돌린다
    # list의 마지막에 있는 view - all 버튼을 지워주기 위해 list의 마지막 요소를 제거 해준다 왜냐하면 view-all버튼은 li태그들 중에 항상 마지막에 있으므로
    job_posts.pop(-1)
    for post in job_posts:
      print(post)
      print("/////////////")
  