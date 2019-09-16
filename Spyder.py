
from bs4 import BeautifulSoup
import requests

ImagePath = "C:\Spyder"
Number = 1
for i in range(1,10):
    urlformat = "https://tieba.baidu.com/p/6114963534?pn={num}"
    url = urlformat.format(num = i)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"}
    req = requests.get(url = url,headers = headers)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html,'lxml')
    targets_url = bf.find_all(class_= "BDE_Image")
    list_url = []
    for each in targets_url:
        list_url.append(each.get('src') )
        Number += 1
        r = requests.get(url = str(each.get('src')),headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"})
        r.encoding = 'utf-8'
        open('C:\\Spyder\\' + str(Number) + ".jpg", 'wb').write(r.content)
    del req
    print(list_url)
    print("Spyder Done")


