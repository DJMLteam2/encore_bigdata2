# 삼성전자 현재 시각 기준 거래가를 출력하는 함수입니다.
def samsung_price():
    import requests, re
    from bs4 import BeautifulSoup as bs
    
    stock_code = "005930"
    url = f"https://finance.naver.com/item/sise_day.naver?code={stock_code}&page=1"
    response = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
    
    soup = bs(response.text, 'html.parser')
    price = soup.select_one("span.tah.p11").text
    
    print(f"현재 가격은 {price}원입니다.")