import requests
import re


# jike = 'http://www.jikexueyuan.com/course'
#
# listClass = requests.get(jike)
# cf = re.findall('<ul class="cf" (.*?)</ul>', listClass.text, re.S)
#
# li_id = re.findall(r'<li id="(.*?)</li>', cf[0], re.S)
#
# f = open('C:/Users/BlueSky/Desktop/titl.txt', 'a')
# for li in li_id:
#     li = li.replace('\n', '').replace('\t', '')
#     title = re.findall('class="lessonimg" title="(.*?)" alt="', li, re.S)
#     intrduce = re.findall('<p style="height: 0px; opacity: 0; display: none;">(.*?)</p>', li, re.S)
#     time = re.findall('<dd class="mar-b8"><i class="time-icon"></i><em>(.*?)</em>', li, re.S)
#     level = re.findall('<i class="xinhao-icon\d?"></i><em>(.*?)</em>', li, re.S)
#     people = re.findall('<em class="learn-number">(.*?)</em>', li, re.S)
#     f.writelines('[' + title[0] + '],[' + intrduce[0] + '],[' + time[0] + '],[' + level[0] + '],[' + people[0] + ']\n')
#
# f.closed()


def changepage(url, total_page):
    now_page = int(re.search('pageNum=(\d+)', url, re.S).group(1))
    print(now_page)
    page_group = []
    for i in range(now_page, total_page + 1):
        link = re.sub('pageNum=\d+', 'pageNum=%s' % i, url, re.S)
        page_group.append(link)
    return page_group


print(changepage('http://www.jikexueyuan.com/course?pageNum=1', 20))
