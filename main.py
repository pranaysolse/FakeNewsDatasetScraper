from bs4 import BeautifulSoup
import requests
class Factdb:

    a = [
        'https://www.thip.media/category/health-news-fact-check/',
        'https://www.thip.media/category/health-news-fact-check/page/2',
        'https://www.thip.media/category/health-news-fact-check/page/3',
        'https://www.thip.media/category/health-news-fact-check/page/4',
        'https://www.thip.media/category/health-news-fact-check/page/5',
        'https://www.thip.media/category/health-news-fact-check/page/6',
        'https://www.thip.media/category/health-news-fact-check/page/7',
        'https://www.thip.media/category/health-news-fact-check/page/8',
        'https://www.thip.media/category/health-news-fact-check/page/9',
    ]

    def __init__(self, website):
        self.website = website


    def getpage(self,website):
        page = requests.get(website)
        return page

    def parse_html(selfself,html):
        return BeautifulSoup(html.content, 'html.parser')


    def findpattern(self,page,pattern,tag):
        return page.find_all(tag, class_=pattern)


if __name__ == '__main__':
    parent_sites = [
        'https://www.thip.media/category/health-news-fact-check/',
        'https://www.thip.media/category/health-news-fact-check/page/2',
        'https://www.thip.media/category/health-news-fact-check/page/3',
        'https://www.thip.media/category/health-news-fact-check/page/4',
        'https://www.thip.media/category/health-news-fact-check/page/5',
        'https://www.thip.media/category/health-news-fact-check/page/6',
        'https://www.thip.media/category/health-news-fact-check/page/7',
        'https://www.thip.media/category/health-news-fact-check/page/8',
        'https://www.thip.media/category/health-news-fact-check/page/9',
    ]
    all_sites = []
    for i in parent_sites:
        a = Factdb(i)
        s = a.findpattern(a.parse_html(a.getpage(a.website)), 'entry-title td-module-title','h3')
        for j in s:
            all_sites.append(str(j.find('a')['href']))
    for alls in all_sites:
        print(alls)

    for s in all_sites:
        m = Factdb(s)
        res =m.findpattern(m.parse_html(m.getpage(m.website)), 'wp-block-media-text__content','div')
        for ak in res:
            print('result: ', ak.find('p')('strong'), 'paragraph:', ak.find('p'))

    current = Factdb('https://www.thip.media/health-news-fact-check/fact-check-drinking-cold-water-after-meal-causes-cancer/4779/')
    res =current.findpattern(current.parse_html(current.getpage(current.website)), 'wp-block-media-text__content')
    print()
    print()
    print('--------------------------------------------------------------')
    for i in res:
        print(i)

