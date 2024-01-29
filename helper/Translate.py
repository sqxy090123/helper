import requests
from bs4 import BeautifulSoup

class Translate:
    @staticmethod
    def auto(string):
        url = f"https://fanyi.so.com/?q=calms&src=tab_hyc#{string}"
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        divs = soup.find_all('div')
        for div in divs:
            print("div")
            navs = div.find_all('nav', _class="sidebar")
            for nav in navs:
                print('nav')
                sections = nav.find_all('section', _class="simple-paraphrase block")
                for section in sections:
                    print('section')
                    ps = section.find(div, _class="comment top5").find_all('p', _class="bottom4")
                    for p in ps:
                        if p is not None:
                            print("翻译结果：", p.text)
                        else:
                            print("p")
