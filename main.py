from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
# 여기서 문자를 바꿔주면 내가 찾고 싶은 단어를 이용해 데이터에서 찾아올 수 있다.
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
  print("Can't request website")
else:

  results = []
  
  soup = BeautifulSoup(response.text,"html.parser")
  jobs = soup.find_all('section', class_="jobs")
  for job_section  in jobs:
    # job posts 란 section안에 있는 모든 li들 이다
    job_posts = job_section.find_all('li')
    # li안의 코드를 실행하기 위해 for loop를 돌린다
    # list의 마지막에 있는 view - all 버튼을 지워주기 위해 list의 마지막 요소를 제거 해준다 왜냐하면 view-all버튼은 li태그들 중에 항상 마지막에 있으므로
    job_posts.pop(-1)
    
    
    for post in job_posts:
      # job_posts에서 a태그들을 가져와 anchors라는 list를 만든다(list형태로 저장)
      anchors = post.find_all('a')
      #첫 번째 a태그는 로고를 만드는 것이므로 데이터를 가져오는 것에 필요가 없기 때문에 지워준다.
      #두 번째 a태그에 대한 데이터만을 가져온다
      anchor = anchors[1]
      #beautifulsoup로 인하여 파이썬 딕셔너리의 형태로 코드를 작성하여 데이터를 확인할 수 있다.
      # 파이썬의 딕셔너리 형태의 코드로 데이터를 가져오기(링크를 가져와 나중에 엑셀에 저장 하기 위해)
      link = anchor['href']

      # 위에서 작성한 anchor태그의 두 번째 안에 있는 span태그이며, class이름이 company를 가진 것을 가져와 list 만들기
      company, kind , region = anchor.find_all('span', class_="company")

      # 이번엔 title을 가져오기
      # find_all은 태그가 여러 개 일 경우 list로 가져오지만 title태그는 하나밖에 없으므로 find로 데이터를 가져온다
      #이렇게 job의 title을 얻었으니 title에 저장하기(find_all 이 아니므로 하나의 변수로 저장)
      title = anchor.find('span', class_="title") 
      #데이터를 데이터 구조(딕셔너리 형태) 안에 넣기 
      job_data = {
        'company' : company.string,
        'region' : region.string,
        'position' : title.string
      }
      # job을 추출할 때 마다 result 배열에 추가적으로 저장해줘야한다.
      # 이렇게 하지 않으면 job for loop를 돌 때마다 초기화가 되기 때문이다(job 각각이 저장되지 않는다 + for loop안에서만 저장되어 있다)
      #for loop가 끝나도 result list에 저장되어 있기 때문에 사라지지 않아!
      results.append(job_data)


# 이 python list를 만들었고, 즉 이제 for resulit in을 사용 가능 하다.

  for result in results:
    print(result)
    print("///////////////////////////////////////////////////////////////")

# 이제 web의 html에 대한 것들을 모두 python 형태의 데이터로 가져왔으니 이것을 파일안에 저장할 수 있다.
