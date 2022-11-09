from requests import get
from bs4 import BeautifulSoup
# python에게 이 extractors 폴더의 wwr 파일에 있는 extract_jobs를 import 하라고 하는 것!
# 하지만 나중에 indeed에서도 job들을 추출할 거니까 이이름을 extract_wwr_jobs로 바꾼다.
from extractors.wwr import extract_wwr_jobs

# 함수를 밖에서 가져와서 사용 한 후 jobs 객체로 저장 ( 나중에 사용하기위해 우선 주석처리!)
# jobs = extract_wwr_jobs("python")
# print(jobs)


# 우리가 한 것은 모든 코드를 extract_wwr_jobs 안에 넣었고
# 이 function은 extractors 폴더 안에 있고 extarct_wwr_jobs는 하나의 parameter를 받을 것이다.
#  사용자가 보낸 입력 값(keyword)가 더해진 url을 받을 것이다
# results를 반환할 것이다 . 왜냐하면 나중에 이 데이터와 다음 번에 만들 extractors에서 나온 데이터를 더한 모든 데이터를 파일에 넣고 싶기 때문이다.
# 따라서 이번 과정에서 처음으로 우리가 만든 함수를 다른 폴더에 만들어 main에서 밖에서 만듬 함수를 가져오는 코드를 작성해보았다.(주의!!!!!폴더명,파일명,함수명을 오타가 없이 잘 작성해야 한다!)
#  이번 과정(폴더와 파일을 만들어서 전에 만들었던 함수를 호출)을 통해 리팩토링을 마무리 했다.