import requests
from bs4 import BeautifulSoup

with requests.Session() as session:
    post = session.post('http://vns.lpnu.ua/login/index.php',
                        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.44'}, 
                        data={'username': 'Oleh.Pykulytskyi.ki.2018', 'password': '15.09.2000',
                              'logintoken': 'lpXe0JqD7uux8BIGvAECBuW12YqvJaLQ'})
    r = session.get('http://vns.lpnu.ua/my/')
    soup = BeautifulSoup(r.text, 'html.parser')
    print(r.text)