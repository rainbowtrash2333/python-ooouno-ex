import requests
from urllib.parse import urlencode
from random import choice


def post():
    base_url = 'https://learning.cbit.com.cn/www/lessonDetails/updateLessonProcessPC.do'
    data = {
        'lessonId': '630d845d295b4a9ebcf65f74a4dbc34b',
        'lessonItemId': 'ce63b66eb1154bcb8161cce8c4c1ddbc',
        'process': '-2',
        'tcid': 'null',
        'totalTime': '2050.2',
        'suspendTime': '2050.2',
        'studytime': '2050.2'
    }
    query_string = urlencode(data)
    url = "learning.cbit.com.cn/www/lessonDetails/updateLessonProcessPC.do" + query_string
    print(url)
    token = 'eyJ0eXAiOiJKV1QiLCJ0eXBlIjoiSldUIiwiZW5jcnlwdGlvbiI6IkhTMjU2IiwiYWxnIjoiSFMyNTYifQ.eyJUaW1lIjoxNjg0MTE0MjM1MTEwLCJleHAiOjE2ODQyMDA2MzUsInVzZXJJZCI6IjNkY2U4ZmUxMWU0ZjRmMjdiYTJlNTViMTIzZTkzOWU2IiwidXNlckNvZGUiOiIxOTE4NDIzNjI0NCJ9.M3bqchWtDWr1PDufAY06Kanu7SfbczTdEg8cug0Jd1g'
    cookie = 'AlteonP=0a140c030aff050635b479941b13; JSESSIONID=kEMdB9-CXKAsuJIqMWycu9cTiCdFfb9o-J4hkIWIMTTsHwtJ8MZx!-1212995460',
    # 3.随机设置请求头信息
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Cookie': cookie,
        'Host': 'learning.cbit.com.cn',
        'Origin': 'https://learning.cbit.com.cn',
        'Referer': 'https://learning.cbit.com.cn/www/views/lesson/mp4Play.html?le_id=630d845d295b4a9ebcf65f74a4dbc34b&itemid=2edde657a8194a71b5e34372e1e3bb49&lindex=1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'apikey': '2456269a445b4a18afad29fd12714da2',
        'isapp': '0',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'token': token
    }
    # 5.发送请求并打印返回值

    response = requests.post(url, data=data, headers=headers)

    print(response.text)


def get_lessons():
    base_url = 'https://learning.cbit.com.cn/www/onlineTraining/trainingdetails.do'
    data = {
        'id': 'e491bf3476e64fe19f61e472c7a41480'
    }
    url = base_url + urlencode(data)
    

if __name__ == '__main__':
    post()