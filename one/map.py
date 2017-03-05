from multiprocessing.dummy import Pool
import requests
import time


# result = pool.map(,)

def getSource(url):
    html = requests.get(url)
    print('ccc')


urls = []

for i in range(1, 151, 50):
    newpage = 'http://tieba.baidu.com/f?kw=java&ie=utf-8&pn=' + str(i)
    urls.append(newpage)

time1 = time.time()

for i in urls:
    print(i)
    getSource(i)
time2 = time.time()
print("single thread time is:" + str(time2 - time1))

pool = Pool(4)
time3 = time.time()
result = pool.map(getSource, urls)
pool.close()
pool.join()
time4 = time.time()
print("muiltxi thread time is" + str(time4 - time3))
