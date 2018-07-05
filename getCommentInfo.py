import urllib
import urllib.request
import urllib.parse
import string
import time
from bs4 import BeautifulSoup
from Spider.beautifulsoup.mylog import Mylog as mylog


class Item(object):
    title = None    # 标题
    firstAuthor = None  # 创建者
    firstTime = None    # 创建时间
    reNum = None    #总回复数
    content = None  # 最后回复内容
    lastAuthor = None # 最后回复者
    lastTime = None # 最后回复时间


class GetTieBaInfo(object):
    def __init__(self, url):
        self.url = url
        self.log = mylog()
        self.pageSum = 1
        self.urls = self.getUrls(self.pageSum)
        self.items = self.spider(self.urls)
        self.pipelines(self.items)


    def getUrls(self, pageSum):
        urls = []
        pns = [str(i*50) for i in range(pageSum)]
        ul = self.url.split('=')
        for pn in pns:
            ul[-1] = pn
            url = '='.join(ul)
            urls.append(url)
        self.log.info("获取urls成功")
        return urls



    def spider(self, urls):
        items = []
        for url in urls:
            htmlContent = self.getResponseContent(url)
            soup = BeautifulSoup(htmlContent, "lxml")
            tagsli = soup.find_all('li', attrs={'class':' j_thread_list clearfix'})
            for tag in tagsli:
                item = Item()
                item.title = tag.find('a', attrs={'class':'j_th_tit'}).get_text().strip()
                item.firstAuthor = tag.find('span', attrs={'class':'frs-author-name-wrap'}).a.get_text().strip()
                item.firstTime = tag.find('span', attrs={'title':'创建时间'}).get_text().strip()
                item.reNum = tag.find('span', attrs={'title':'回复'}).get_text().strip()
                item.content = tag.find('div', attrs={'class':'threadlist_abs threadlist_abs_onlyline '}).get_text().strip()
                item.lastAuthor = tag.find('span', attrs={'class':'tb_icon_author_rely j_replyer'}).a.get_text().strip()
                item.lastTime = tag.find('span', attrs={'title':'最后回复时间'}).get_text().strip()
                items.append(item)
                self.log.info('获取标题为<<%s>>的项成功' % item.title)
                time.sleep(2)
        return items


    def pipelines(self, items):
        fileName = "百度贴吧_权利的游戏.txt"
        with open(fileName, 'w', encoding='utf8') as fp:
            for item in items:
                fp.write('title:%s\nauthor:%s\nfirstTime:%s\ncontent:%s\nreturn:%s\nlastAuthor:%s\nlastTime:%s\n\n\n'
                        % (item.title, item.firstAuthor, item.firstTime, item.content, item.reNum, item.lastAuthor, item.lastTime))
                self.log.info('标题为<<%s>>的项目输入成功' % item.title)


    def getResponseContent(self, url):
        try:
            url = urllib.parse.quote(url, safe=string.printable)
            response = urllib.request.urlopen(url)
        except:
            self.log.error('返回%s数据失败' % url)
        else:
            self.log.info('返回%s数据成功' % url)
            return response.read()


if __name__ == "__main__":
    url = "http://tieba.baidu.com/f?kw=权利的游戏&ie=utf-8&pn=50"
    GTI = GetTieBaInfo(url)
    # print(GTI.getUrls(1))
    # print(GTI.spider(url))