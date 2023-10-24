from datetime import datetime

def today_felicette():
    now = datetime.now()
    print("현재 : ", now)
    print("현재 날짜 : ", now.date())
    print("현재 시간 : ", now.time())
    print("timestamp : ", now.timestamp())
    print("년 : ", now.year)
    print("월 : ", now.month)
    print("일 : ", now.day)
    print("시 : ", now.hour)
    print("분 : ", now.minute)
    print("초 : ", now.second)
    print("마이크로초 : ", now.microsecond)
    print("요일 : ", now.weekday())
    print("문자열 변환 : ", now.strftime('%Y-%m-%d %H:%M:%S'))