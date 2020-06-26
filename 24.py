import re
def date(url):
        return re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)
url1= "https://www.com/news/2020/06/26/asf"
print(date(url1))