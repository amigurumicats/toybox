import requests
import lxml.html
import random

url = 'https://shindanmaker.com/XXXXXX'
max_num = 50


def random_name():
    src_str = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(src_str) for _ in range(15))


if __name__ == '__main__':
    s = requests.Session()
    payload = {'u': ''}
    for _ in range(max_num):
        payload['u'] = random_name()
        r = s.post(url, data=payload)
        root = lxml.html.fromstring(r.text)
        res = root.xpath('//div[@class="result2"]')
        text = res[0].text_content()
        print(text.strip())

