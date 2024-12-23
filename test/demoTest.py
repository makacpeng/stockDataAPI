import urllib.request

import requests

# urllib.request.urlretrieve("http://172.28.25.148:5002/getData", '股票数据.xlsx')

response = requests.get("http://172.19.189.83:5003/getDayData/SH000001")
print(response.text)